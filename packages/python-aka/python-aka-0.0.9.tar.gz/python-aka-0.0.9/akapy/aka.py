"""
Beefy bits of the akapy
"""

import logging
import sys
import curlify


class Api(object):
    """
    API Object
    """

    def __init__(self, aka_base, credentials):
        self.aka_base = aka_base
        self.credentials = (credentials['username'], credentials['password'])

    @classmethod
    def print_errors(cls, errors):
        """
        Print errors array from an aka api call
        """
        for item in errors:
            logging.info(item)

    @classmethod
    def print_notices(cls, notices):
        """
        Print notices array from an aka api call
        """
        for notice in notices:
            logging.info(notice)

    def register_next_available(self, network, hostname):
        """
        Register the next IP in a network
        """
        post_items = {'cidr': network, 'hostname': hostname}
        new_ip_info = self.query_path(
            'ip4/subnets/%s/register_next_available' % network,
            params=post_items,
            method='post')

        return new_ip_info

    def search_dns(self, *args, **kwargs):
        """
        Given a DNS name, return matching names

        Required Args:
          name str: Name to search

        Params:
          record_type str: Only return records of this type (Default 'A')

        Returns:
          list of matching DNS entries
        """

        name = args[0]
        record_type = kwargs.get('record_type', 'A')

        records = []

        for item in self.query_path('dns/%s' % name):

            # Match record types
            if item['type'] != record_type:
                continue

            records.append(item)

        return records

    def query_path(self, path, params={}, method='get', success_codes=[200]):
        """
        Do the actual API query here
        """
        import requests
        url = "%s/api/v1/%s" % (self.aka_base, path)
        logging.debug("URL: %s PARAMS: %s METHOD: %s", url, params, method)

        if method == 'get':
            result = requests.get(url, auth=self.credentials, params=params)
        elif method == 'put':
            result = requests.put(url, auth=self.credentials, params=params)
        elif method == 'post':
            result = requests.post(url, auth=self.credentials, params=params)
        elif method == 'delete':
            result = requests.delete(url, auth=self.credentials, params=params)
        else:
            logging.error("Invalid method: %s", method)
            sys.exit(2)

        try:
            real_result = result.json()
        except Exception as e:
            real_result = result

        logging.debug("CURL Command:")
        logging.debug("%s" % curlify.to_curl(result.request))
        result.raise_for_status()
        #       if result.status_code not in success_codes:
        #           logging.error("Got code %s instead of %s" %
        #                         (result.status_code, success_codes))
        #       logging.debug("Got code %s" % result.status_code)

        if 'error' in real_result:
            logging.error("Error in request, quitting: %s",
                          real_result['error'])
            sys.exit(2)

        if 'notices' in real_result:
            self.print_notices(real_result['notices'])

        if 'errors' in real_result:
            self.print_errors(real_result['errors'])
            logging.error("Quitting because of errors")
            sys.exit(2)

        return real_result

    def delete_dns(self, dns_name):
        """
        Delete an IP Address
        """
        logging.info("Deleting DNS: %s", dns_name)
        # We are deleting both, so just get that first one
        items = self.search_dns(dns_name)
        if len(items) > 0:
            item = items[0]
            self.query_path(
                'dns/%s/%s/%s' %
                (item['backend_name'], item['type'], item['address']),
                method='delete')

        return True

    def delete_ip(self, ip_address):
        """
        Delete an IP Address
        """
        logging.info("Deleting IP: %s", ip_address)
        self.query_path('ip/%s' % ip_address,
                        params={'ip': ip_address},
                        method='delete')

        return True

    def get_ip(self, ip_address):
        """
        Get information on an IP address
        """
        return self.query_path('ip/%s' % ip_address,
                               params={'ip': ip_address},
                               method='get')

    def guess_ttl(self, target):
        """
        Given a thing that looks like some sort of DNS record, do your best try
        and figuring out what the TTL should be
        """
        # Handle dns records
        return self.query_path('/dns/%s' % target,
                               params={'name': target},
                               method='get')[0]['ttl']

    def register_cname(self, cname, hostname, ttl=3600):
        """
        Register a new cname to a host
        """
        params = {
            'name': cname,
            'type': 'CNAME',
            'ttl': ttl,
            'target': hostname
        }

        self.query_path('dns', method='post', params=params)

        return True

    def register_a(self, name, ip, ttl=3600):
        """
        Register a new cname to a host
        """
        params = {'name': name, 'type': 'A', 'ttl': ttl, 'address': ip}

        self.query_path('dns', method='post', params=params)

        return True

    def get_network(self, network):
        """
        Get network information based on CIDR
        """
        return self.query_path('ip4/subnets/%s' % network)

    def validate_network(self, network):
        """
        Validate that this is a real network
        """
        try:
            self.query_path('ip4/subnets/%s' % network)
            is_valid = True
        except Exception as e:
            is_valid = None

        return is_valid

    def validate_hostname(self, hostname):
        """

        Validate that this is a real hostname/A record.  If it's real, return
        the IP, otherwise return None

        """
        results = self.query_path('dns/%s' % hostname)
        if len(results) != 1:
            return None
        else:
            return results[0]['address']

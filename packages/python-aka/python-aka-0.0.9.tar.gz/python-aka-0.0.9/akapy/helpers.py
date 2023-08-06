"""
Helper functions
"""
import os
import sys
import logging
class CredentialParser(object):
    """
    Import credentials for connecting to AKA

    This file should look something like:
    [https://aka.oit.duke.edu]
    user = joeuser
    key = 11111111-2222-3333-4444-555555555555

    [https://aka-test.oit.duke.edu]
    user = joeuser
    key = aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def import_credentials(self):
        """
    	Pull in your credentials
    	"""
        cred_file = os.path.expanduser("~/.akarc")
        if not os.path.exists(cred_file):
            sys.exit("%s is required" % cred_file)
        import configparser
        config = configparser.ConfigParser()
        config.read(cred_file)

        creds = {}
        creds['username'] = config.get(self.base_url, "user")
        creds['password'] = config.get(self.base_url, "key")
        return creds

def cidr_to_netmask(cidr):
    """
    Take a CIDR and conver it to the subnet that redhat ifconfig files use

    Heavily borrowed from:
    http://stackoverflow.com/questions/33750233/convert-cidr-to-subnet-mask-in-python
    """
    import socket
    import struct
    net_bits = cidr.split('/')[1]
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return netmask


def dns_lookup(dns_name):
    """
    Simple DNS lookup
    """
    import socket
    try:
        return socket.gethostbyname(dns_name)
    except socket.gaierror:
        return None


def is_pingable(hostname):
    """
    Check if a host or ip pings
    """
    response = os.system("ping -c 1 %s &>/dev/null" % hostname)
    if response == 0:
        return True
    else:
        return None

def wait_until_it_pings(target):
    """
    Pause until a host actually pings
    """
    import time
    logging.info("Waiting until %s is pingable", target)
    pings = None
    while not pings:
        if is_pingable(target):
            pings = True
            break
        else:
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(5)

def pp_results(results):
    """
    Print list of results (or just results)
    """
    if isinstance(results, list):
        for result in results:
            pp_result(result)
            print()
    else:
        pp_result(results)

def pp_result(result):
    """
    Print out json results in a pretty way (Pretty Print)
    """
    from datetime import timedelta
    import humanize
    for name, value in result.items():
        if name == 'ttl':
            natty_time = humanize.\
                naturaltime(timedelta(seconds=int(value))).\
                replace(" ago", "")
            hr_value = '%s (or %s seconds)' % (natty_time, value)
        elif name == 'last_registered':
            hr_value = naturalize_day(value)
        elif name == 'last_unregistered':
            hr_value = naturalize_day(value)
        elif name == 'last_seen':
            hr_value = naturalize_day(value)
        else:
            hr_value = value
        print("%-20s %-5s" % (name, hr_value))

def naturalize_day(value):
    """
    Given an ISO date, return something human readable
    """
    import humanize
    from dateutil import parser
    try:
        natty_time = humanize.naturalday(parser.parse(value))
    except:
        natty_time = value
    hr_value = '%s (%s)' % (natty_time, value)
    return hr_value

def is_ipaddress(target):
    """
    Check if a string is an IP address
    """
    from IPy import IP
    try:
        IP(target)
        return True
    except:
        return False

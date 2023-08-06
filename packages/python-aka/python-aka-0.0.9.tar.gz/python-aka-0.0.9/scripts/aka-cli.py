#!/usr/bin/env python3
"""
Command line interface to AKA
"""
import argparse
import sys
import os

import logging
from akapy.helpers import CredentialParser, pp_results, is_ipaddress
from akapy.aka import Api


def parse_arguments():
    """
    Handle argument parsing here
    """
    parser = argparse.ArgumentParser(
        description='Command line application for the AKA application')
    subparsers = parser.add_subparsers(dest='action',
                                       help='sub-command help',
                                       required=True)
    parser_query = subparsers.add_parser('query', help='query AKA')
    parser_query.add_argument('target', type=str, help='Entry to query')
    parser_sysconfig = subparsers.add_parser(
        'sysconfig', help='Print out a sysconfig record for a hostname or ip')
    parser_sysconfig.add_argument('target',
                                  type=str,
                                  help='Entry to show a sysconfig on')
    parser_sysconfig.add_argument('-d',
                                  '--device',
                                  type=str,
                                  default='eth0',
                                  help='Device to use in sysconfig')
    parser_update = subparsers.add_parser('update', help='Update a record')
    parser_update.add_argument('target',
                               type=str,
                               help='Target record to update')
    parser_update.add_argument('-t',
                               '--type',
                               type=str,
                               help='Type of record to update',
                               default='A')
    parser_update.add_argument('--ttl',
                               type=str,
                               help='Update the Time to Live for this record')
    subparsers.add_parser('zones', help='Print out a list of zones')
    subparsers.add_parser('subnets', help='Print out a list of subnets')
    setup_a = subparsers.add_parser(
        'setup-a',
        help='Create an A record.  If it exists, delete and recreate it')
    setup_a.add_argument('dns_name', help='DNS Name for A record', type=str)
    setup_a.add_argument('ip_address',
                         help='IP Address for A record',
                         type=str)
    return parser.parse_args()


args = parse_arguments()

if 'AKA_BASE_URL' in os.environ:
    AKA_BASE = os.environ['AKA_BASE_URL']
else:
    AKA_BASE = "https://aka.oit.duke.edu"

cred_parser = CredentialParser(AKA_BASE)
cred = cred_parser.import_credentials()
AKA = Api(AKA_BASE, cred)


def main():
    """
    Main process for application
    """
    if args.action == 'query':
        if is_ipaddress(args.target):
            res = AKA.query_path('ip/%s' % args.target, method='get')
            pp_results(res)
            print()
            for title, res in AKA.query_path("ip/%s/dns_records" % args.target,
                                             method='get').iteritems():
                print("DNS Records for %s" % title)
                pp_results(res)
        else:
            res = AKA.query_path('dns/%s' % args.target, method='get')
            pp_results(res)
    elif args.action == 'setup-a':
        existing_records = AKA.search_dns(args.dns_name)
        if len(existing_records) > 0:
            print("Deleting existing records for %s" % args.dns_name)
            AKA.delete_dns(args.dns_name)

        res = AKA.register_a(args.dns_name, args.ip_address)
        if res:
            print("Successfully registered %s to %s" %
                  (args.dns_name, args.ip_address))
            return 0
        else:
            print("Failed to register %s" % args.dns_name)
            return 2

    elif args.action == 'sysconfig':
        from IPy import IP
        if is_ipaddress(args.target):
            ip_res = AKA.query_path('ip/%s' % args.target)
        else:
            dns_res = AKA.query_path('dns/%s' % args.target)
            ip_res = AKA.query_path('ip/%s' % dns_res[0]['address'])

        ip = ip_res['ip']
        network_obj = IP(ip_res['subnet'])
        network_long_netmask = network_obj.strNormal(2).split("/")[1].strip()
        gateway = AKA.query_path('ip4/subnets/%s' %
                                 ip_res['subnet'])['gateway']

        print("DEVICE=%s" % args.device)
        print("IPADDR=%s" % ip)
        print("GATEWAY=%s" % gateway)
        print("NETMASK=%s" % network_long_netmask)
        print("TYPE=Ethernet")
        print("BOOTPROTO=none")
        print("IPV6INIT=no")
        print("USERCTL=yes")

    elif args.action == 'zones':
        res = AKA.query_path('/dns/zones')
        pp_results(res)

    elif args.action == 'subnets':
        res = AKA.query_path('/ip4/subnets')
        print("%-20s %-60s %-20s" % ('cidr', 'name', 'gateway'))
        for item in res:

            # Ug, some netwoks don't have names 😔
            if not item['name']:
                item_name = 'NO_NAME'
            else:
                item_name = item['name']
                item_name = item_name.replace('\u2013', '-')

            try:
                print(
                    "%-20s %-60s %-20s" %
                    (item['cidr'], item_name.decode('utf-8'), item['gateway']))
            except UnicodeEncodeError:
                # TODO: Handle unicode strings
                logging.error(
                    "%s has unicode characters in it, skipping for now\n" %
                    item)
                continue

    elif args.action == 'update':
        if args.type == 'A':
            records = AKA.query_path('/dns/%s' % args.target)
            print(records)
            for item in records:
                post_items = {
                    'backend_name': item['backend_name'],
                    'type': args.type,
                    'value': item['address']
                }

                # Update TTL here
                # TODO:  Handle things like 5m, 24h, etc
                if args.ttl:
                    post_items['ttl'] = args.ttl

                res = AKA.query_path(
                    'dns/%s/%s/%s' %
                    (item['backend_name'], args.type, item['address']),
                    params=post_items,
                    method='put')
                for notice in res['notices']:
                    print(notice)
                for alert in res['alerts']:
                    print(alert)
        else:
            sys.stderr.write("This doesn't handle %s records yet\n" %
                             args.type)
            return 255

    return 0


if __name__ == "__main__":
    sys.exit(main())

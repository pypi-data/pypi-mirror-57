#!/usr/bin/env python
"""
Find important information out about a VM
"""
import sys
import os
import atexit
from pyVim import connect

def get_esxi_info_from_vm(target_vm):
    """
    Main subroutine
    """
    ## Sadly we gotta have this in here
    import ssl
    try:
        create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = create_unverified_https_context

    vsphere_rc = os.path.expanduser('~/.vsphererc')
    if not os.path.exists(vsphere_rc):
        sys.exit("%s is required" % vsphere_rc)
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read(vsphere_rc)

    vmware_clusters = config.sections()

    import socket
    ipaddress = socket.gethostbyname(target_vm)

    for vmware_cluster in vmware_clusters:
        username = config.get(vmware_cluster, 'ro_username')
        password = config.get(vmware_cluster, 'ro_password')
        service_instance = connect.SmartConnect(
            host=vmware_cluster,
            user=username,
            pwd=password,
            port=443
        )
        atexit.register(connect.Disconnect, service_instance)

        datacenters = service_instance.RetrieveContent().rootFolder.childEntity
        for datacenter in datacenters:
            searcher = service_instance.content.searchIndex
            virt_machine = searcher.FindByIp(datacenter=datacenter, ip=ipaddress, vmSearch=True)
            if virt_machine:
                return {
                    'cluster': vmware_cluster,
                    'datacenter': datacenter.name,
                    'esx_host': virt_machine.summary.runtime.host.name
                }

    ## If we make it here, we couldn't find it :(
    return None

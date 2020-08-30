#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest='target', help='IP address or Set IP range ')
    (options, arguments) = parser.parse_args()
    return options

def scan(ip):
    arp_req=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast=broadcast/arp_req
    answered=scapy.srp(arp_req_broadcast,timeout=1,verbose=False)[0]

    client_list=[]
    for element in answered:
        client_dict={"ip":element[1].psrc,"MAC":element[1].hwdst}
        client_list.append(client_dict)

    return (client_list)
def printt(result):
    print("IP\t\t\tMac Address\n--------------------------------------------")
    for data in result:
        print(data["ip"]+" \t\t"+data["MAC"])

ipdata = get_arguments()
ip_address=scan(ipdata.target)
printt(ip_address)

#!/usr/bin/env python3

import re
import binascii
import socket
import struct
import fcntl

if __name__ =="__main__":
    '''
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    nic = "wlp1s0"
    ip = socket.gethostbyname(socket.gethostname())
    #test = IPv4Network(ip)
    test = ipaddress.ip_network(ip).subnets()
    print(list(test))
    '''

    iface = "eno1"
    #print(struct.pack("256s", iface.encode()))
    socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', iface.encode()))[20:24])

#!/usr/bin/env python3

import re
import binascii
import socket
import struct
import fcntl

def createPacket():
    pass

if __name__ =="__main__":
    iface = "eth0@if25"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = socket.inet_ntoa(fcntl.ioctl(
        sock.fileno(),
        0x8915,
        struct.pack("256s", iface)
    )[20:24])
    print(ip)

    '''
    ip = socket.gethostbyname(socket.gethostname())
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.bind(())
    '''

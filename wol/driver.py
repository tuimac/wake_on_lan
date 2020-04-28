#!/usr/bin/env python3

from icmp import Icmp

if __name__ =="__main__":
    ip = "localhost"
    icmp = Icmp()
    icmp.echoRequest(ip, 10)

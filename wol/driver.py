#!/usr/bin/env python3

from icmp import Icmp

if __name__ =="__main__":
    ip = "10.0.222.6"
    icmp = Icmp()
    icmp.echoRequest(ip, 10)

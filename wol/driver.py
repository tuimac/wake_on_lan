#!/usr/bin/env python3

from icmp import Icmp

if __name__ =="__main__":
    ip = "node7"
    icmp = Icmp()
    icmp.echoRequest(ip, 1)

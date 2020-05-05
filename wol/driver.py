#!/usr/bin/env python3

from icmp import IcmpClient

if __name__ =="__main__":
    icmp = IcmpClient()
    icmp.sendEchoRequest("10.0.222.4", 10)

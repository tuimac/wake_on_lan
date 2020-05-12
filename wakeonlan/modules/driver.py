#!/usr/bin/env python3

from icmp import IcmpClient

if __name__ =="__main__":
    icmp = IcmpClient()
    icmp.sendEchoRequest("node-win", times=10)

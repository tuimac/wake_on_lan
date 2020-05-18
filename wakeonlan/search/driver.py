#!/usr/bin/env python3

from arpscan import ArpScan

if __name__ == "__main__":
    iprange = "10.0.222.4/24"
    ArpScan.scan(iprange, "eth0@if13")

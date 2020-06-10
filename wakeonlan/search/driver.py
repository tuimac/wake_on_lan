#!/usr/bin/env python3

from arp import Arp

if __name__ == "__main__":
    iprange = "10.0.222.4/24"
    arp = Arp()
    arp.scan(iprange)

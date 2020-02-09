#!/usr/bin/env python3

from magicPacket import MagicPacket

def main():
    macAddress = "24:b6:fd:fd:fe:28"
    mp = MagicPacket(macAddress)
    mp.sendPacket()
    #print(mp.sendPacket())

if __name__ == '__main__':
    main()

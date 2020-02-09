#!/usr/bin/env python3

from magicPacket import MagicPacket

def main():
    macAddress = "12:AB:34:CD:56:EF"
    mp = MagicPacket(macAddress)
    mp.sendPacket()
    #print(mp.sendPacket())

if __name__ == '__main__':
    main()

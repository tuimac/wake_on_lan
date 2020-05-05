#!/usr/bin/env python3

def checksum(packet) -> int:
    try:
        sumBytes = 0
        checksum = 0
        for i in range(0, len(packet), 2):
            a = packet[i]
            if len(packet) == i + 2:
                b = 0
            else:
                b = packet[i]
            sumBytes += ((a << 8) + b)
        if sumBytes > 65535:
            checksum = 65535 ^ ((sumBytes >> 16) << 16)
        else:
            checksum = 65535 ^ sumBytes
        return checksum
    except Exception as e:
        raise e

def test(test):
    test = test - ((test >> 2) << 2)
    print(test)

if __name__ == "__main__":
    #checksum()
    test(13)

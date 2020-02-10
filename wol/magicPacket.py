import socket
import re
import struct

class MagicPacket:
    def __init__(self, macAddress):
        self.mac = macAddress

    def __createPacket(self):
        macAddress = self.mac.replace(":", "").replace("-", "").lower()
        print(macAddress)
        hexTable = {
             "0": 0, "1": 1,
             "2": 2, "3": 3,
             "4": 4, "5": 5,
             "6": 6, "7": 7,
             "8": 8, "9": 9,
             "a": 10, "b": 11,
             "c": 12, "d": 13,
             "e": 14, "f": 15,
        }
        header = b"\xff\xff\xff\xff\xff\xff"
        data = bytearray()
        for i in range(0, len(macAddress), 2):
            #print(macAddress[i] + macAddress[i + 1])
            data.append(hexTable[macAddress[i]] * 16 + hexTable[macAddress[i + 1]])
        print(data)
        data = bytes(data)
        data = header + b"".join(data for i in range(16))
        print(data)
        return data

    def sendPacket(self):
        #ip = socket.gethostbyname("node7")
        port = 9999

        data = self.__createPacket()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(data,("10.0.222.255", port))

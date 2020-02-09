import socket
import re

class MagicPacket:
    def __init__(self, mac):
        self.mac = mac

    def __createPacket(self):
        mac = self.mac.replace(":", "").replace("-", "").lower()
        data = b"\xff"

        byteMap = {
             "0": b"\x00", "1": b"\x01",
             "2": b"\x02", "3": b"\x03",
             "4": b"\x04", "5": b"\x05",
             "6": b"\x06", "7": b"\x07",
             "8": b"\x08", "9": b"\x09",
             "a": b"\x0a", "b": b"\x0b",
             "c": b"\x0c", "d": b"\x0d",
             "e": b"\x0e", "f": b"\x0f",
        }

        for byte in mac:
            data += byteMap[byte]
        print(data)
        return data


    def sendPacket(self):
        ip = "10.0.240.3"
        port = 9999

        data = self.__createPacket()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, (ip, port))

import socket
import struct
import random
import threading 
from queue import Queue
import traceback

class Icmp:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    def checksum(self, data):
        return 0

    def createPacket(self, sequence):
        type = 8
        code = 0
        checksum = 0
        identifier = random.randint(0, 65355)

        header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
        data = b"\xff" * size
        packet = header + data
        checksum = self.__checksum(header + packet)
        header = struct.pack("bbHHh", type, code, checksum, identifier, sequence)
        packet = header + data
        return packet

    def receiver(self, queue, sourceIp):
        self.sock.bind((sourceIp, 60000))
        while stop == False:
            packet = self.sock.recvfrom(1024)
            queue.put(packet)

    def echoRequest(self, destIp, times, size=64):
        destIp = socket.gethostbyname(destIp)
        sourceIp = socket.gethostbyname(socket.getfqdn())
        stop = False

        print(sourceIp)
        print(destIp)

        try:
            queue = Queue()
            recv = threading.Thread(target=receiver, name="receiver",args=(queue, sourceIp))
            recv.start()

            for i in range(1, times + 1):
                dataSize = self.sock.sendto(__createPacket(i), (destIp, 0))
                packet = queue.get()
                print(packet)
            stop = True
            recv.join()
            sendPacket(__createPacket(1), destIp, 1)
        except:
            traceback.print_exc() 

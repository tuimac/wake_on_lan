import socket
import struct
import random
import threading 
from queue import Queue
import traceback

class Icmp:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        self.stop = False

    def __checksum(self, data):
        print(data)
        return 0

    def createPacket(self, sequence, size):
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
        while self.stop == False:
            packet = self.sock.recvfrom(1024)
            queue.put(packet)

    def echoRequest(self, destIp, times, size=64):
        destIp = socket.gethostbyname(destIp)
        sourceIp = socket.gethostbyname(socket.getfqdn())
        print(sourceIp)
        print(destIp)
        try:
            queue = Queue()
            recv = threading.Thread(target=self.receiver, args=(queue, sourceIp))
            recv.start()

            for i in range(1, times + 1):
                dataSize = self.sock.sendto(self.createPacket(i, size), (destIp, 0))
                packet = queue.get()
                print(packet)
            self.stop = True
            recv.join()
        except:
            traceback.print_exc()
            self.stop = True

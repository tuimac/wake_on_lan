import socket
import time
from threading import Thread
from queue import Queue

class Endpoint(Thread):
    def __init__(self, inIp, inPort, protocol):
        Thread.__init__(self)
        self.__inboundQueue = Queue()
        self.__outboundQueue = Queue()
        self.__inIp = inIp
        self.__inPort = inPort
        self.__protocol = protocol

    def run(self):
        try:
            sock = {
                "icmp": lambda: socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP),
                "udp": lambda: socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            }[self.__protocol]()
            self.inbound = InboundEndpoint(self.__inboundQueue, self.__inIp, self.__inPort, self.__sock)
            self.inbound.daemon = True
            self.inbound.start()
            self.outbound = OutboundEndpoint(self.__outboundQueue, self.__sock)
            self.outbound.daemon = True
            self.outbound.start()
            self.inbound.join()
            self.outbound.join()
        except Exception as e:
            raise e

    def getInboundQueue(self):
        return self.inboundQueue

    def getOutBoundQueue(self):
        return self.outboundQueue

    def deleteAllSockets(self):
        try:
            self.inbound.deleteSocket()
            self.outbound.deleteSocket()
        except Exception as e:
            raise e

class InboundEndpoint(Thread):
    def __init__(self, queue, ip, port, socket):
        Thread.__init__(self)
        self.__queue = queue
        self.__ip = ip
        self.__port = port
        self.__socket = socket
        self.__delete = False
        self.__buffer = 512

    def run(self):
        try:
            self.__socket.bind((self.__ip, self.__port))
            while not self__.delete:
                data = self.__socket.recvfrom(self.__buffer)
                self.__queue.put(data)
        except KeyboardInterrupt:
            deleteSocket()
        except Exception as e:
            raise e
        
    def deleteSocket(self):
        try:
            self.__delete = True
            self.__queue.put("delete")
            time.sleep(1)
            self.__socket.close()
        except Exception as e:
            raise e

class OutboundEndpoint(Thread):
    def __init__(self, queue, socket):
        Thread.__init__(self)
        self.__queue = queue
        self.__socket = socket
        self.__delete = False

    def run(self):
        try:
            while not self.__delete:
                message = self.__queue.get()
                if message == "": continue
                self.__socket.sendto(message[0], message[1])
        except KeyboardInterrupt:
            deleteSocket()
        except Exception as e:
            raise e

    def deleteSocket(self):
        try:
            self.__delete = True
            self.__queue.put("delete")
            time.sleep(1)
            self.__socket.close()
        except Exception as e:
            raise e

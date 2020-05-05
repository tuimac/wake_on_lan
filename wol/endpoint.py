import socket
import time
from threading import Thread
from queue import Queue

class Endpoint():
    def __init__(self, inIp, inPort, protocol):
        self.__inIp = inIp
        self.__inPort = inPort
        self.__protocol = protocol
        self.__inboundQueue = Queue()
        self.__outboundQueue = Queue()
        try:
            sock = {
                "icmp": lambda: socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP),
                "udp": lambda: socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            }[self.__protocol]()
            self.__inbound = InboundEndpoint(self.__inboundQueue, self.__inIp, self.__inPort, sock)
            self.__inbound.daemon = True
            self.__inbound.start()
            self.__outbound = OutboundEndpoint(self.__outboundQueue, sock)
            self.__outbound.daemon = True
            self.__outbound.start()
            self.__inbound.join()
            self.__outbound.join()
            sock.close()
        except KeyboardInterrupt:
            self.closeAllEndpoints()
        except Exception as e:
            raise e

    def getInboundQueue(self):
        return self.__inboundQueue

    def getOutboundQueue(self):
        return self.__outboundQueue

    def closeAllEndpoints(self):
        try:
            self.__inbound.closeEndpoint()
            self.__outbound.closeEndpoint()
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
            while not self.__delete:
                data = self.__socket.recvfrom(self.__buffer)
                self.__queue.put(data)
        except KeyboardInterrupt:
            self.closeEndpoint()
        except Exception as e:
            raise e
        
    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__queue.put((b"", ("0.0.0.0", 0)))
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
                packet = self.__queue.get()
                self.__socket.sendto(packet[0], packet[1])
        except KeyboardInterrupt:
            self.closeEndpoint()
        except Exception as e:
            raise e

    def closeEndpoint(self):
        try:
            self.__delete = True
            self.__queue.put((b"", ("0.0.0.0", 0)))
        except Exception as e:
            raise e

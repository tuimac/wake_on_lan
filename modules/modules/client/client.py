#!/usr/bin/env python3

import socket
import threading
from queue import Queue
import time

DELETE = False
queue = Queue()

def receive():
    ip = socket.gethostbyname(socket.gethostname())
    port = 9999
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    while DELETE != True:
        data = sock.recvfrom(4096)
        queue.put(data)
        time.sleep(0.5)

def printBinary(data):
    print(data)

def main():
    try:
        threading.Thread(target=receive, name='receive')
        while DELETE != True:
            data = queue.get()
            printBinary(data)
    except:
        DELETE = True

if __name__ == '__main__':
    main()

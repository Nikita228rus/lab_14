import json
import socket

from sha import *
from threading import Thread

from datetime import datetime


name = 'Bob'
client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 5000))


def sender():
    while True:
        message = input('Your message: ')
        client_socket.send(message.encode("utf-8"))


def receiver():
    while True:
        package = (client_socket.recv(1024))
        print(package)


'''tread1 = Thread(target=sender)
tread2 = Thread(target=receiver)
tread1.start()
tread2.start()
'''
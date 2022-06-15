import json
import random
import socket
from threading import Thread
from datetime import datetime
from sha import *


name = 'Alica'
client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 5000))
password = input('Input password:\t')
n = 8
hash_list = []
for i in range(n):
    if i == 0:
        hash_list.append(sha_256(password))
    else:
        hash_list.append(sha_256(hash_list[i-1]))

first_message = str([name, 1, hash_list[-1]]).encode()
client_socket.send(first_message)
print(client_socket.recv(1024).decode())

i = n - 2
number = 1
while i != 0:
    client_socket.send(str([name, number + 1, hash_list[i]]).encode())
    print(client_socket.recv(1024).decode())
    i -= 1

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
tread2.start()'''
import socket
from sha import *
from threading import Thread  # Подключили класс потока


new_socket = socket.socket()  # Создаём объект сокета
new_socket.bind(('127.0.0.1', 5000))  # Привязываем наш объект к ip и порту
new_socket.listen(2)  # Указываем нашему сокету, что он будет слушать 2 других

print("Server is up now!")

conn1, add1 = new_socket.accept()
# сохраняем объект сокета нашего клиента и его адрес
print("First client is connected!")

def one_send_recv():

    hash_list_user = []
    while True:

        message = eval(conn1.recv(1024))
        if message[1] == 1:
            hash_list_user.append(message)
            conn1.send('Your save in systems'.encode())

        elif message[1] != 1:
            check_hash = sha_256(message[2])
            if check_hash == hash_list_user[0][2]:
                hash_list_user[0] = message
                conn1.send(f'User {message[0]} идентифицирован!'.encode())

            else:
                conn1.send('В доступе отказано!'.encode())



tread3 = Thread(target=one_send_recv)
tread3.start()


conn2, add2 = new_socket.accept()
# аналогично со вторым клиентом
print("Second client is connected!")


def acceptor1():

    while True:

        a = conn1.recv(1024)

        conn2.send(a)


def acceptor2():

    while True:
        b = conn2.recv(1024)

        conn1.send(b)

'''
tread1 = Thread(target=acceptor1)
tread2 = Thread(target=acceptor2)

tread1.start()
tread2.start()'''


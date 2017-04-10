#!/usr/bin/env python3
import socket
import threading


class Server:
    server_addr = "127.0.0.1", 50002
    sock = socket.socket()

    def __init__(self, server_addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_addr = self.server_addr if not server_addr else server_addr

    def start(self):
        self.sock.bind(self.server_addr)
        self.sock.listen(2)

    def connect(self, conn, addr):
        print('connect', addr)

        while True:
            data = conn.recv(1024)

            if not data:
                continue

            print(data.decode('utf-8'))

    def add_client(self):
        conn, addr = self.sock.accept()
        t = threading.Thread(target=self.connect, args=(conn, addr))
        t.start()

if __name__ == '__main__':
    s = Server(("127.0.0.1", 50002))
    s.start()
    while True:
        s.add_client()

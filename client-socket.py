import socket

HOST = '127.0.0.1'
PORT = 50002
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        try:
            message = input('Your message: ')
            s.sendall(message.encode('utf-8'))
        except KeyboardInterrupt:
            s.close()
            exit()

import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

msg = sk.recv(1024)
print(msg)
# sk.send(b'byebye')
sk.send(b'HTTP/1.1 200 OK\r\n\r\nHello World')

sk.close()
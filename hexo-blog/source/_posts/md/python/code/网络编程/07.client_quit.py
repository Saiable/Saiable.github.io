import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 9000))
while True:
    inp = input('>>>')
    sk.send(inp.encode('utf-8'))
    if inp.upper() == 'Q': break

    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q': break
    print(msg)

sk.close()
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

print('*' * 20)
conn, addr = sk.accept()

while True:
    msg = conn.recv(1024).decode('utf-8')
    if msg.upper() == 'Q': break
    print(msg)

    inp = input('>>>')
    conn.send(inp.encode('utf-8'))
    if inp.upper() == 'Q': break

conn.close()
sk.close()
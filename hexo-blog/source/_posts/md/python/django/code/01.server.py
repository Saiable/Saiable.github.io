import socket

sock = socket.socket()
sock.bind(('127.0.0.1',9090))
sock.listen(5)

while 1:
    print('server waiting...')
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data:',data)

    with open('post_test.html','rb') as fr:
        response = fr.read()
    # 响应首行和响应体之间，用\r\n\r\n隔开
    # conn.send(('HTTP/1.1 200 OK\r\n\r\n%s'%response).encode('utf-8'))
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n%s'%response)


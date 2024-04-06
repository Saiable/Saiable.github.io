import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
    inp = input('>>>').encode('utf-8')
    sk.sendto(inp, ('127.0.0.1', 9001))
    # recvfrom也可以，因为已经确定了ip和端口
    ret = sk.recv(1024)
    print(ret)

    # msg,server_addr = sk.recvfrom(1024)
    # print(msg.decode('utf-8'))
sk.close()

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.01', 9001))

while True:
    # ret = sk.recvfrom(1024)
    # ret是一个元组，是client发过来的msg和addr
    # 使用recvfrom是因为不确定谁会给我发消息
    # print(ret)

    msg, client_addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))

    msg = input('>>>').encode('utf-8')
    sk.sendto(msg, client_addr)

sk.close()
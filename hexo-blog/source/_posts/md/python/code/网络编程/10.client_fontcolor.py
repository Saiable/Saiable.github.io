import socket
import json

sk = socket.socket()

id = '12345'
sk.connect(('127.0.0.1', 9000))
while True:
    inp = input('>>>')
    name = 'alex'
    # dic = {'msg':inp, 'name':name}
    dic = {'msg':inp,'id':id}
    str_dict = json.dumps(dic)
    # sk.send('|'.join([name,inp]).encode('utf-8'))
    sk.send(str_dict.encode('utf-8'))
    if inp.upper() == 'Q':
        print('你已经断开和server的聊天！')
        break
    msg = sk.recv(1024).decode('utf-8')

    if msg.upper() == 'Q': break

    print(msg)
sk.close()
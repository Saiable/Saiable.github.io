import socket
import json

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

color_dict = {
    # 绿色
    '12345': {'color':'\033[31m','name':'alex'},
    '12346': {'color': '\033[33m', 'name': 'sia'},

}

print('*' * 20)


def chat(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        dic_msg = json.loads(msg)
        uid = dic_msg['id']
        # name,msg = msg.split('|')
        # print('%s: %s'%(name,msg))
        # print('%s: %s'%(dic_msg['name'],dic_msg['msg']))

        if dic_msg['msg'].upper() == 'Q':
            print('%s已经下线'%color_dict[uid]['name'])
            break
        print('%s%s: %s\033[0m'%(color_dict[uid]['color'],color_dict[uid]['name'],dic_msg['msg']))

        inp = input('>>>')
        conn.send(inp.encode('utf-8'))
        if inp.upper() == 'Q':
            print('你已经断开和%s的聊天！'%color_dict[uid]['name'])
            break
    conn.close()


while True:
    conn, addr = sk.accept()
    chat(conn)
sk.close()
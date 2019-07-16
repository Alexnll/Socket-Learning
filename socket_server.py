# socket server
import socket
import sys
import threading

HOST = socket.gethostname()
PORT = 12345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket object created.\n')

except socket.error:
    print('Failed to create socket.\n')
    sys.exit()

# 绑定socket到特定地址和端口
try:
    s.bind((HOST, PORT))
    print('successfully bind ' + HOST + ' with ' + str(PORT) + '.\n')
except socket.error:
    print('bind failed.\n')
    sys.exit()

# 连接侦听并接受连接
s.listen(10) # 最大可有10个连接在等待处理
print('socket now listening.\n')

while True:
    conn, addr =s.accept()
    print('链接地址', str(addr))
    message = '欢迎访问本地服务器!\n'
    conn.send(message.encode())
    conn.close()


'''
def clientthread(conn):
    conn.send('Welcome to the server. Type something and hit enter\n')
    
    while True:
        # 发送数据给客户端
        data = conn.recv(1024)
        print(data, '\n')
        reply = 'OK...' + data
        if not data:
            break
        
        conn.sendall(reply)
    conn.close()

# 保持与客户机的通信
while True: 
    # 阻塞
    conn, addr = s.accept()
    print('Connect with ' + addr[0] + ' : ' + str(addr[1]))

    threading._start_new_thread(clientthread, (conn, ))
'''

# Socket client connecting
import socket
import sys

# 创建socket对象
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket object created.\n')

except socket.error:
    print('Failed to create socket.\n')
    sys.exit()

# 连接到远端服务器
# 获取远端服务器IP地址
host =  socket.gethostname()
try:
    remote_ip = socket.gethostbyname(host)
    print('IP address of ' + host + ' is ' + remote_ip + '\n')

except socket.gaierror:
    print('Hostname could not be resolved. Exiting.\n')
    sys.exit()

# 指定要连接的接口
port = 12345
s.connect((remote_ip, port))
print('socket connected to ' + host + ' on ip ' + remote_ip + '\n')

'''
# 向远端服务器发送数据
message = "GET / HTTP/1.1\r\n\r\n"
try:
    s.sendall(message.encode())
    print('message sended successfully.\n')

except socket.error:
    print('Send failed.\n')
    sys.exit()
'''

# 接收数据
reply = s.recv(1024)
print(reply.decode())

# 关闭
s.close()
import socket

ipAddress = ""
port = 5050;

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((ipAddress, port))

while True :
    # msg = (mySocket.recv(1024).decode('utf-8'))
    # print(msg, end='')
    msg = input() + '\n'
    mySocket.send(msg.encode())

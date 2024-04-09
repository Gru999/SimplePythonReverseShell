import socket, os, sys

#Setup
s = socket.socket()
port = 9999
s.bind(('', port))
s.listen(5)

while True:
    #Establish connection with client
    c, addr = s.accept()
    print('Connection from', addr)

    while True:
        command = input('Enter a command: ')
        
        if command == "quit":
            c.close()
            break
        
        c.send(command.encode())
        output = c.recv(1024).decode()
        print(output)
        sys.stdout.flush()

    c.close()
# Citation for the whole file:
# Date: 6/28/2022
# Adapted from:
# TCPServer.py in [Kurose, Ross 2022]
from socket import * 

host = 'localhost'
port = 65517

with socket(AF_INET, SOCK_STREAM) as s: # set up the socket
    # get the socket listening with the right options
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((host, port)) 
    s.listen(1)
    print('Server listening on:', host, 'on port:', port)

    # this is so we can print a message only after the first message
    first_msg = True

    # accept the connection
    conn, addr = s.accept()
    print('Connected by (\'' + addr[0] + '\', ' + str(addr[1]) + ')')
    print('Waiting for message...')

    # message loop
    while True:
        data = conn.recv(2048).decode()

        # break if the quit sequence is sent so we can close the connection
        if data == '/q':
            break

        print(data)

        # print instructions only after the first message
        if first_msg:
            print('Type /q to quit')
            print('Enter message to send...')
            first_msg = False

        # prompt for a message and send it
        msg = input('>')
        conn.send(msg.encode())

        # if we asked the client to quit, we should also quit
        if msg == '/q':
            break

    conn.close()
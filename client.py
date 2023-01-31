# Citation for the whole file:
# Date: 6/28/2022
# Adapted from:
# TCPClient.py in [Kurose, Ross 2022]
from socket import *

host = 'localhost'
port = 65517

with socket(AF_INET, SOCK_STREAM) as s: # set up the socket

    # connect and print instructions
    s.connect((host, port))
    print('Connected to:', host, 'on port:', port)
    print('type /q to quit')
    print('Enter message to send...')

    while True:
        # prompt for and send message
        msg = input('>')
        s.send(msg.encode())

        # if we asked the server to quit, we should also quit
        if msg == '/q':
            break

        # receive response
        response = s.recv(2048).decode()

        # break if the quit sequence is sent so we can close the connection
        if response == '/q':
            break

        # print response
        print(response)
    
    s.close()
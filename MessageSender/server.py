from socket import *

if __name__ == '__main__':
    serverPort = 12000

    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    while 1:
        message, clientAddress = serverSocket.recvfrom(1024)
        msgModified = message.upper()
        serverSocket.sendto(msgModified, clientAddress)
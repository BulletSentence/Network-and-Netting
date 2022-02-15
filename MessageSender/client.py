from socket import *

if __name__ == '__main__':
    serverPort = 12000
    serverName = 'localhost'

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('Mensagem: ')
    clientSocket.sendto(str.encode(message), (serverName, serverPort))
    msg, serverAddress = clientSocket.recvfrom(1024)
    print(msg)
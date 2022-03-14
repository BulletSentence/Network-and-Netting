import socket

if __name__ == '__main__':
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.0.123"
    port = 4040
    serverSocket.bind((host, port))
    serverSocket.listen(2)

    while True:
        clientSocket, address = serverSocket.accept()
        print("Connection Establish " + str(address))
        message = "200 OK" + "\r\n"
        encodedMessage = bytes(message, 'utf-8')
        clientSocket.send(encodedMessage)
        clientSocket.close()
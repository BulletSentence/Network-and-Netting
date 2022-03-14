import socket

if __name__ == '__main__':
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.0.123"
    port = 4040

    clientSocket.connect((host, port))
    message = clientSocket.recv(1024)
    clientSocket.close()
    print(message.decode('utf-8'))
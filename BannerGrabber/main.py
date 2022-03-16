import socket


def banner(ip_addr, addr_port):
    skt = socket.socket()
    skt.connect((ip_addr, int(addr_port)))
    skt.settimeout(5)
    print(str(skt.recv(1024)).strip('b'))


if __name__ == '__main__':
    ip = input("Target IP: ")
    port = str(input("Target Port: "))
    banner(ip, port)

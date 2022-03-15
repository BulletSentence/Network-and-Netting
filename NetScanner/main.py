import nmap

if __name__ == '__main__':
    scanner = nmap.PortScanner()
    print("** NMAP NetRunner **")

    ip_addr = input("Target IP: ")
    print("Targeted: ", ip_addr)

    response = input("""\n Type of Scan:
    1) SYN ACK Scan
    2) UDP Scan
    3) Comprehensive Scan
    """)
    print("Type: ", response)

    if response == '1':
        print("NMap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

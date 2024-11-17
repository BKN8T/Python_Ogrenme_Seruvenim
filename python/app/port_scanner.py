import socket
import ipaddress

def get_target_info():
    while True: 
        try:
            target_ip = input("Hedef IP adresinini giriniz: ")
            ipaddress.ip_address(target_ip)
            break
        except ValueError:
            print("Geçersiz IP adresi. Lütfen doğru bir IP giriniz.")
    while True:
        try:
            port_range = input ("Port aralığını giriniz(örn: 1-1000): ")
            start_port , end_port = map(int, port_range.split("-"))
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                raise ValueError
            break
        except ValueError:
            print("Geçersiz port aralığı. Tekrar deneyin.")
    return target_ip , start_port, end_port


def scan_ports(target_ip, start_port,end_port):
    print(f"\n{target_ip} aresinde {start_port}-{end_port} aralığındaki portlar taranıyor...\n")

    open_ports = []

    for port in range(start_port,end_port+1):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip,port))

            if result ==0:
                open_ports.append(port)
                print(f"Port {port} AÇIK")
            else:
                print(f"Port {port} KAPALI")
    return open_ports

def display_result(open_ports):
    if open_ports:
        print(f"\nAçık Portlar:")
        for port in open_ports:
            print(f"- Port {port}")
    else:
        print("\nHiçbir açık port BULUNAMADI.")

if __name__ == "__main__":
    print("KN8T P0rt Scanner'a Hoş Geldiniz!")
    target_ip, start_port, end_port = get_target_info()
    open_ports = scan_ports(target_ip, start_port,end_port)
    display_result(open_ports)


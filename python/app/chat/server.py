import socket
import threading

def log_disconnection(client_address):
    with open("server_log.txt", "a") as log_file:
        log_file.write(f"{client_address} bağlantıyı kapattı.\n")

def handle_client(client_socket, client_address):
    print(f"Yeni bağlantı: {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:  # Eğer veri yoksa bağlantı kapatılıyor
                print(f"{client_address} bağlantıyı kapattı.")
                log_disconnection(client_address)  # Bağlantı kesildiğinde log tut
                break
            message = data.decode()
            print(f"{client_address} mesajı: {message}")
            response = input("Mesaj: ")
            client_socket.send(response.encode())
        except (ConnectionResetError, OSError) as e:
            print(f"{client_address} bağlantı hatası: {e}")
            log_disconnection(client_address)  # Hata durumunda da log kaydı yapılmalı
            break
    client_socket.close()
    print(f"{client_address} için bağlantı kapatıldı.")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"  # Yerel ağda çalıştırmak için 127.0.0.1
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Sunucu {host}:{port} adresinde çalışıyor ve istemcileri bekliyor...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
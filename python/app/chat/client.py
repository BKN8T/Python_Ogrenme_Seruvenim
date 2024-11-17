import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print("Sunucu bağlantıyı kesti.")
                break
            print(f"Sunucudan gelen: {message}")
        except:
            print("Bağlantı kesildi.")
            break
    client_socket.close()

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    client_socket.connect((host, port))
    print(f"{host}:{port} adresine bağlanıldı.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Mesaj yaz: ")
        if message.lower() == "exit":
            client_socket.send(message.encode())
            print("Bağlantı kapatılıyor...")
            client_socket.close()
            break
        client_socket.send(message.encode())

if __name__ == "__main__":
    main()
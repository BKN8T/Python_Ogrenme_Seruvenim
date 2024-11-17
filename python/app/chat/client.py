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
    host = "127.0.0.1"  # Burayı dış ağda çalıştırmak için harici IP'ye çevirebilirsin.
    port = 12345
    
    try:
        client_socket.connect((host, port))
        print(f"{host}:{port} adresine bağlanıldı.")
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Mesaj yaz: ")
        if message.lower() == "exit":
            client_socket.send(message.encode())  # "exit" mesajını sunucuya gönder
            print("Bağlantı kapatılıyor...")
            client_socket.close()  # Bağlantıyı kapat
            break  # Döngüyü sonlandır
        else:
            client_socket.send(message.encode())  # Normal mesajları gönder

if __name__ == "__main__":
    main()
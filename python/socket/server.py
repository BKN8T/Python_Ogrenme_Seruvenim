import socket

host = "127.0.0.1"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

s.listen()
print(f"Sunucu {host}:{port} adresinde çalışıyor...")


conn , addr = s.accept()
print(f"Bağlantı kuruldu: {addr}")

if conn: 
    while True:
        ldata = conn.recv(1024)
        if ldata.decode("utf-8") == "exit":
            print("Bağlantı kapatılıyor...")
            conn.close()

        else: 
            print(ldata.decode("utf-8"))


        data = input("Message: ")
        if data.encode("utf-8") == "exit":
            print("Bağlantı kapatılıyor...")
            conn.close()
        else :
            conn.sendall(data.encode("utf-8"))





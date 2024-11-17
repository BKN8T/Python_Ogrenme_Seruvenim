import socket

cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "127.0.0.1"
port = 8080

cs.connect((host,port))
print(f"{host}:{port} adresine bağlanıldı.")
()
while True:
    message = input("Message: ")
    cs.send(message.encode())

    if message.lower() == "exit": 
        print("Bağlantı Kapatılıyor... ")
        cs.close()
        break
    response = cs.recv(1024).decode()
    print(f"Sunucudan gelen: {response}")

import socket

host = "35.202.25.143"
port = 12345

sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sunucu.bind((host, port))
sunucu.listen(5)

while True:
    clientsocket , addr = sunucu.accept()
    print(f'Bağlantı sağlandı {addr}')
    clientsocket.send(bytes("Sunucuya bağlandı", "utf-8"))

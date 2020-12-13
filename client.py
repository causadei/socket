import socket

host = "localhost"
port = 12345

sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sunucu.connect((host, port))
msg = sunucu.recv(1024)
print(msg.decode("utf-8"))

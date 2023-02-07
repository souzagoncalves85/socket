from socket import *

serverHost = "localhost"
serverPort = 50007

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((serverHost, serverPort))

message = input("Usuário do github: ")
sock.sendall(message.encode("utf-8"))

data = sock.recv(4096)
print("Repositórios de %s: %s"%(message, data.decode()))

sock.close()
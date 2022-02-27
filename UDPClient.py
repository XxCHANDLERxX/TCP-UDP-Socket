# Python UDPClient
from socket import *
serverName = 'ubuntu1604-002.student.cs.uwaterloo.ca'
serverPort = 13579
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close()

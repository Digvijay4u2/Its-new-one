import socket
serverName='192.168.43.20'
serverPort=9998
clientServer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientServer.connect((serverName,serverPort))
sentence=b'highleted'
clientServer.send(sentence)
modifiedSentence=clientServer.recv(1024)
print(modifiedSentence)
clientServer.close()

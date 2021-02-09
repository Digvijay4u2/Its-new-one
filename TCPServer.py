import socket
serverName='192.168.43.20'
ServerPort=9998
ServerSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ServerSocket.bind((serverName,ServerPort))
ServerSocket.listen(1)
print('Server is ready : ')
while True:
    connectionSocket,address=ServerSocket.accept()
    sentence=connectionSocket.recv(1024)
    capitalizeSentence=sentence.upper()
    connectionSocket.send(capitalizeSentence)
    print(capitalizeSentence)
    connectionSocket.close()




# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 06:02:35 2021

@author: digvijay
"""


import socket
Servername = '192.168.43.20'
ServerPort=9998
ClientSocket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message =input("enter something :")

ClientSocket.sendto(message.encode(),(Servername,ServerPort))
modifiedmessage,ServerAddress=ClientSocket.recvfrom(1024)
print (modifiedmessage.decode())
ClientSocket.close()
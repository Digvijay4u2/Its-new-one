# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 06:08:56 2021

@author: digvijay
"""


import socket
#ServerAddress='192.168.43.20'
ServerPort=9998
ServerSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ServerSocket.bind(('',ServerPort))
print ("Server is ready : ")
while 1:
    message,clientAddress=ServerSocket.recvfrom(1024)
    modifiedAddress=message.upper()
    print(message)

    ServerSocket.sendto(modifiedAddress,clientAddress)

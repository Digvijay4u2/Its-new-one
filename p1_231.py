# -*- coding: utf-8 -*-

"""
Created on Sat Jan 23 19:30:08 2021

@author: digvijay
"""
"""
message = ['Digvijay','Mrityunjay','Dhananjay','vijay']
print(message)
for name in message:
    print(name +" , "+ "hi".title()+"!  how are you")
    print("ok how it was\n")
print("This will run after the for loop")
mess="this is your message ."
print(mess)
for messag in range(1,4):
    print(message[messag])


list=list(range(3,6))
print(list)
print(min(list))
print(max(list))
print(sum(list))
for list in message:
    if list.lower()=='digvijay':
        print(list)
    else:
        print("Sorry it is not 4")
if 'Mrityunjay' in message:
    print("Oo  yes mrityunjay you are in the  list")
if "Dhaval" not in message:
    print("Dhaval you can join in the list")
message.insert(-2,"Dhaval")
print(message)

m=input("Please press some thing : ")
print(m)
"""
def fun(a,b):
    print(a + " "+ str(b))
    
fun(b=2,a="dig")
#building a webserver in python
import socket #built in python


mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #makeaphonecall
mysock.connect(('data.pr4e.org',80))  #dialthephonetoadomainnameandportnumber
cmd= 'GET http:// data.pr4e.org/page1.html HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode(),end='')

mysock.close()
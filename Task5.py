# Task 5 – Port State Checker
import socket

portsCheckList = [22, 23, 53, 80, 443]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for checkPort in portsCheckList:
    portStatus = sock.connect_ex(('127.0.0.1', checkPort))
    if portStatus == 0:
        print('Port {} is Open'.format(checkPort))
    else:
        print('Port {} is Closed'.format(checkPort))
sock.close()

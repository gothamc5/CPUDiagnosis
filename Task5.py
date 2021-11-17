# Task 5 – Port State Checker
import socket

portsCheckList = [22, 23, 53, 80, 443]
hostIP = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('----------------------------------------------------------------------------------')
print('Port State Report for Machine {}'.format(hostIP))
print('----------------------------------------------------------------------------------')
for checkPort in portsCheckList:
    portStatus = sock.connect_ex((hostIP, checkPort))
    if portStatus == 0:
        print('Port {} is Open'.format(checkPort))
    else:
        print('Port {} is Closed'.format(checkPort))
sock.close()
print('----------------------------------------------------------------------------------')

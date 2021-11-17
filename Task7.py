# Task 7 – Network Checker System
import socket
import requests

portsCheckList = [22, 23, 53, 80, 443]
hostIP = '127.0.0.1'
testUrlList = ['http://www.google.com', 'https://en.wikipedia.org/wiki/Main_Page']
responseTimesList = list()
status = 'NO Internet or Very Bad Network'


def average(listToAvg):
    return sum(listToAvg) / len(listToAvg)


def port_state_checker():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('----------------------------------------------------------------------------------')
    print('Running Port State Report for Machine {}'.format(hostIP))
    print('----------------------------------------------------------------------------------')
    for checkPort in portsCheckList:
        portStatus = sock.connect_ex((hostIP, checkPort))
        if portStatus == 0:
            print('Port {} is Open'.format(checkPort))
        else:
            print('Port {} is Closed'.format(checkPort))
    sock.close()
    print('----------------------------------------------------------------------------------')


def connection_status_checker():
    print('----------------------------------------------------------------------------------')
    print('Running Connection Status Checker on this computer')
    print('----------------------------------------------------------------------------------')
    for url in testUrlList:
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print('Connection Error while connecting website: {}'.format(url))
            continue
        except:
            print('Unknown Error while connecting website: {}'.format(url))
            continue
        responseTimesList.append(response.elapsed.total_seconds())
        print('{} secs elapsed to connect Website: {}'.format(response.elapsed.total_seconds(), url))
    if responseTimesList:
        avgResponseTime = average(responseTimesList)
        print('Average response time of all connected websites: {} secs'.format(avgResponseTime))
        if avgResponseTime <= 0.1:
            status = 'Very Good Speed'
        elif avgResponseTime <= 1.0:
            status = 'Moderate Speed'
        else:
            status = 'Bad Speed'
    print('Internet status of this computer: {}'.format(status))
    print('----------------------------------------------------------------------------------')


def exit_network_checker():
    print('----------------------------------------------------------------------------------')
    print('Thank you for Using Network Checker System. Bye.')
    print('----------------------------------------------------------------------------------')
    exit()


def invalid_option():
    print('-------------------------------')
    print('You have entered invalid option')
    print('-------------------------------')


def run_option(opt):
    switcher = {
        '0': exit_network_checker,
        '1': port_state_checker,
        '2': connection_status_checker
    }
    return switcher.get(opt, invalid_option)


print('----------------------------------------------------------------------------------')
print('Welcome to Network Checker System')
while True:
    print('Kindly chose an option below')
    print('-------------------------------')
    print('1 - Run Port State Checker')
    print('2 - Run Connection Status Checker')
    print('0 - Exit')
    print('-------------------------------')
    option = input('Enter your option:')
    func = run_option(option)
    func()

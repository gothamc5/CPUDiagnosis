# Task 2 – Intelligent CPU Monitor
import psutil
import time

historyUsage = list()
checkInterval = 5
historyDuration = 120
warningThreshold = 90


def average(l):
    return sum(l) / len(l)


x = historyDuration
while x > 0:
    historyUsage.append(psutil.cpu_percent())
    time.sleep(checkInterval)
    x -= checkInterval

while True:
    currentCpuUsage = psutil.cpu_percent()
    if currentCpuUsage > warningThreshold:
        print('Warning: CPU usage is High and above 90%')
    if currentCpuUsage > 2 * average(historyUsage):
        print('Warning: CPU usage is High than normal levels')
    historyUsage.pop(0)
    historyUsage.append(currentCpuUsage)
    time.sleep(checkInterval)

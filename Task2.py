# Part A - Task 2 : Intelligent CPU Monitor
import psutil
import time

cpuUsageHistory = list()
checkInterval = 5
historyDuration = 120
warningThreshold = 90


def average(listToAvg):
    return sum(listToAvg) / len(listToAvg)


x = historyDuration
while x > 0:
    cpuUsageHistory.append(psutil.cpu_percent(interval=checkInterval))
    x -= checkInterval

while True:
    currentCpuUsage = psutil.cpu_percent()
    if currentCpuUsage > warningThreshold:
        print('Warning: CPU usage is High and above 90%')
    if currentCpuUsage > 2 * average(cpuUsageHistory):
        print('Warning: CPU usage is High than normal levels')
    cpuUsageHistory.pop(0)
    cpuUsageHistory.append(currentCpuUsage)
    time.sleep(checkInterval)

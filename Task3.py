# Task 3 – CPU Problem Diagnoser

import psutil
import time

cpuUsageHistory = list()
processCountHistory = list()
problemRootCauseFound = False
checkInterval = 2
historyDuration = 10
warningThreshold = 90
cpuCount = psutil.cpu_count()
currentProcessCount = 0


def average(l):
    return sum(l) / len(l)


x = historyDuration
while x > 0:
    cpuUsageHistory.append(psutil.cpu_percent(interval=checkInterval))
    processCountHistory.append(len(psutil.pids()))
    x -= checkInterval

while True:
    for process in psutil.process_iter():
        cpu_usage = process.cpu_percent()
    time.sleep(checkInterval)
    currentCpuUsage = psutil.cpu_percent()
    if currentCpuUsage > warningThreshold or currentCpuUsage > 2 * average(cpuUsageHistory):
        print('Warning: CPU usage is High')
        for process in psutil.process_iter():
            pid = process.pid
            cpu_usage = process.cpu_percent()
            if pid == 0:
                continue
            try:
                coresUsed = len(process.cpu_affinity())
            except psutil.AccessDenied:
                coresUsed = 0
                continue
            if cpu_usage / cpuCount > currentCpuUsage / 2:
                print('Root Cause: One particular process is taking more than half of CPU usage')
                print(process.cpu_affinity())
                print('            ID        :' + str(pid))
                print('            Name      :' + str(process.name()))
                print('            Cores Used:' + str(coresUsed))
                print('            CPU Used  :' + str(cpu_usage / coresUsed))
                print('--------------------------------')
                problemRootCauseFound = True
        currentProcessCount = len(psutil.pids())
        if currentProcessCount > 2 * average(processCountHistory):
            print('Root Cause: There are lot of new process running than usual')
            print('            Average process count: {}'.format(average(processCountHistory)))
            print('            Current process count: {}'.format(currentProcessCount))
            problemRootCauseFound = True
        if not problemRootCauseFound:
            print('Root Cause: CPU Usage is High for unknown reason')
            problemRootCauseFound = False
    cpuUsageHistory.pop(0)
    cpuUsageHistory.append(currentCpuUsage)
    processCountHistory.pop(0)
    processCountHistory.append(len(psutil.pids()))
    print(cpuUsageHistory)
    print(processCountHistory)

# Task 3 – CPU Problem Diagnoser
import psutil
import time

cpuUsageHistory = list()
processCountHistory = list()
problemRootCauseFound = False
checkInterval = 5
historyDuration = 120
warningThreshold = 90
currentProcessCount = 0
currentCpuUsage = 0


def average(listToAvg):
    return sum(listToAvg) / len(listToAvg)


x = historyDuration
while x > 0:
    cpuUsageHistory.append(psutil.cpu_percent(interval=checkInterval))
    processCountHistory.append(len(psutil.pids()))
    x -= checkInterval

while True:
    for process in psutil.process_iter():
        processCpuUsage = process.cpu_percent()
    time.sleep(checkInterval)
    currentCpuUsage = psutil.cpu_percent()
    currentProcessCount = len(psutil.pids())
    if currentCpuUsage > warningThreshold or currentCpuUsage > 2 * average(cpuUsageHistory):
        print('Warning: CPU usage is High')
        for process in psutil.process_iter():
            pid = process.pid
            if pid == 0:
                continue
            try:
                coresUsed = len(process.cpu_affinity())
                processCpuUsage = process.cpu_percent() / coresUsed
            except psutil.AccessDenied:
                coresUsed = 0
                continue
            if processCpuUsage > currentCpuUsage / 2:
                print('Root Cause: One particular process is taking more than half of CPU usage')
                print('            ID        :' + str(pid))
                print('            Name      :' + str(process.name()))
                print('            Cores Used:' + str(coresUsed))
                print('            CPU Used  :' + str(processCpuUsage))
                print('            Process   :' + str(process))
                problemRootCauseFound = True
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
    processCountHistory.append(currentProcessCount)

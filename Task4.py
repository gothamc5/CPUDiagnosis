# Task 4 – Process-based CPU Problem Diagnoser
import time
import psutil

processHistoryUsage = dict()
processCurrentUsage = dict()
processWarningThreshold = 10
checkInterval = 300
cpuCores = psutil.cpu_count()

for process in psutil.process_iter():
    process.cpu_percent()
while True:
    for process in psutil.process_iter():
        if process.pid == 0:
            continue
        try:
            processCpuUsage = process.cpu_percent() / cpuCores
            processCurrentUsage[process.pid] = processCpuUsage
            if process.pid in processHistoryUsage.keys():
                if processHistoryUsage[process.pid] and processCpuUsage > processWarningThreshold * processHistoryUsage[process.pid]:
                    print('Warning: This process has increased its CPU usage by {} times in the past {} secs'.format(processWarningThreshold, checkInterval))
                    print('         ID             :' + str(process.pid))
                    print('         Name           :' + str(process.name()))
                    print('         Previous usage :' + str(processHistoryUsage[process.pid]))
                    print('         Current usage  :' + str(processCpuUsage))
        except psutil.AccessDenied:
            continue
    processHistoryUsage = processCurrentUsage.copy()
    processCurrentUsage.clear()
    time.sleep(checkInterval)

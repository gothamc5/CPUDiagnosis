# Task 1 – Basic CPU Monitor
import psutil
import time

checkInterval = 5
warningThreshold = 90
while True:
    if psutil.cpu_percent(interval=5) > warningThreshold:
        print('Warning: CPU usage is High')
    # time.sleep(checkInterval)

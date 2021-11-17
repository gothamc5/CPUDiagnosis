import time

import psutil

cpuCount = psutil.cpu_count()
print(psutil.cpu_percent())
# print(psutil.pids())
p = psutil.Process(6076)
# print(p)
while True:
    print('ID = {}  CPU = {}'.format(p.pid, p.cpu_percent()/cpuCount))
    time.sleep(1)

# for i in range(3):
#     for p in psutil.pids():
#         pd = psutil.Process(p)
#         print('ID = {}  CPU = {}'.format(pd.pid, pd.cpu_percent()))
#         time.sleep(1)
#         print('ID = {}  CPU = {}'.format(pd.pid, pd.cpu_percent()))

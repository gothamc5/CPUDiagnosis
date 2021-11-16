import time

import psutil

# print(psutil.cpu_percent())
# print(psutil.pids())
p = psutil.Process(6076)
# print(p)

while True:
    print(psutil.cpu_count())
    # print(p.num_fds())
    # print(p.cpu_num())
    print('ID = {}  CPU = {}'.format(p.pid, p.cpu_percent()/psutil.cpu_count()))
    time.sleep(1)

# for i in range(3):
#     for p in psutil.pids():
#         pd = psutil.Process(p)
#         print('ID = {}  CPU = {}'.format(pd.pid, pd.cpu_percent()))
#         time.sleep(1)
#         print('ID = {}  CPU = {}'.format(pd.pid, pd.cpu_percent()))

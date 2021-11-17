# Part B - Task 6 : Connection Status Checker
import requests

testUrlList = ['http://www.google.com', 'https://en.wikipedia.org/wiki/Main_Page']
responseTimesList = list()
status = 'NO Internet or Very Bad Network'


def average(listToAvg):
    return sum(listToAvg) / len(listToAvg)


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

import urllib3

https = urllib3.PoolManager()
url = 'http://google.com'

response = https.request('GET', url)

print(response.status)
print(response.data)
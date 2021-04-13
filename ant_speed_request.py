import requests

# Save speed to file

f = open('miner_speed.html','r')
message = f.read()
print(message)
#f.close()

content_list = f.readlines()
print(content_list)
f.close()
print(message)

if(message) > '201' :print 'running fast config'
else: print 'running slow config'

# get speed

username = "root"
password = "root"
api_url = "http://192.168.1.107/cgi-bin/minerAdvanced.cgi"

# import requests module
import requests
from requests.auth import HTTPDigestAuth

# Making a get request
url = 'http://192.168.1.107/cgi-bin/minerAdvanced.cgi/'

response = requests.get(url, auth=HTTPDigestAuth('root', 'root'))

page_info = response.content
#print page_info

#print(page_info[1689 : 1692])
txt = page_info
speed = txt.find("bitmain-freq")
print speed

# save to file
f = open('miner_speed.html', 'wb')
f.write(page_info[1689 : 1692]) # position of bitmain-speed
f.close


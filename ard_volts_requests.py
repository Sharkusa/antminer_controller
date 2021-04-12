
import json
import os
import time
import urllib2
import requests
import parse




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


#while True:
#     jsonobj = json.load(urllib2.urlopen(url))
#    battery_volts = jsonobj[0]['battery']
#     freq = jsonobj[0]['bitmain-freq']
#    voltage = jsonobj[0]['voltage']
#    print "Got Battery Voltage from API"
#     time.sleep(4)
 #   clear()
 #    print jsonobj
 #    print "freq"
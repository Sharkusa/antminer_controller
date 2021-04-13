#!/usr/bin/python

import json
import os
import time
import requests
import urllib2
import parse
import requests



api_url = "http://149.248.38.51/cgi-bin/getLastVolts.py"

MIN_VOLTS = 12.000000
AVG_VOLTS = 12.400000
MAX_VOLTS = 13.000000


POLLING_MINUTES = 1
poll_time = POLLING_MINUTES*5
clear = lambda: os.system('clear')
c = 0
config = 0
maxVolts = False
avgVolts = False
username = "root"
password = "root"
# api_url = "http://192.168.1.107/cgi-bin/minerAdvanced.cgi"

while True:
    jsonobj = json.load(urllib2.urlopen(api_url))
    battery_volts = jsonobj[0]['battery']
    amps = jsonobj[0]['amps']
    voltage = jsonobj[0]['voltage']
#       print "Got Battery Voltage from API"
    time.sleep(4)
    clear()
#       print jsonobj
    print "battery volts"
    print battery_volts
    print "charge amps"
    print amps
    print "solar panel voltage"
    print voltage
#       print jsonobj
    print "number of restarts"
    print (c)
    print config
# sleep for poll_time seconds
    time.sleep(poll_time)

# while battery_volts > AVG_VOLTS:
# while battery_volts > AVG_VOLTS:
    print "polling"
    if maxVolts:
        print "already running fast config nothing to do"
    else:
            if(float(battery_volts) > MAX_VOLTS):
                os.system('sshpass -p "admin" scp /home/ubuntu/cgminer_L32_Solar/cgminer.conf root@192.168.1.107:/config/')
                os.system('sshpass -p "admin" ssh root@192.168.1.107 /etc/init.d/cgminer.sh restart')
                config = "fastconfig"
                maxVolts = True
                print "Voltage above MAX setpoint, loading fast config"



    # get speed



    # import requests module

    from requests.auth import HTTPDigestAuth

    # Making a get request
    url = 'http://192.168.1.107/cgi-bin/minerAdvanced.cgi/'

    response = requests.get(url, auth=HTTPDigestAuth('root', 'root'))

    page_info = response.content
    # print page_info

    # print(page_info[1689 : 1692])
    txt = page_info
    speed = txt.find("bitmain-freq")
    print speed

    # save to file
    f = open('miner_speed.html', 'wb')
    f.write(page_info[1689: 1692])  # position of bitmain-speed
    f.close

    # Save speed to file

    f = open('miner_speed.html', 'r')
    message = f.read()
    print(message)
    # f.close()

    content_list = f.readlines()
    print(content_list)
    f.close()
    print(message)

    if (message) > '201':
        print 'running fast config'
    else:
        print 'running slow config'


    # Restart miner and load slow config if battery volts go below AVG_VOLTS
#       if avgVolts: False
#       print "already running slow config nothing to do"
    pass
    if(float(battery_volts) < AVG_VOLTS):
            print "load slow config"
            os.system('sshpass -p "admin" scp /home/ubuntu/cgminer_L32_Solar/slow/cgminer.conf root@192.168.1.107:/config/')
            os.system('sshpass -p "admin" ssh root@192.168.1.107 /etc/init.d/cgminer.sh restart')
            config = "slowconfig"
            print "Voltage below MIN setpoint, loading slow config"
            c = c + 1
            maxVolts = False
            time.sleep(30)
            if(float(battery_volts) <= MIN_VOLTS):
                print "Voltage below minimum"

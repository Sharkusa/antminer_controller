import requests
f = open('miner_speed.txt','r')
message = f.read()
print(message)
#f.close()

content_list = f.readlines()
print(content_list)
f.close()
print(message)

if(message) > '201' :print 'running fast config'
else: print 'running slow config'

#while message > 300:
#    print ("yes")
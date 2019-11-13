import os
import time
import re


current_time = time.time()
path = '/var/tmp'
mask = "^[0-3][0-9].[0-1][0-9].20[1-2][0-9]-[0-2][0-9]:[0-5][0-9]:[0-5][0-9]"
#datetime.datetime.now().strftime('%d.%m.%Y-%H:%M:%S')
#13.11.2019-01:18:01
os.chdir(path)
for file in os.listdir(os.getcwd()):
    if current_time - os.stat(file)[7]  > 60 * 15 and re.match(mask,file):
        #print(file)
        #print(os.stat(file)[7],  current_time, current_time - os.stat(file)[7],  60 * 15 )
        os.remove(file)
        

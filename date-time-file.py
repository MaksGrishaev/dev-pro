import datetime


time_str = datetime.datetime.now().strftime('%d.%m.%Y-%H:%M:%S')
with open('/var/tmp/' + time_str, 'w') as file:
    file.write("")
    

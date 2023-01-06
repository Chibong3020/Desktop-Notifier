from plyer import notification
import time


title = "Time to drink water"
message = "Stay hydrated"
while(True):
    notification.notify(title = title,message=message,app_icon = None,timeout = 10,toast = False)       
    time.sleep(60*30)
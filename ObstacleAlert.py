3 importing desired libraries
from boltiot import Bolt, Sms
import json, time

obstacle_limit =90

API_KEY = "02e5a88b-1226-420b-ab32-994863a3a59b"
DEVICE_ID  = "BOLT3848427"

# Credentials required to send SMS
SID = 'ACa6896b1ba825ab7a4277b54f655db8d3'
AUTH_TOKEN = '6f6ac88c31e1871f226df1d2cc77daa0'
FROM_NUMBER = '+12565008729'
TO_NUMBER = '+918075805684'




mybolt = Bolt(API_KEY, DEVICE_ID)
sms = Sms(SID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER) 
response = mybolt.serialRead('10')
print(response)

while True:
    response = mybolt.serialRead('10')  #Fetching the value from Arduino
    data = json.loads(response)
    obstacle_value = data['value'].rstrip()
    print("Obstacle Not detected", obstacle_value)
    if int(obstacle_value) < obstacle_limit:
        response = sms.send_sms('Alert, Obstacle Detected') # If the object distance is less than 90 it will send a sms to the desired person
        mybolt.digitalWrite('2', 'HIGH') The buzzer will activate #for 3sec
        time.sleep(3)
        mybolt.digitalWrite('2', 'LOW')
    time.sleep(3)
    
  
     


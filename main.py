from gpiozero import MotionSensor
from time import sleep
import datetime
import csv

pir = MotionSensor(pin = 12)

sleep(1)

print("Inititating motion detection")

def speed(t):
    l = 7
    return (l / t)
    
def motionDetect():
    pir.wait_for_no_motion()
    print('No motion data')
    crisp = []
    start = datetime.datetime.now()
    now = datetime.datetime.now()
    duration = datetime.timedelta(seconds = 10200) # 2 timer 50 min 
    
    while now < start + duration:
        pir.wait_for_motion()
        start_time = datetime.datetime.now()
        print('Motion detected at: \n' + str(start_time))
        
        print('-------------------------------------')
        
        pir.wait_for_no_motion()
        end_time = datetime.datetime.now()
        print('No motion detected at: \n' + str(end_time))
        
        print('-------------------------------------')
        
        print('Total time: \n' + str(end_time - start_time))
        
        print('-------------------------------------')
        
        t = (end_time - start_time).total_seconds()
        
        print("Total seconds: " + str(t))
        
        print('-------------------------------------')
        
        print("Speed = " + str(speed(t)) + " m/s")
        
        crisp.append(str(speed(t)))
        
        now = datetime.datetime.now()
        
    return crisp


data = motionDetect()
        
print(data) # Array af gennemsnitlige hastigheder

x = 0

for i in range(len(data)):
    x += float(data[i])


print("Middelværdi: " + str(x / len(data))) # Middelværdi af hastighederne

print('Færdig')

average = str(x / len(data))

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    writer.writerow(average)

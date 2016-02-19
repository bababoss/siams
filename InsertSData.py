# this python file use for insert sensor data in database

#import MyDB connection module
import MyDB
db = MyDB.DB()
import Rpi.GPIO as GPIO
import time

sensorPin1 = 18 #Broadcom pin 18
#pin setup:
GPIO.setmode(GPIO.BCM) #Broadcom pin numbering scheem
GPIO.setup(sensorPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # sensor pin set as input
user_id = 1023
data = [user_id]

try:
    while 1:
        if GPIO.input(sensorPin1):
            db.execute("INSERT INTO Zones (user_id,zone1) \
                  VALUES (%s, NOW() )", [data]);

            db.commit()
            print "Records created successfully";
            db.close()

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:

    GPIO.cleanup() # cleanup all GPIO
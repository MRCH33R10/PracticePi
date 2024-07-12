from gpiozero import Motor
import RPi.GPIO as GPIO
import time


print("Hello to this great and prosperous world and to all who inhabit it, ps this is editted")
print("editted from ipad")
ext = True
#GPIO22 Right:Forward
#GPIO23 Right:Backward
motorR = Motor(22, 23)
#GPIO27 Left:Forward
#GPIO24 Left:Backward
motorL = Motor(27, 24)

def ButtonPin_Callback(channel):
  ext = False
  
ButtonPin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(ButtonPin, GPIO.BOTH, Callback = ButtonPin_Callback, bouncetime = 50)

while ext == True:
  motorR.forward()
  time.sleep(1)
  motorR.forward(0.5)
  time.sleep(1)
  motorR.forward(0.1)
  time.sleep(1)
  motorR.backward()
  time.sleep(1)
  
  motorL.forward()
  time.sleep(1)
  motorL.forward(0.5)
  time.sleep(1)
  motorL.forward(0.1)
  time.sleep(1)
  motorL.backward()
  time.sleep(1)



#GPIO22 Right:Forward
#GPIO23 Right:Backward
#GPIO24 Right:Forward
#GPIO25 Right:Backward

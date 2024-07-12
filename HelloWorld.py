from gpiozero import Motor
from gpiozero import LED
from gpiozero import Button
import time


print("Hello to this great and prosperous world and to all who inhabit it, ps this is editted")
print("editted from ipad")

#GPIO22 Right:Forward
#GPIO23 Right:Backward
motor1 = Motor(22, 23)
led = LED(27)
led2 = LED(24)
button = Button(25)

try:
  while true:
    motor1.forward()
    time.sleep(1)
    motor1.forward(0.5)
    time.sleep(1)
    motor1.forward(0.1)
    time.sleep(1)
    motor1.backward()
    time.sleep(1)
    
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    
    led2.on()
    time.sleep(1)
    led2.off()
    time.sleep(1)
except KeyboardInterrupt:
    exit()

#GPIO22 Right:Forward
#GPIO23 Right:Backward
#GPIO24 Right:Forward
#GPIO25 Right:Backward

from gpiozero import LED
from gpiozero import Motor
import time


print("Hello to this great and prosperous world and to all who inhabit it, ps this is editted")
print("editted from ipad")

motor1 = Motor(22, 23)
motor1.forward()
time.sleep(1)
motor1.backward()
time.sleep(1)
motor1.forward(0.5)
time.sleep(1)
motor1.backward(0.5)
time.sleep(1)
#GPIO22 Right:Forward
#GPIO23 Right:Backward
#GPIO24 Right:Forward
#GPIO25 Right:Backward

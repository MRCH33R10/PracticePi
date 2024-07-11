from gpiozero import LED
import time


print("Hello to this great and prosperous world and to all who inhabit it, ps this is editted")
print("editted from ipad")

led1 = LED(22)
led2 = LED(23)
while(1):
  led1.on()
  time.sleep(1)
  led1.off()
  time.sleep(1)
  led2.on()
  time.sleep(1)
  led2.off()
  time.sleep(1)
#GPIO22 Right:Forward
#GPIO23 Right:Backward
#GPIO24 Right:Forward
#GPIO25 Right:Backward

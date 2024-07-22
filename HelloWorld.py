from gpiozero import Motor
from gpiozero import Button
from threading import Thread
from signal import pause
import sys
import time

print("Hello")

#GPIO22 Right:Forward
#GPIO23 Right:Backward
motorR = Motor(22, 23)
#GPIO27 Left:Forward
#GPIO24 Left:Backward
motorL = Motor(27, 24)

stgenum = iter(("blink", "close"))
i = next(stgenum)

def pressed():
    i = next(stgenum)

def waitncheck():
    time.sleep(1)
    if (i == "close"):
        quit()
    
def blink_led():
    while i == "blink":
        btn.when_pressed = pressed
        motorR.forward()
        waitncheck()
        motorR.forward(0.5)
        waitncheck()
        motorR.forward(0.1)
        waitncheck()
        motorR.backward()
        waitncheck()
        motorR.stop()
        
        motorL.forward()
        waitncheck()
        motorL.forward(0.5)
        waitncheck()
        motorL.forward(0.1)
        waitncheck()
        motorL.backward()
        waitncheck()
        motorL.stop()

            
btn = Button(25)
btn.when_pressed = pressed

blink_thread = Thread(target=blink_led)
blink_thread.start()

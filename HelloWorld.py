from gpiozero import Motor
from gpiozero import Button
from threading import Thread
from signal import pause
import sys
import time

# Right:(Forward,Backward).(GPIO22,GPIO23)
# Left :(Forward,Backward).(GPIO27,GPIO24)

motorR = Motor(22, 23)
motorL = Motor(27, 24)


stgenum = True

print("Hello")

def pressed():
    global stgenum
    stgenum = False

def waitncheck():
    global stgenum
    time.sleep(1)
    if not stgenum:
        return break

        

def blink_led():
    global stgenum
    while True:
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
    print("bye")
    exit()
btn = Button(25)
btn.when_pressed = pressed

blink_thread = Thread(target=blink_led)
blink_thread.start()

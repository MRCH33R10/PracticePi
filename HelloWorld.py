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
    for x in range(9):
        time.sleep(0.1)
        if not stgenum:
            quit()

        

def blink_led():
    while true:
        motorR.forward()
        waitncheck()
        motorR.forward(0.5)  # Adjust this line if Motor does not support this directly
        waitncheck()
        motorR.forward(0.1)  # Adjust this line if Motor does not support this directly
        waitncheck()
        motorR.backward()
        waitncheck()
        motorR.stop()

        motorL.forward()
        waitncheck()
        motorL.forward(0.5)  # Adjust this line if Motor does not support this directly
        waitncheck()
        motorL.forward(0.1)  # Adjust this line if Motor does not support this directly
        waitncheck()
        motorL.backward()
        waitncheck()
        motorL.stop()
    exit()
btn = Button(25)
btn.when_pressed = pressed

blink_thread = Thread(target=blink_led)
blink_thread.start()

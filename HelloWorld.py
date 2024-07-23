from gpiozero import Motor
from gpiozero import Button
from threading import Thread
from signal import pause
import sys
import time

print("Hello")

# GPIO22 Right:Forward
# GPIO23 Right:Backward
motorR = Motor(22, 23)
# GPIO27 Left:Forward
# GPIO24 Left:Backward
motorL = Motor(27, 24)

stgenum = True

def pressed():
    global stgenum
    stgenum = False

def waitncheck():
    time.sleep(1)
    if not stgenum:
        print("bye")
        exit_program()

def blink_led():
    while stgenum:
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

btn = Button(25)
btn.when_pressed = pressed

blink_thread = Thread(target=blink_led)
blink_thread.start()

pause()


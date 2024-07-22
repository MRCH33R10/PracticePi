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

def pressed():
    next(stgenum)
    print("Bye")

def waitncheck():
    time.sleep(1)
    if (stgenum == "close"):
        quit()
    
def blink_led():
    i = next(stgenum)
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



         
# import signal                   
# import sys
# import RPi.GPIO as GPIO

# BUTTON_GPIO = 25

# def signal_handler(sig, frame):
#     GPIO.cleanup()
#     sys.exit(0)

# def button_callback(channel):
#     if not GPIO.input(BUTTON_GPIO):
#         print("Button pressed!")
#     else:
#         print("Button released!")

# if __name__ == '__main__':
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
#     GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, 
#             callback=button_callback, bouncetime=50)
    
#     signal.signal(signal.SIGINT, signal_handler)
#     signal.pause()

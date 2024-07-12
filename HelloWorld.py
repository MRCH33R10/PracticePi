from gpiozero import Motor
from gpiozero import Button
from threading import Thread
from signal import pause
import sys
import time


print("Hello to this great and prosperous world and to all who inhabit it, ps this is editted")
print("editted from ipad")

#GPIO22 Right:Forward
#GPIO23 Right:Backward
motorR = Motor(22, 23)
#GPIO27 Left:Forward
#GPIO24 Left:Backward
motorL = Motor(27, 24)
blink = True
def pressed():
    global blink
    blink = False
    print("button was pressed")
    stop_threads = True
def blink_led():
    while blink:
        btn.when_pressed = pressed
        motorR.forward()
        time.sleep(1)
        motorR.forward(0.5)
        time.sleep(1)
        motorR.forward(0.1)
        time.sleep(1)
        motorR.backward()
        time.sleep(1)
        motorR.stop()
        
        motorL.forward()
        time.sleep(1)
        motorL.forward(0.5)
        time.sleep(1)
        motorL.forward(0.1)
        time.sleep(1)
        motorL.backward()
        time.sleep(1)
        motorL.stop()   
    
btn = Button(25)
stop_threads = False
btn.when_pressed = pressed

blink_thread = Thread(target=blink_ledargs =(lambda : stop_threads, ))
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

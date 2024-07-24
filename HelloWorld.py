from gpiozero import Motor
from gpiozero import Button
from signal import pause
import threading
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
        print("bye")
        stgenum = False
        
def mtr(spdl,spdr):
    if isinstance(spdr, float):
        motorR.forward(spdr) if spdr > 0 else motorR.forward(abs(spdr)) if spdr < 0 else motorR.stop()
    if isinstance(spdl, float):
        motorL.forward(spdl) if spdl > 0 else motorL.forward(abs(spdl)) if spdl < 0 else motorL.stop()
            
def blink_led():
    n = None
    x = 0
    seq = ((n,1.0),(n,0.5),(n,-1.0),(0.0,n),(1.0,n),(0.5,n),(-1.0,n),(0.0,n))
    
    global stgenum
    while stgenum:
        mtr(seq[x][0],seq[x][1])
        waitncheck()
        if x < (len(seq)-1):
            x += 1 
        else:
            x = 0

    print("bye")
    exit()

btn = Button(25)
btn.when_pressed = pressed

blink_thread = threading.Thread(target=blink_led)
blink_thread.start()

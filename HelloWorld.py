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
    
def mtr(spdl,spdr): 
    if isinstance(spdr, float):
        if spdr > 0:
            motorR.forward(spdr)  
        elif spdr < 0:
            motorR.backward(abs(spdr))  
        else: 
            motorR.stop()
            
    if isinstance(spdl, float):        
        if spdl > 0:
            motorL.forward(spdl)  
        elif spdl < 0:
            motorL.backward(abs(spdl))  
        else: 
            motorL.stop()
            
def blink_led():
    n = None
    x = 0
    seq = ((0.0,1.0),(n,0.5),(n,-1.0),(0.0,n),(1.0,0.0),(0.5,n),(-1.0,n),(0.0,n))
    
    global stgenum
    while stgenum:
        mtr(seq[x][0],seq[x][1])
        time.sleep(1)
        if x < (len(seq)-1): x += 1 
        else: x = 0

    print("bye")
    exit()

btn = Button(25)
btn.when_pressed = pressed

blink_thread = threading.Thread(target=blink_led)
blink_thread.start()

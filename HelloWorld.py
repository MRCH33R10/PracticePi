from gpiozero import Button, Motor, RotaryEncoder
from signal import pause
import threading
import sys
import time

# Right:(Forward,Backward).(GPIO22,GPIO23)
# Left :(Forward,Backward).(GPIO27,GPIO24)

motorR, motorL = Motor(22, 23), Motor(27, 24)
stgenum, x, n, i = 0, 0, None, 1
btn = Button(12, hold_time = 3, bounce_time = 0.2) #formally 25
encoder, MIN_VALUE, MAX_VALUE = RotaryEncoder(a=6, b=5, max_steps=0), 1, 8
encoder.steps = MIN_VALUE

print("Hello")

def pressed():
    global stgenum, x
    stgenum += 1
    x = 0
    
def mtr(spdl,spdr): 
    if isinstance(spdr, float):
        if spdr > 0:   motorR.forward(spdr)  
        elif spdr < 0: motorR.backward(abs(spdr))  
        else:          motorR.stop() 
    if isinstance(spdl, float):        
        if spdl > 0:   motorL.forward(spdl)  
        elif spdl < 0: motorL.backward(abs(spdl))  
        else:          motorL.stop()
            
def mtrseq(seq, disp):
        global x
        mtr(seq[x][0],seq[x][1])
        time.sleep(disp)
        if x < (len(seq)-1): x += 1 
        else: x = 0
            
def rotary_callback():
    if encoder.steps < MIN_VALUE:
        encoder.steps = MIN_VALUE
    elif encoder.steps > MAX_VALUE:
        encoder.steps = MAX_VALUE
    
def MtrFunct():
    global n, stgenum
    while True:
        if stgenum == 0:
            inptseq = ((0.0,1.0),(n,0.5),(n,0.1),(n,-1.0),(1.0,0.0),(0.5,n),(0.1,n),(-1.0,n))
            mtrseq(inptseq, 0.5)
        elif stgenum == 1:
            inptseq = ((1.0,1.0),(0.0,0.0),(-1.0,-1.0),(0.0,0.0))
            mtrseq(inptseq, (encoder.steps/4.0))              
        else:
            print("Bye")
            break
            

btn.when_pressed = pressed
encoder.when_rotated = rotary_callback

Mtr_thread = threading.Thread(target=MtrFunct)
Mtr_thread.start()


Mtr_thread.join()


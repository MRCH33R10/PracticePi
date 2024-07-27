from gpiozero import Button, Motor
from signal import pause
import threading
import sys
import time

# Right:(Forward,Backward).(GPIO22,GPIO23)
# Left :(Forward,Backward).(GPIO27,GPIO24)

motorR = Motor(22, 23)
motorL = Motor(27, 24)

stgenum, x, n = 0, 0, None

print("Hello")

def pressed():
    global stgenum
    stgenum += 1
    
def mtr(spdl,spdr): 
    if isinstance(spdr, float):
        if spdr > 0:   motorR.forward(spdr)  
        elif spdr < 0: motorR.backward(abs(spdr))  
        else:          motorR.stop() 
    if isinstance(spdl, float):        
        if spdl > 0:   motorL.forward(spdl)  
        elif spdl < 0: motorL.backward(abs(spdl))  
        else:          motorL.stop()
            
def mtrseq(seq):
        mtr(seq[x][0],seq[x][1])
        time.sleep(0.5)
        if x < (len(seq)-1): x += 1 
        else: x = 0
            
def MtrFunct():
    global n, stgenum, x
    while True:
        if stgenum == 0:
            inptseq = ((0.0,1.0),(n,0.5),(n,0.1),(n,-1.0),(1.0,0.0),(0.5,n),(0.1,n),(-1.0,n))
            mtrseq(inptseq)
        elif stgenum == 1:
            inptseq = ((1.0,1.0),(0.0,0.0),(-1.0,-1.0),(0.0,0.0))
            mtrseq(inptseq)              
        elif stgenum == 2:
            print("Bye")
            break
            

btn = Button(12) #formally 25
button = Button(25)
btn.when_pressed = pressed

Mtr_thread = threading.Thread(target=MtrFunct)
Mtr_thread.start()


Mtr_thread.join()


# from gpiozero import Button, Motor
# from signal import pause
# import threading
# import sys
# import time

# # Right:(Forward,Backward).(GPIO22,GPIO23)
# # Left :(Forward,Backward).(GPIO27,GPIO24)

# motorR = Motor(22, 23)
# motorL = Motor(27, 24)

# button_pins = [12, 25]  # Replace with your actual GPIO pin numbers

# # Initialize buttons
# buttons = [Button(pin) for pin in button_pins]

# # Define actions for button presses
# def action_button_1():
#     print("Button 1 pressed")
#     # Add your custom logic here

# def action_button_2():
#     print("Button 2 pressed")
#     # Add your custom logic here

# def button_thread(button, action):
#     button.when_pressed = action
#     button.wait_for_press()
#     button.wait_for_release()
    
# stgenum = True
# n = None

# print("Hello")

# def pressed():
#     global stgenum
#     stgenum = False
    
# def mtr(spdl,spdr): 
#     if isinstance(spdr, float):
#         if spdr > 0:   motorR.forward(spdr)  
#         elif spdr < 0: motorR.backward(abs(spdr))  
#         else:          motorR.stop() 
#     if isinstance(spdl, float):        
#         if spdl > 0:   motorL.forward(spdl)  
#         elif spdl < 0: motorL.backward(abs(spdl))  
#         else:          motorL.stop()
            
# def MtrFunct():
#     global n, stgenum
#     x = 0
#     seq = ((0.0,1.0),(n,0.5),(n,0.1),(n,-1.0),
#            (1.0,0.0),(0.5,n),(0.1,n),(-1.0,n))
#     while stgenum:
#         mtr(seq[x][0],seq[x][1])
#         time.sleep(0.5)
#         if x < (len(seq)-1): x += 1 
#         else: x = 0
#     print("Bye")
#     exit()

# btn = Button(12) #formally 25
# btn.when_pressed = pressed

# threads = [
#     threading.Thread(target=button_thread, args=(buttons[0], action_button_1)),
#     threading.Thread(target=button_thread, args=(buttons[1], action_button_2)),
#     threading.Thread(target=MtrFunct)
# ]

# for thread in threads:
#     thread.start()

from gpiozero import Button, Motor
from signal import pause
import threading
import sys
import time

# Right:(Forward, Backward).(GPIO22, GPIO23)
# Left :(Forward, Backward).(GPIO27, GPIO24)

motorR = Motor(22, 23)
motorL = Motor(27, 24)

button_pins = [12, 25]  # Replace with your actual GPIO pin numbers

# Initialize buttons
buttons = [Button(pin) for pin in button_pins]

# Define actions for button presses
def action_button_1():
    print("Button 1 pressed")
    # Add your custom logic here

def action_button_2():
    print("Button 2 pressed")
    # Add your custom logic here

def button_thread(button, action):
    button.when_pressed = action
    pause()  # Keep the thread running and listening for button presses

# Global variables
stgenum = True
n = 0.5  # Assuming n should be a float value for motor speed

print("Hello")

def pressed():
    global stgenum
    stgenum = False

def mtr(spdl, spdr): 
    if isinstance(spdr, float):
        if spdr > 0:   motorR.forward(spdr)  
        elif spdr < 0: motorR.backward(abs(spdr))  
        else:          motorR.stop() 
    if isinstance(spdl, float):        
        if spdl > 0:   motorL.forward(spdl)  
        elif spdl < 0: motorL.backward(abs(spdl))  
        else:          motorL.stop()

def MtrFunct():
    global n, stgenum
    x = 0
    seq = ((0.0, 1.0), (n, 0.5), (n, 0.1), (n, -1.0),
           (1.0, 0.0), (0.5, n), (0.1, n), (-1.0, n))
    while stgenum:
        mtr(seq[x][0], seq[x][1])
        time.sleep(0.5)
        if x < (len(seq) - 1): 
            x += 1 
        else: 
            x = 0
    print("Bye")
    sys.exit()

# Initialize the button to stop the motor function
btn = Button(12)
btn.when_pressed = pressed

# Create threads for button actions and motor function
threads = [
    threading.Thread(target=button_thread, args=(buttons[0], action_button_1)),
    threading.Thread(target=button_thread, args=(buttons[1], action_button_2)),
    threading.Thread(target=MtrFunct)
]

# Start the threads
for thread in threads:
    thread.start()

# Keep the main program running
pause()


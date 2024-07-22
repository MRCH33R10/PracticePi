from gpiozero import Motor, Button
from threading import Thread
from signal import pause
import time

print("Hello")

#GPIO22 Right:Forward
#GPIO23 Right:Backward
motorR = Motor(22, 23)
#GPIO27 Left:Forward
#GPIO24 Left:Backward
motorL = Motor(27, 24)

stgenum = iter(("blink", "close"))
i = next(stgenum)

def pressed():
    global i
    try:
        i = next(stgenum)
    except StopIteration:
        # Reset the generator if it reaches the end
        stgenum = iter(("blink", "close"))
        i = next(stgenum)

def waitncheck():
    global i
    time.sleep(1)
    if i == "close":
        sys.exit()

def blink_led():
    while True:
        if i == "blink":
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
        else:
            time.sleep(0.1)

btn = Button(25)
btn.when_pressed = pressed

blink_thread = Thread(target=blink_led)
blink_thread.start()

pause()  # Keep the main thread running

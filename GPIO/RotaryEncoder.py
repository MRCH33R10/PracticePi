from gpiozero import RotaryEncoder, Button
from signal import pause

# Define the pins connected to the rotary encoder
encoder = RotaryEncoder(a=6, b=5, max_steps=0)

# Define the button connected to pin 25
button = Button(12)

# Define the range limits
MIN_VALUE = 0
MAX_VALUE = 3

def rotary_callback():
    if encoder.steps < MIN_VALUE:
        encoder.steps = MIN_VALUE
    elif encoder.steps > MAX_VALUE:
        encoder.steps = MAX_VALUE

    print(f"Encoder value: {encoder.steps}")

def button_callback():
    print("Button pressed")

print("Rotary Encoder and Button Test")
print("Rotate the encoder to see the changes in steps.")
print("Press the button to see the button press message.")

# Attach the callbacks to the rotary encoder and button
encoder.when_rotated = rotary_callback
button.when_pressed = button_callback

# Keep the program running to detect events
pause()


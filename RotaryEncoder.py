# from gpiozero import RotaryEncoder
# from signal import pause

# # Define the pins connected to the rotary encoder
# encoder = RotaryEncoder(a=5, b=6, max_steps=0)

# def rotary_callback():
#     print(f"Encoder value: {encoder.steps}")

# # Attach the callback to the rotary encoder
# encoder.when_rotated = rotary_callback

# print("Rotary Encoder Test")
# print("Rotate the encoder to see the changes in steps.")

# # Keep the program running to listen for encoder changes
# pause()


# from gpiozero import RotaryEncoder
# from signal import pause

# # Define the pins connected to the rotary encoder
# encoder = RotaryEncoder(a=6, b=5, max_steps=0)

# # Define the range limits


# def rotary_callback():
#     MIN_VALUE = 0
#     MAX_VALUE = 3
    
#     if encoder.steps < MIN_VALUE:
#         encoder.steps = MIN_VALUE
#     elif encoder.steps > MAX_VALUE:
#         encoder.steps = MAX_VALUE
      
    
#     print(f"Encoder value: {encoder.steps}")

# print("Rotary Encoder Test")
# print("Rotate the encoder to see the changes in steps.")

# # Attach the callback to the rotary encoder
# encoder.when_rotated = rotary_callback

from gpiozero import RotaryEncoder, Button
from signal import pause

# Define the pins connected to the rotary encoder
encoder = RotaryEncoder(a=6, b=5, max_steps=0)

# Define the button connected to pin 25
button = Button(25)

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
# encoder.when_rotated = rotary_callback
button.when_pressed = button_callback

# Keep the program running to detect events
pause()


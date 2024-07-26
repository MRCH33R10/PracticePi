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


from gpiozero import RotaryEncoder
from signal import pause

# Define the pins connected to the rotary encoder
encoder = RotaryEncoder(a=5, b=6, max_steps=0)

# Define the range limits
MIN_VALUE = 0
MAX_VALUE = 3

def rotary_callback():
    # Constrain the encoder value within the range
    value = encoder.steps % (MAX_VALUE + 1)
    if value < MIN_VALUE:
        value += (MAX_VALUE + 1)
    
    print(f"Encoder value: {value}")

print("Rotary Encoder Test")
print("Rotate the encoder to see the changes in steps.")

# Attach the callback to the rotary encoder
encoder.when_rotated = rotary_callback

# Keep the program running to listen for encoder changes
pause()

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

# Initialize the current step value within the range
current_value = 0

def rotary_callback(RoL):
    global current_value
    if (RoL == True):
        print("right")
        if (current_value != MAX_VALUE): current_value -= 1
    elif (RoL == False):
        print("left")
        if (current_value != MIN_VALUE): current_value += 1
    print(f"Encoder value: {current_value}")

print("Rotary Encoder Test")
print("Rotate the encoder to see the changes in steps.")

# Attach the callback to the rotary encoder
encoder.when_rotated = rotary_callback(True)
encoder.when_rotated = rotary_callback(False)

# Keep the program running to listen for encoder changes
pause()

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

def rotary_callback():
    global current_value
    steps = encoder.steps

    # Calculate the new value based on the current encoder steps
    if steps > 0:
        new_value = min(current_value + 1, MAX_VALUE)
    elif steps < 0:
        new_value = max(current_value - 1, MIN_VALUE)
    else:
        new_value = current_value

    # Update the current value and reset the encoder steps
    if new_value != current_value:
        current_value = new_value
        encoder.steps = 0  # Reset the encoder steps to prevent accumulation

    print(f"Encoder value: {current_value}")

print("Rotary Encoder Test")
print("Rotate the encoder to see the changes in steps.")

# Attach the callback to the rotary encoder
encoder.when_rotated = rotary_callback

# Keep the program running to listen for encoder changes
pause()

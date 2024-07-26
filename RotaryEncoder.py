from gpiozero import RotaryEncoder
from signal import pause

# Set up the rotary encoder on GPIO pins 17 and 18
rotor = RotaryEncoder(5, 6)

# Function to print the counter value
def print_value():
    print(rotor.steps)

# Attach the function to be called whenever the encoder value changes
rotor.when_rotated = print_value

# Keep the program running to continue responding to encoder changes
pause()

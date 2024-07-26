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

# from gpiozero import Button

# pin_a = Button(5,pull_up=True)         # Rotary encoder pin A connected to GPIO2
# pin_b = Button(6,pull_up=True)         # Rotary encoder pin B connected to GPIO3

# def pin_a_rising():                    # Pin A event handler
#     if pin_b.is_pressed: print("-1")   # pin A rising while A is active is a clockwise turn

# def pin_b_rising():                    # Pin B event handler
#     if pin_a.is_pressed: print("1")    # pin B rising while A is active is a clockwise turn

# pin_a.when_pressed = pin_a_rising      # Register the event handler for pin A
# pin_b.when_pressed = pin_b_rising      # Register the event handler for pin B

# input("Turn the knob, press Enter to quit.\n")

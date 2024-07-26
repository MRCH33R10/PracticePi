from gpiozero import RotaryEncoder, PWMLED
from gpiozero.tools import scaled_half
from signal import pause

# Set up the rotary encoder on GPIO pins 21 and 20
rotor = RotaryEncoder(5, 6)

# Set up the PWM LED on GPIO pin 5
led = PWMLED(13)

# Link the output of the rotary encoder to the LED's brightness,
# scaling the value to half of the encoder's range.
led.source = scaled_half(rotor.values)

# Keep the program running to continue responding to encoder changes
pause()

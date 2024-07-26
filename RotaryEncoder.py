from gpiozero import RotaryEncoder
from gpiozero.tools import scaled_half

rotor = RotaryEncoder(5, 6)
led = PWMLED(13)
led.source = scaled_half(rotor.values)

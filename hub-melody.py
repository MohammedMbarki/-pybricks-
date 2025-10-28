from pybricks.hubs import PrimeHub
from pybricks.parameters import Button

# Initialize the hub
hub = PrimeHub()

# Configure the stop button combination. Now, your program stops
# if you press the center and Bluetooth buttons simultaneously.
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

# Define the melody as a list of (frequency, duration) tuples
melody = [
    (440, 500),  # A4, 500 ms
    (494, 500),  # B4, 500 ms
    (523, 500),  # C5, 500 ms
    (587, 500),  # D5, 500 ms
    (659, 500),  # E5, 500 ms
    (698, 500),  # F5, 500 ms
    (784, 500),  # G5, 500 ms
    (880, 500),  # A5, 500 ms
]

# Main loop
while True:
    # Play the melody if the center button is pressed
    if Button.CENTER in hub.buttons.pressed():
        for note in melody:
            frequency, duration = note
            hub.speaker.beep(frequency, duration)
            hub.speaker.beep(frequency, duration)

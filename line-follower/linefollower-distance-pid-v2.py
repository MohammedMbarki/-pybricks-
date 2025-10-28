from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize hub and devices
hub = InventorHub()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
color_sensor = ColorSensor(Port.F)

# Initialize the drive base
wheel_diameter = 56
axle_track = 130
wheels = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# PID constants
KP = 1.0
KD = 0.5

def follow_line_for_distance_left(target_distance, speed):
    # PID variables
    last_error = 0

    # Initial distance
    initial_distance = wheels.distance()

    while wheels.distance() - initial_distance < target_distance:
        # Read color sensor reflection
        reflection = color_sensor.reflection()

        # Calculate error from the threshold (assuming black and white values as 0 and 100)
        threshold = 50
        error = reflection - threshold  # Inverted error to follow the line to the right

        # Calculate derivative
        derivative = error - last_error

        # Calculate correction
        correction = KP * error + KD * derivative

        # Apply correction to maintain line following
        wheels.drive(speed, correction)  # Positive correction turns right

        # Update last error
        last_error = error

        # Wait a short moment
        wait(10)

        # Debug statements to check values
        # print(f"Distance: {wheels.distance() - initial_distance}, Reflection: {reflection}, Error: {error}, Correction: {correction}")

    # Stop the motors after reaching the distance
    wheels.stop()


def follow_line_for_distance_right(target_distance, speed):
    # PID variables
    last_error = 0

    # Initial distance
    initial_distance = wheels.distance()

    while wheels.distance() - initial_distance < target_distance:
        # Read color sensor reflection
        reflection = color_sensor.reflection()

        # Calculate error from the threshold (assuming black and white values as 0 and 100)
        threshold = 50
        error = reflection - threshold  # Invert error calculation for left-following

        # Calculate derivative
        derivative = error - last_error

        # Calculate correction
        correction = KP * error + KD * derivative

        # Apply correction to maintain line following
        wheels.drive(speed, -correction)  # Negative correction to steer left

        # Update last error
        last_error = error

        # Wait a short moment
        wait(10)

        # Debug statements to check values
        print(f"Distance: {wheels.distance() - initial_distance}, Reflection: {reflection}, Error: {error}, Correction: {correction}")

    # Stop the motors after reaching the distance
    wheels.stop()



def follow_line_for_distance(Direction, target_distance, speed):
    if Direction == 'R':
        # PID variables
        KP = 1.0  # Replace with appropriate value
        KD = 0.5  # Replace with appropriate value
        last_error = 0

        # Initial distance
        initial_distance = wheels.distance()

        while wheels.distance() - initial_distance < target_distance:
            # Read color sensor reflection
            reflection = color_sensor.reflection()

            # Calculate error from the threshold (assuming black and white values as 0 and 100)
            threshold = 50
            error = reflection - threshold  # Invert error calculation for left-following

            # Calculate derivative
            derivative = error - last_error

            # Calculate correction
            correction = KP * error + KD * derivative

            # Apply correction to maintain line following
            wheels.drive(speed, -correction)  # Negative correction to steer left

            # Update last error
            last_error = error

            # Wait a short moment
            wait(10)

            # Debug statements to check values
            print(f"Distance: {wheels.distance() - initial_distance}, Reflection: {reflection}, Error: {error}, Correction: {correction}")

        # Stop the motors after reaching the distance
        wheels.stop()
    

    elif Direction == 'L':
        # PID variables
        KP = 1.0  # Replace with appropriate value
        KD = 0.5  # Replace with appropriate value
        last_error = 0

        # Initial distance
        initial_distance = wheels.distance()

        while wheels.distance() - initial_distance < target_distance:
            # Read color sensor reflection
            reflection = color_sensor.reflection()

            # Calculate error from the threshold (assuming black and white values as 0 and 100)
            threshold = 50
            error = reflection - threshold  # Inverted error to follow the line to the right

            # Calculate derivative
            derivative = error - last_error

            # Calculate correction
            correction = KP * error + KD * derivative

            # Apply correction to maintain line following
            wheels.drive(speed, correction)  # Positive correction turns right

            # Update last error
            last_error = error

            # Wait a short moment
            wait(10)

            # Debug statements to check values
            # print(f"Distance: {wheels.distance() - initial_distance}, Reflection: {reflection}, Error: {error}, Correction: {correction}")

        # Stop the motors after reaching the distance
        wheels.stop()

# Example usage
follow_line_for_distance('L', 400, 200)

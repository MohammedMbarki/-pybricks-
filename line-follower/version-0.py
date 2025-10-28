


from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

color_sensor = ColorSensor(Port.F)

wheels = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=105)

def followLineForDistance(distance):
    initial_distance = wheels.distance()
    while wheels.distance() - initial_distance < distance:
        intensity = color_sensor.reflection()
        if intensity < 40:
            wheels.drive(200, 20)
        else:
            wheels.drive(200, -20) 
        wait(10)

    
    wheels.stop()

followLineForDistance(700)

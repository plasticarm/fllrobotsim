
# This code was automatically generated for mission: Scrimmage2
# It assumes a library named '*' with asynchronous commands for movement and rotation.
"""
Available functions in the common library:

setupMotors()
resetYaw()
degreesForDistance(distance_cm)
drive(distance, speed)
rotateRightArm(degrees, speed)
rotateLeftArm(degrees, speed)
rotateCenterArm(degrees, speed)
resetArmRotation()
turn_done()
rotateDegrees(degrees, speed)
spin_turn(robot_degrees, motor_speed)
pivot_turn(robot_degrees, motor_speed)
all_done()
beep(frequency, duration)
"""

from common import *
import runloop

async def main():
    # Starting mission: Scrimmage2
    # Initial Position: 75.92, -44.72 cm
    # Initial Angle: 0.00 degrees   
    # Initialize the motor pair for wheels and save motor positions. Do this every time.
    await init()

    await drive(45.00, 1000)
    await rotateRightArm(90, 500)
    await rotateRightArm(90, 500)
    await rotateRightArm(90, 500)
    await drive(19.00, 1000)
    await rotateDegrees(20.00, 500)
    await drive(3.00, 1000)
    await rotateDegrees(-30.00, 500)
    await rotateDegrees(-20.00, 500)
    await drive(5.00, 1000)
    await rotateDegrees(-60.00, 500)
    await drive(10.00, 1000)
    await rotateDegrees(90.00, 500)
    await drive(2.00, 1000)
    await rotateDegrees(-15.00, 500)
    await drive(-2.00, 1000)
    await rotateDegrees(-75.00, 500)
    await drive(48.00, 1000)
    await rotateDegrees(-90.00, 500)
    await rotateLeftArm(90, 500)
    await drive(-15.00, 1000)
    await rotateDegrees(-45.00, 500)
    await drive(10.00, 1000)
    await rotateDegrees(-45.00, 500)
    await drive(8.00, 1000)
    await rotateDegrees(45.00, 500)
    await drive(21.00, 1000)
    await drive(-10.00, 1000)
    await rotateDegrees(-45.00, 500)
    await drive(10.00, 1000)
    await rotateDegrees(45.00, 500)
    await drive(26.00, 1000)
    await rotateDegrees(90.00, 500)
    await rotateRightArm(90, 500)
    await drive(14.00, 1000)
    await rotateRightArm(90, 500)
    await rotateRightArm(90, 500)
    await drive(39.00, 1000)
    await rotateDegrees(45.00, 500)
    await rotateDegrees(90.00, 500)
    await drive(10.00, 1000)
    await rotateLeftArm(90, 500)
    await drive(-10.00, 1000)
    await rotateDegrees(100.00, 500)
    await drive(50.00, 1000)

    # reset the arms before finishing so they are ready to go again.
    await resetArmRotation()

runloop.run(main())

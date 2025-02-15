### 1️⃣ gait_control.py - Walking Gait Algorithm
"""
This script controls the walking gait of the Stanford Pupper bot using four MG996R servos.
The gait implemented here is a simple trot.
"""
from machine import Pin, PWM
import time

# Placeholder: Servo pin assignments
front_left = PWM(Pin(15))
front_right = PWM(Pin(16))
back_left = PWM(Pin(17))
back_right = PWM(Pin(18))

# Function to move servo
def move_servo(servo, angle):
    duty = int((angle / 180) * 5000 + 2500)
    servo.duty_u16(duty)

# Simple Trot Gait
def trot_step():
    # Lift front left and back right
    move_servo(front_left, 45)
    move_servo(back_right, 45)
    time.sleep(0.2)
    
    # Return to ground
    move_servo(front_left, 90)
    move_servo(back_right, 90)
    time.sleep(0.2)
    
    # Lift front right and back left
    move_servo(front_right, 45)
    move_servo(back_left, 45)
    time.sleep(0.2)
    
    # Return to ground
    move_servo(front_right, 90)
    move_servo(back_left, 90)
    time.sleep(0.2)

# Continuous Gait Loop
def walk():
    while True:
        trot_step()

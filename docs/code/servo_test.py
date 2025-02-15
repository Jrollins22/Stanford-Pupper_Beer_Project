# 📂 Stanford Pupper Bot - Servo Test Script
# This script tests the MG996R servos connected to the Raspberry Pi Pico.
# It moves each servo from 0° to 180° and back to 90° (neutral position).

from machine import Pin, PWM
import time

# Servo Pin Assignments (Adjust according to your wiring)
servo_pins = [15, 16, 17, 18]  # GPIO pins for the servos

# Initialize PWM for Servos
servos = []
for pin in servo_pins:
    pwm = PWM(Pin(pin))
    pwm.freq(50)  # Set PWM frequency to 50Hz (standard for servos)
    servos.append(pwm)

# Function to convert angle to duty cycle
def angle_to_duty(angle):
    return int((angle / 180 * 5000) + 2500)  # Duty cycle range: 500-2500 (0-180°)

# Function to move servo to a specified angle
def move_servo(servo, angle):
    duty = angle_to_duty(angle)
    servo.duty_u16(duty)
    time.sleep(0.5)

# Servo Test Routine
def test_servos():
    print("Starting servo test...")
    for i, servo in enumerate(servos):
        print(f"Testing Servo {i+1} on GPIO {servo_pins[i]}")
        # Move from 0° to 180°
        for angle in range(0, 181, 30):
            move_servo(servo, angle)
        # Return to 90° (neutral)
        move_servo(servo, 90)
        time.sleep(0.5)
    print("Servo test completed.")

# Run the test
test_servos()

# Stop all servos after test
for servo in servos:
    servo.duty_u16(0)
    servo.deinit()

print("All servos stopped.")

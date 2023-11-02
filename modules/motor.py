import RPi.GPIO as GPIO
import time


class MotorModule:
    def __init__(self):
        self.CONTACTS = [20, 21]
        self.DIRECTION = [2, 4]
        self.STEP = [3, 17]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DIRECTION[0], GPIO.OUT)
        GPIO.setup(self.DIRECTION[1], GPIO.OUT)
        GPIO.setup(self.STEP[0], GPIO.OUT)
        GPIO.setup(self.STEP[1], GPIO.OUT)
        GPIO.output(self.DIRECTION[0], GPIO.HIGH)
        GPIO.output(self.DIRECTION[1], GPIO.HIGH)
        self.DELAY = 0.005 / 4
        self.STEP_DISTANCE = 0.001
        GPIO.setup(self.CONTACTS[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.CONTACTS[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def move(self, axis, direction, steps):
        GPIO.output(self.DIRECTION[axis], direction)
        for i in range(int(steps)):
            GPIO.output(self.STEP[axis], GPIO.HIGH)
            time.sleep(self.DELAY)
            GPIO.output(self.STEP[axis], GPIO.LOW)
            time.sleep(self.DELAY)

    def return_home(self):
        while not GPIO.input(self.CONTACTS[0]):  # verificar gpio
            self.move(0, 0, 1)
        while not GPIO.input(self.CONTACTS[1]):  # verificar gpio
            self.move(1, 0, 1)

    def follow_path(self, path):
        # array de tuplas: [(2,4), (-1,8), (-5,9)]
        for movement in path:
            direction_x = 1 if movement[0] > 0 else 0
            direction_y = 1 if movement[1] > 0 else 0
            self.move(0, direction_x, movement[0] / self.STEP_DISTANCE)
            self.move(0, direction_y, movement[1] / self.STEP_DISTANCE)

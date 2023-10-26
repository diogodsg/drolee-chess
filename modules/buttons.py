import RPi.GPIO as GPIO

QUEEN_BUTTON_PIN = 1
BISHOP_BUTTON_PIN = 2
KNIGHT_BUTTON_PIN = 3
ROOK_BUTTON_PIN = 4

class ButtonsModule:
    def __init__(self):

        self.button_map = {"queen": QUEEN_BUTTON_PIN, "bishop": BISHOP_BUTTON_PIN, "knight": KNIGHT_BUTTON_PIN, "rook": ROOK_BUTTON_PIN}

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(QUEEN_BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(BISHOP_BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(KNIGHT_BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(ROOK_BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def buttonPressed(self, button) -> bool:
        return GPIO.input(self.button_map[button])

    

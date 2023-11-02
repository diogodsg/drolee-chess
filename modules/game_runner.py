import time
import RPi.GPIO as GPIO
import numpy as np
from modules.camera import CameraModule
from modules.game_logic import GameLogicModule
from utils.move_detector import detect_movement
from modules.display import DisplayModule


class GameRunner:
    def __init__(self, color, has_time, difficulty, display: DisplayModule):
        self.display = display
        self.chess_game = GameLogicModule(difficulty=difficulty)
        self.illegal_state = False
        self.bot_move = ""
        self.player_turn = True if color == "WHITE" else False
        self.camera_module = CameraModule((0, 0), (200, 200))
        board = self.camera_module.detect_game()
        self.left_cem_state = board["left_cemitery"]
        self.last_state = board["main_board"]
        self.right_cem_state = board["right_cemitery"]
        self.player_time = 10 * 60  # 10 min in seconds
        GPIO.setmode(GPIO.BCM)
        self.last_timestamp = time.time()

    def run(self):
        while not self.chess_game.board.outcome:
            if self.has_time:
                self.display.display(
                    0, "Tempo: " + time.strftime("%M:%S", time.gmtime(self.player_time))
                )
                self.handle_time()
            self.handle_frame()

        GPIO.cleanup()

    def handle_time(self):
        if self.player_turn:
            now = time.time()
            self.player_time -= now - self.last_timestamp
            self.last_timestamp = now

    def handle_frame(self):
        board = self.camera_module.detect_game()

        if board["obstructed"]:
            self.display.display(1, "Obstruido!")

        elif self.illegal_state or self.bot_move:
            self.display.display(1, "Estado ilegal!")
            self.handle_illegal_state(board)
        else:
            self.handle_legal_state(board["main_board"])

        time.sleep(0.1)

    def handle_illegal_state(self, board):
        new_state = self.chess_game.make_matrix()
        if np.array_equal(board["main_board"], np.array(new_state, dtype=float)):
            self.illegal_state = False
            self.bot_move = ""

        self.last_state = new_state

    def handle_legal_state(self, state):
        if self.player_turn:
            self.display.display(1, "Sua Vez!")
            move = detect_movement(self.last_state, state)
            if move:
                valid_move = self.chess_game.make_move(move)
                if valid_move:
                    self.player_turn = False
                else:
                    self.illegal_state = True

                print(self.player_turn)
        else:
            self.bot_move = self.chess_game.get_bot_move()
            self.display.display(1, "Vez do Tabuleiro")
            # fazer movimento fisico
            self.player_turn = True
            self.last_timestamp = time.time()

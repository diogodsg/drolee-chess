import time
import numpy as np
from modules.camera import CameraModule
from utils.move_detector import detect_movement
from modules.game_logic import GameLogicModule
from modules.display import DisplayModule
from modules.buttons import ButtonsModule


class GameRunner:
    def __init__(self):
        self.chess_game = GameLogicModule()
        self.illegal_state = False
        self.bot_move = ""
        self.player_turn = True
        self.camera_module = CameraModule()
        board = self.camera_module.detect_game()
        self.left_cem_state = board["left_cemetery"]
        self.last_state = board["main_board"]
        self.right_cem_state = board["right_cemetery"]

    def run(self):
        while "Screen capturing":
            self.handle_frame()

        GPIO.cleanup()

    def handle_frame(self):
        board = self.camera_module.detect_game()

        if board["invalid"]:
            self.illegal_state = True

        if self.illegal_state or self.bot_move:
            self.handle_illegal_state(board)
        else:
            self.handle_legal_state(board["main_board"])

        time.sleep(0.1)

    def handle_illegal_state(self, board):
        new_state = self.chess_game.make_matrix()
        if np.array_equal(board["main_board"], np.array(new_state, dtype=float)):
            self.illegal_state = False
            self.bot_move = False

        self.last_state = new_state

    def handle_legal_state(self, state):
        if not self.player_turn:
            self.bot_move = self.chess_game.get_bot_move()
            self.player_turn = True

        else:
            move = detect_movement(self.last_state, state)
            print(move)
            if move:
                valid_move = self.chess_game.make_move(move)
                self.illegal_state = True
                if valid_move:
                    self.player_turn = False
                print(self.player_turn)


class Menu:
    def __init__(self):
        self.buttons = ButtonsModule()

        self.color = self.selectColor()
        self.diff = self.selectDifficulty()
        self.game_time = self.selectTime()

    def selectColor(self):
        DisplayModule.display(0, "Selecione a cor")
        DisplayModule.display(1, "Q-Brancas R-Pretas")

        if self.buttons.buttonPressed("queen"):
            DisplayModule.display(0, "Cor Branca")
            DisplayModule.display(1, "Selecionada")
            time.sleep(2)
            return 0
        elif self.buttons.buttonPressed("rook"):
            DisplayModule.display(0, "Cor Preta")
            DisplayModule.display(1, "Selecionada")
            time.sleep(2)
            return 1

    def selectDifficulty(self):
        DisplayModule.display(0, "Selecione a dificuldade")
        DisplayModule.display(1, "Q-1 B-2 N-3 R-4")
        if self.buttons.buttonPressed("queen"):
            DisplayModule.display(0, "Dificuldade 1")
            DisplayModule.display(1, "Selecionada")
            time.sleep(2)
            return 0
        elif self.buttons.buttonPressed("bishop"):
            DisplayModule.display(0, "Dificuldade 2")
            DisplayModule.display(1, "Selecionada")
            time.sleep(2)
            return 1
        elif self.buttons.buttonPressed("knight"):
            DisplayModule.display(0, "Dificuldade 3")
            DisplayModule.display(1, "Selecionada")
            time.sleep(2)
            return 2
        elif self.buttons.buttonPressed("rook"):
            DisplayModule.display(0, "Dificuldade 4")
            DisplayModule.display(1, "Selecionada")
            time.sleep(2)
            return 3

    def selectTime(self):
        DisplayModule.display(0, "Selecione a o tempo")
        DisplayModule.display(1, "Q-Sem tempo R-10 min")

        if self.buttons.buttonPressed("queen"):
            DisplayModule.display(0, "Sem tempo")
            DisplayModule.display(1, "Selecionado")
            time.sleep(2)
            return 0
        elif self.buttons.buttonPressed("rook"):
            DisplayModule.display(0, "10 min")
            DisplayModule.display(1, "Selecionado")
            time.sleep(2)
            return 1
    
    def select_promotion(self):
        DisplayModule.display(0, "Selecione a promocao")
        DisplayModule.display(1, "desejada")
        if self.buttons.buttonPressed("queen"):
            DisplayModule.display(0, "Peao promovido")
            DisplayModule.display(1, "para rainha")
            time.sleep(2)
            return 0
        elif self.buttons.buttonPressed("bishop"):
            DisplayModule.display(0, "Peao promovido")
            DisplayModule.display(1, "para bispo")
            time.sleep(2)
            return 1
        elif self.buttons.buttonPressed("knight"):
            DisplayModule.display(0, "Peao promovido")
            DisplayModule.display(1, "para cavalo")
            time.sleep(2)
            return 2
        elif self.buttons.buttonPressed("rook"):
            DisplayModule.display(0, "Peao promovido")
            DisplayModule.display(1, "para torre")
            time.sleep(2)
            return 3



if __name__ == "__main__":
    GameRunner().run()


#
#    Menu:
#        Welcome to drole chess

#         pergunto se quer jogar com preto ou branco
#         pergunto dificuldade
#         pergunto se quer jogar com tempo

#         pressione para iniciar o jogo

#         mostrar timer

#         Peças pretas ganharam
#         Peças brancas ganharam
#         presisone sus pra continuar

#         promover para:
#         Q K H B


#     ButtonModule:
#         botao resign

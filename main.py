
import cv2
import numpy
import time
import mss
import numpy as np
from modules.camera import CameraModule
from utils.move_detector import detect_movement
from modules.game_logic import GameLogicModule

class GameRunner:
    def __init__(self):
        self.chess_game = GameLogicModule()
        self.monitor = {"top": 230, "left": 10, "width": 480, "height": 480}
        self.last_state = None
        self.illegal_state = False
        self.bot_move = ""
        self.player_turn = True

    def run(self):
        with mss.mss() as sct:
            img = numpy.array(sct.grab(self.monitor))
            bd = CameraModule(img, (25,40), (445,460))
            self.last_state = bd.detect()
            while "Screen capturing":
                self.handle_frame(sct)
                
                 # Press "q" to quit
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break
                
    def handle_frame(self, sct):
        img = numpy.array(sct.grab(self.monitor))
        bd = CameraModule(img, (25,40), (445,460))
        state = bd.detect()
        
        if bd.invalid:
            self.illegal_state = True

        if self.illegal_state or self.bot_move:
            self.handle_illegal_state(sct)            
        else:
            self.handle_legal_state(img, state)
                

        time.sleep(0.1)

    def handle_illegal_state(self, sct):
        new_state = self.chess_game.make_matrix()
        img = numpy.array(sct.grab(self.monitor))
        bd = CameraModule(img, (25,40), (445,460))   
        bd.write(f"BOT_MOVE {self.bot_move}" if self.bot_move else "INVALID")
        cv2.imshow("OpenCV/Numpy normal", img)
        if np.array_equal(bd.detect(), np.array(new_state, dtype=float)):
            self.illegal_state = False
            self.bot_move = False
            
        self.last_state = new_state        

    def handle_legal_state(self, img, state):
        cv2.imshow("OpenCV/Numpy normal", img)

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
       

if __name__ == "__main__":
    GameRunner().run()
import chess
from stockfish import Stockfish


class GameLogicModule:
    def __init__(self, difficulty, color: str):
        self.board = chess.Board()
        self.stockfish = Stockfish(path="./Stockfish-sf_15/src/stockfish")
        self.stockfish.set_fen_position(self.board.fen())
        self.stockfish.set_skill_level(difficulty)
        if color != "WHITE":
            self.get_bot_move()


    def is_valid_movement(self, move: str):
        legal_moves = [str(x) for x in list(self.board.legal_moves)]
        if move in legal_moves:
            print("valid move\n")
            return True
        
        print("invalid move\n")
        return False

    def make_move(self, move: str):
        print(f"moving {move}")
        self.board.push_san(move)
         

    def make_bot_move(self):
        print("querrying bot move\n")
        self.stockfish.set_fen_position(self.board.fen())
        bot_move = self.stockfish.get_best_move()
        print("bot move: ", bot_move)
        self.board.push_san(bot_move)
        return bot_move

    def make_matrix(self):
        pgn = self.board.epd()
        foo = []
        pieces = pgn.split(" ", 1)[0]
        rows = pieces.split("/")
        for row in rows:
            foo2 = []
            for thing in row:
                if thing.isdigit():
                    for i in range(0, int(thing)):
                        foo2.append(0)
                else:
                    foo2.append(-1 if thing.islower() else 1)
            foo.append(foo2)
        return foo

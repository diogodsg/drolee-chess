import chess
from stockfish import Stockfish

class GameLogicModule:
    def __init__(self):
        self.board = chess.Board()
        self.stockfish = Stockfish(path="./stockfish/stockfish-ubuntu-x86-64-avx2")
        self.stockfish.set_fen_position(self.board.fen())

    def make_move(self, move: str):
        legal_moves = [str(x) for x in list(self.board.legal_moves)]
        if (move in legal_moves):
            print("legal move")
            self.board.push_san(move)
            # print(self.board)
            self.stockfish.set_fen_position(self.board.fen())
            bot_move = self.stockfish.get_best_move()
            print("bot move: ",bot_move)
            self.board.push_san(bot_move)

            # print(self.board)
            return bot_move
        else:
            print(f"illegal move {move}")
            return False
        
    def make_matrix(self): #type(board) == chess.Board()
        pgn = self.board.epd()
        foo = []  #Final board
        pieces = pgn.split(" ", 1)[0]
        rows = pieces.split("/")
        for row in rows:
            foo2 = []  #This is the row I make
            for thing in row:
                if thing.isdigit():
                    for i in range(0, int(thing)):
                        foo2.append(0)
                else:
                    foo2.append(-1 if thing.islower() else 1)
            foo.append(foo2)
        return foo
            
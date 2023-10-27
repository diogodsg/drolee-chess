import chess
from stockfish import Stockfish


class GameLogicModule:
    def __init__(self,  difficulty):
        self.board = chess.Board()
        self.stockfish = Stockfish(path="./stockfish/stockfish-ubuntu-x86-64-modern")
        self.stockfish.set_fen_position(self.board.fen())
        self.stockfish.set_skill_level(difficulty)

    def make_move(self, move: str):
        legal_moves = [str(x) for x in list(self.board.legal_moves)]
        if move in legal_moves:
            self.board.push_san(move)
            return True
        else:
            return False

    def get_bot_move(self):
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

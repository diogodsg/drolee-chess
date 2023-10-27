

from modules.game_runner import GameRunner
from modules.menu import Menu


class Application:
    def __init__(self):
        self.menu = Menu()

    def start(self):
        while True:
            color = self.menu.selectColor()
            difficulty = self.menu.selectDifficulty()
            has_time = self.menu.selectTime()

            self.menu.waitStart()

            game = GameRunner(color=color, difficulty=difficulty, has_time=has_time)
            game.run()

            self.menu.endGame()

            #joga tudo para cemiterio
            game.finish()
      
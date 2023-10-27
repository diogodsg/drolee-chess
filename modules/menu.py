import time
from modules.display import DisplayModule
from modules.buttons import ButtonsModule


class Menu:
    def __init__(self):
        self.buttons = ButtonsModule()

    def endGame(self):

        DisplayModule.display(0, "Jogo Finalizado!")
        DisplayModule.display(1, "ACABO")

        while True:
            if self.buttons.buttonPressed("queen"):
                DisplayModule.display(0, "Arrumando")
                DisplayModule.display(1, "Tabuleiro...")
                time.sleep(2)
                return 0

    def waitStart(self):

        DisplayModule.display(0, "Pressione Q")
        DisplayModule.display(1, "para iniciar")

        while True:
            if self.buttons.buttonPressed("queen"):
                DisplayModule.display(0, "JOGO")
                DisplayModule.display(1, "INICIADO!")
                time.sleep(2)
                return 0


    def selectColor(self):
        DisplayModule.display(0, "Selecione a cor")
        DisplayModule.display(1, "Q-Brancas R-Pretas")

        while True:
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

        while True:
            if self.buttons.buttonPressed("queen"):
                DisplayModule.display(0, "Dificuldade 5")
                DisplayModule.display(1, "Selecionada")
                time.sleep(2)
                return 5
            elif self.buttons.buttonPressed("bishop"):
                DisplayModule.display(0, "Dificuldade 10")
                DisplayModule.display(1, "Selecionada")
                time.sleep(2)
                return 10
            elif self.buttons.buttonPressed("knight"):
                DisplayModule.display(0, "Dificuldade 15")
                DisplayModule.display(1, "Selecionada")
                time.sleep(2)
                return 15
            elif self.buttons.buttonPressed("rook"):
                DisplayModule.display(0, "Dificuldade 20")
                DisplayModule.display(1, "Selecionada")
                time.sleep(2)
                return 20

    def selectTime(self):
        DisplayModule.display(0, "Selecione a o tempo")
        DisplayModule.display(1, "Q-Sem tempo R-10 min")

        while True:
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

        while True:
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

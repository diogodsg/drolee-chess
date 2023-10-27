from modules.motor import MotorModule

##tabuleiro:

#     8
#     7
#     6
#     5
#     4
#     3
#     2
#     1
#       w x   a b c d e f g h   y z



class PathModule:
    def __init__(self):
        self.motors = MotorModule()

        self.BOARD_CORNER_X = 7
        self.BOARD_CORNER_Y = 1 
        self.HALF_SQUARE = 1.5
        self.CEMITERY_GAP = 1

        self.motors.return_home()
        self.current_pos = (30, 0)##(self.BOARD_CORNER_X + 16*self.HALF_SQUARE + self.CEMITERY_GAP + , 0)

        self.board_positions = {}

        

        leters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'w', 'x', 'y', 'z']

        for x in range(0, 8):
            for y in range(0, 8):
                self.board_positions[leters[x] + str(y+1)] = (self.BOARD_CORNER_X + self.HALF_SQUARE + 2*self.HALF_SQUARE*x,
                                                              self.BOARD_CORNER_Y + self.HALF_SQUARE + 2*self.HALF_SQUARE*y)
        
        for x in range(0, 2):
            for y in range (0, 8):
                self.white_cemitery_positions[leters[8+x] + str(y+1)] = ()
                self.black_cemitery_positions[leters[10+x] + str(y+1)] = ()


        

    def calculate_path(self, destination):
        current_pos = (2, 5)  # mm
        origin = "e2"
        destination = "e4"

        path = []

        #move magnet to center of origin square
        path.append()
        
        #move piece to the bottom left corner of origin square
        path.append((-self.HALF_SQUARE, -self.HALF_SQUARE))

        #move piece to the bottom left corner of destination square
        path.append((self.board_positions[destination][0]-self.current_pos[0], 0)) # x axis
        path.append((0, self.board_positions[destination][1]-self.current_pos[1])) # y axis

        #move piece to the center of the destination square
        path.append((self.HALF_SQUARE, self.HALF_SQUARE))

        self.current_pos = self.board_positions[destination]

    def move_piece(self, movement: str):
        path = self.calculate_path(movement[:2], movement[2:4])
        self.motors.follow(path)
            
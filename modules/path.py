class PathModule:
    def __init__(self):
        self.HALF_SQUARE = 1.5
        self.CEMITERY_GAP = 1

    def calculate_path(self, current_pos, origin, destination):
        current_pos = (2, 5)  # mm
        origin = "e2"
        destination = "e4"

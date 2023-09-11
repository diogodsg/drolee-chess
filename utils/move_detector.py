table = ["a", "b", "c", "d","e","f", "g", "h"]

def detect_movement(m1, m2):
    move_from = ""
    move_to = ""
    for i in range(8):
        for j in range(8):
            if m1[i][j] != 0 and m2[i][j] == 0:
                move_from = f"{table[j]}{8-i}"
            if m1[i][j] != m2[i][j] and m2[i][j] != 0:
                move_to = f"{table[j]}{8-i}"
    if move_from and move_to:
        return move_from + move_to
import cv2
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt

class CameraModule:
    def __init__(
        self,img, top_left: Tuple[int, int], bottom_right: Tuple[int, int]
    ):
        self.img = img
        self.top_left = top_left
        self.bottom_right = bottom_right
        cv2.rectangle(self.img, self.top_left, self.bottom_right, (0, 255, 0), 1)
        self.square_width = int((self.bottom_right[0] - self.top_left[0]) / 8)
        self.square_height = int((self.bottom_right[1] - self.top_left[1]) / 8)
        self.threshold_x = int(self.square_width / 8)
        self.threshold_y = int(self.square_height / 8)
        self.invalid = False

    def get_square(self, x, y):
        x_start = self.top_left[0] + x * self.square_width + self.threshold_x
        x_end = self.top_left[0] + (x + 1) * self.square_width - self.threshold_x
        y_start = self.top_left[1] + y * self.square_height + self.threshold_y
        y_end = self.top_left[1] + (y + 1) * self.square_height - self.threshold_y

        rec_tl = (x_start, y_start)
        rec_br = (x_end, y_end)
        square = self.img[y_start:y_end, x_start:x_end]
        return square, rec_tl, rec_br

    def draw_squares(self):
        for i in range(8):
            for j in range(8):
                _, rec_tl, rec_br = self.get_square(i, j)
                cv2.rectangle(self.img, rec_tl, rec_br, (0, 0, 255), 1)
        return self.img

    def detect(self):
        self.invalid=False
        self.draw_squares()
        matrix = np.zeros((8, 8))

        for i in range(8):
            for j in range(8):
                matrix[j][i] = self.get_piece(i, j)
        return matrix

    def get_piece(self, x: int, y: int):
        roi, _, _ = self.get_square(x, y)

        square_white = (x + y) % 2 == 0

        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray_roi, (5, 5), 0)
        atg = cv2.adaptiveThreshold(
            blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
        average_intensity = cv2.mean(atg)[0]

        has_piece = False
        if average_intensity < 220:
            has_piece = True

        if square_white:
            _, tb = cv2.threshold(gray_roi, 100, 255, cv2.THRESH_BINARY)
        else:
            _, tb = cv2.threshold(gray_roi, 150, 255, cv2.THRESH_BINARY_INV)


        # fig, (ax1, ax2) = plt.subplots(1, 2)
        # ax1.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
        # ax2.imshow(cv2.cvtColor(tb, cv2.COLOR_BGR2RGB))

        average_intensity = cv2.mean(tb)[0]
        same_color = False
        color_thresh = 150 if square_white else 210
        
        if average_intensity > color_thresh:
            same_color = True
        if average_intensity < 40:
            self.invalid = True
        if not has_piece:
            return 0
 
        return self.get_piece_color(square_white, same_color)

    def get_piece_color(self, square_white: bool, same_color: bool):
        if square_white:
            if same_color:
                return 1
            return -1
        else:
            if same_color:
                return -1
            return 1
        
    def write(self, text):
        cv2.putText(self.img, text, (10,25), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)


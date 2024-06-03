from constants import *
import random


class Square:
    def __init__(self, pos):
        self.exp = 1
        self.pos = pos
        #value = 2^self.exp

    def draw_square(self, win):
        pygame.draw.rect(win, COLOR_2, (100 + PADDING + (PADDING + SQUARE_SIZE) * (self.pos % 4), 
                                        100 + PADDING + (PADDING + SQUARE_SIZE) * (self.pos // 4), SQUARE_SIZE, SQUARE_SIZE))
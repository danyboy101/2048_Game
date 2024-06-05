from constants import *
import random


class Square:
    def __init__(self, pos):
        self.exp = 1
        self.pos = pos
        self.col = self.pos % 4
        self.row = self.pos // 4
        self.x = 100 + PADDING + (PADDING + SQUARE_SIZE) * self.col
        self.y = 100 + PADDING + (PADDING + SQUARE_SIZE) * self.row
        self.exp = 2

    def draw_square(self, win):
        pygame.draw.rect(win, COLOR_2, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
        nb = NB_FONT.render(str(self.exp), 1, BLACK)
        win.blit(nb, (self.x + SQUARE_SIZE//2 - nb.get_rect()[2]//2, self.y + SQUARE_SIZE//2 - nb.get_rect()[3]//2))
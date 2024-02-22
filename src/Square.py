from constants import *
import random

class Square:
    def __init__(self, pos):
        self.pos = pos
        self.x = 100 + PADDING + (PADDING + SQUARE_SIZE) * (self.pos % 4)
        self.y = 100 + PADDING + (PADDING + SQUARE_SIZE) * (self.pos // 4)
        self.exp = 1
        self.value = str(2 ** self.exp)

    def draw_square(self, win):
        pygame.draw.rect(win, COLOR_2, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
        nb = NB_FONT.render(self.value, 1, BLACK)
        win.blit(nb, (self.x + SQUARE_SIZE//2 - nb.get_rect()[2]//2, self.y + SQUARE_SIZE//2 - nb.get_rect()[3]//2))
from constants import *
import random


class Square:
    def __init__(self, pos):
        self.exp = 1
        self.pos = pos
        self.col = self.pos % 4
        self.row = self.pos // 4
        self.x = self.getX()
        self.y = self.getY()
        self.exp = 2


    def getX(self):
        return 100 + PADDING + (PADDING + SQUARE_SIZE) * self.col


    def getY(self):
        return 100 + PADDING + (PADDING + SQUARE_SIZE) * self.row


    def updatePos(self):
        self.pos = 4 * self.row + self.col
        self.x = self.getX()
        self.y = self.getY()


    def draw_square(self, win):
        pygame.draw.rect(win, COLOR_2, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
        nb = NB_FONT.render(str(self.exp), 1, BLACK)
        win.blit(nb, (self.x + SQUARE_SIZE//2 - nb.get_rect()[2]//2, self.y + SQUARE_SIZE//2 - nb.get_rect()[3]//2))


    def moveRight(self):
        if self.col != 3:
            self.col += 1
            while self.x < self.getX():
                self.x += SPEED
            self.updatePos()
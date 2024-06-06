from constants import *
from Grid import *


class Square:
    grid = Grid()

    def __init__(self, pos):
        self.exp = 1
        self.pos = pos
        self.col = self.pos % 4
        self.row = self.pos // 4
        self.x = self.getX()
        self.y = self.getY()
        self.exp = 2
        Square.grid.add(self)


    def getX(self):
        return 100 + PADDING + (PADDING + SQUARE_SIZE) * self.col


    def getY(self):
        return 100 + PADDING + (PADDING + SQUARE_SIZE) * self.row


    def updatePos(self):
        self.pos = 4 * self.row + self.col
        self.x = self.getX()
        self.y = self.getY()
        Square.grid.updatePos(self)


    def draw_square(self, win):
        pygame.draw.rect(win, COLOR_2, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
        nb = NB_FONT.render(str(self.exp), 1, BLACK)
        win.blit(nb, (self.x + SQUARE_SIZE//2 - nb.get_rect()[2]//2, self.y + SQUARE_SIZE//2 - nb.get_rect()[3]//2))


    def canUp(self):
        return self.row != 0 and Square.grid.list[self.pos - 4] == 0

    
    def canDown(self):
        return self.row != 3 and Square.grid.list[self.pos + 4] == 0


    def canLeft(self):
        return self.col != 0 and Square.grid.list[self.pos - 1] == 0


    def canRight(self):
        return self.col != 3 and Square.grid.list[self.pos + 1] == 0


    def __str__(self):
        return "Sq" + str(self.pos)
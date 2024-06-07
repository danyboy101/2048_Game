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
        for n in range(self.row):
            if Square.grid.list[4*n + self.col] == 0:
                return True 
        return False

    
    def canDown(self):
        for n in range(self.row + 1, 4):
            if Square.grid.list[4*n + self.col] == 0:
                return True 
        return False


    def canLeft(self):
        for n in range(self.col):
            if Square.grid.list[self.pos + n - 3] == 0:
                return True 
        return False

    def canRight(self):
        for n in range(self.col + 1, 4):
            if Square.grid.list[self.pos - n + 2] == 0:
                return True 
        return False


    def __str__(self):
        return "Sq" + str(self.pos)
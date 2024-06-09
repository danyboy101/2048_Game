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
        Square.grid.updatePos(self)


    def draw_square(self, win):
        pygame.draw.rect(win, COLOR_2, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
        nb = NB_FONT.render(str(self.exp), 1, BLACK)
        win.blit(nb, (self.x + SQUARE_SIZE//2 - nb.get_rect()[2]//2, self.y + SQUARE_SIZE//2 - nb.get_rect()[3]//2))


    def moveUp(self):
        for row in range(self.row):
            if Square.grid.list[row*4 + self.col] == 0:
                self.row = row
                self.updatePos()
                return True
        return False

    
    def moveDown(self):
        for row in range(3, self.row, -1):
            if Square.grid.list[row*4 + self.col] == 0:
                self.row = row
                self.updatePos()
                return True
        return False
    

    def moveLeft(self):
        for col in range(self.col):
            if Square.grid.list[4*self.row + col] == 0:
                self.col = col
                self.updatePos()
                return True
        return False


    def moveRight(self):
        for col in range(3, self.col, -1):
            if Square.grid.list[4*self.row + col] == 0:
                self.col = col
                self.updatePos()
                return True
        return False
    

    def __str__(self):
        return "Sq" + str(self.pos)
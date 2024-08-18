from Square import *


class Grid:
    def __init__(self):
        self.cells = [[0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0]]
        self.tk_free = [[], []]
        self.dir = 0
        self.add(Square(5))


    def getTaken(self):
        taken = []
        free = list(range(16))
        for row in range(4):
            for col in range(4):
                cell = self.cells[row][col]
                if cell != 0:
                    taken.append(cell)
                    free.remove(4*row + col)
        return [taken, free]
    

    def moveUp(self):
        for square in self.tk_free[0]:
            if square.y > 100 + PADDING:  
                square.y -= SPEED
                square.moving = True
            else:
                square.moving = False
        if not self.is_moving():
            self.dir = 0


    def moveDown(self):
        for square in self.tk_free[0]:
            if square.y < 100 + PADDING + 3 * (PADDING + SQUARE_SIZE):  
                square.y += SPEED
                square.moving = True
            else:
                square.moving = False
        if not self.is_moving():
            self.dir = 0


    def moveLeft(self):
        for square in self.tk_free[0]:
            if square.x > 100 + PADDING:  
                square.x -= SPEED
                square.moving = True
            else:
                square.moving = False
        if not self.is_moving():
            self.dir = 0


    def moveRight(self):
        for square in self.tk_free[0]:
            if square.x < 100 + PADDING + 3 * (PADDING + SQUARE_SIZE):  
                square.x += SPEED
                square.moving = True
            else:
                square.moving = False
        if not self.is_moving():
            self.dir = 0
    

    def getLimUpper(self):
        pass

    def getLimLower(self):
        pass

    def getLimRight(self, pos):
        if pos % 4 == 3:
            return 100 + PADDING + 3 * (PADDING + SQUARE_SIZE)
        
    def getLimLeft(self):
        pass


    def getCell(self, x, y):
        pass
    

    def is_moving(self):
        return not all(not square.moving for square in self.tk_free[0])

        
    def add(self, square):
        self.cells[square.row][square.col] = square
        self.tk_free = self.getTaken()


    def remove(self, square):
        self.cells[square.row][square.col] = 0
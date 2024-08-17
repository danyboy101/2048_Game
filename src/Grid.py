from Square import *
import random

class Grid:
    def __init__(self):
        self.cells = [[0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0]]
        self.tk_free = self.getTaken()
        self.addRandom()
        self.addRandom()
        is_moving = False


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
    

    def addRandom(self):
        randPos = random.choice(self.tk_free[1])
        initValue = random.choices([2, 4], weights=[9, 1])
        self.add(Square(randPos, initValue[0]))
    

    def moving(self):
        self.is_moving = all(not square.moving for square in self.tk_free[0])

        
    def add(self, square):
        self.cells[square.row][square.col] = square
        self.tk_free = self.getTaken()


    def remove(self, square):
        self.cells[square.row][square.col] = 0
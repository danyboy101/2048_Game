from Square import *
import random

class Grid:
    def __init__(self):
        self.cells = [[0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0]]
        self.tk_free = [[], []]
        self.addRandom()
        self.addRandom()


    def getTaken(self):
        taken = []
        free = []
        for row in range(4):
            for col in range(4):
                cell = self.cells[row][col]
                if cell != 0:
                    taken.append(cell)
                else:
                    free.append(cell)
        return [taken, free]
    

    def addRandom(self):
        randPos = random.choice(self.tk_free[1])
        initValue = random.choice([2, 4], weights=[9, 1])
        self.add(Square(randPos, initValue[0]))

        
    def add(self, square):
        self.cells[square.row][square.col]


    def remove(self, square):
        self.cells[square.row][square.col] = 0
from Square import *


class Grid:
    def __init__(self):
        self.cells = [[0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0]]
        self.taken = []


    def getTaken(self):
        taken = []
        for row in range(4):
            for col in range(4):
                cell = self.cells[row][col]
                if cell != 0:
                    taken.append(cell)
        return taken

        
    def add(self, square):
        self.cells[square.row][square.col]


    def remove(self, square):
        self.cells[square.row][square.col] = 0
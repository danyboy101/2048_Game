from Square import *


class Grid:
    def __init__(self):
        self.cells = [[0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0]]
        self.taken = []
        is_moving = False
        self.add(Square(5))


    def getTaken(self):
        taken = []
        for row in range(4):
            for col in range(4):
                cell = self.cells[row][col]
                if cell != 0:
                    taken.append(cell)
        return taken
    

    def moving(self):
        self.is_moving = all(not square.moving for square in self.taken)

        
    def add(self, square):
        self.cells[square.row][square.col] = square
        self.taken = self.getTaken()


    def remove(self, square):
        self.cells[square.row][square.col] = 0
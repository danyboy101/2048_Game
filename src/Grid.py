class Grid:
    def __init__(self):
        self.cells = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        
    
    def __str__(self):
        return (f"{self.cells[0]}\n"
                f"{self.cells[1]}\n"
                f"{self.cells[2]}\n"
                f"{self.cells[3]}")
    

    def getSquareRow(self, square):
        return square.pos // 4
    

    def getSquareCol(self, square):
        return square.pos % 4


    def add(self, square):
        self.cells[self.getSquareRow(square)][self.getSquareCol(square)] = square

    
    def remove(self, square):
        temp = self.cells[self.getSquareRow(square)][self.getSquareCol(square)]
        self.cells[self.getSquareRow(square)][self.getSquareCol(square)] = 0
        return temp

    
    def updatePos(self, square):
        s = self.remove(square)
        s.updatePos()
        self.add(s)
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
                f"{self.cells[3]}\n")


    def add(self, square):
        self.cells[square.row][square.col] = square
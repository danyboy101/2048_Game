class Grid:
    def __init__(self):
        self.list = [0] * 16

    
    def add(self, sq):
        self.list[sq.pos] = sq

    
    def updatePos(self, sq):
        self.list[self.list.index(sq)] = 0
        self.add(sq)


    def __str__(self):
        string = ""
        for i in range(4):
            for j in range(4):
                sq = str(self.list[4*i + j])
                if j == 0:
                    string += "[" + sq + ", "
                elif j == 3:
                    string += sq + "]\n"
                else:
                    string += sq + ", "
        return string
from constants import *
from Grid import *

class Square:
    """
    Grid Diagram:
        
        [ 0 , 1 , 2 , 3  ]
        [ 4 , 5 , 6 , 7  ]
        [ 8 , 9 , 10, 11 ]
        [ 12, 13, 14, 15 ]

    """
    SPEED = 1
    grid = Grid()


    def __init__(self, win, pos):
        self.win = win
        self.pos = pos
        self.col = self.pos % 4
        self.row = self.pos // 4
        self.x = self.getX()
        self.y = self.getY()
        self.exp = 0
        self.update_exp()
        Square.grid.add(self)


    def getX(self):
        return 100 + PADDING + (PADDING + SQUARE_SIZE) * self.col


    def getY(self):
        return 100 + PADDING + (PADDING + SQUARE_SIZE) * self.row


    def update_exp(self):
        self.exp += 1
        self.value = str(2 ** self.exp)


    def updatePos(self):
        self.pos = 4 * self.row + self.col


    def draw_square(self):
        pygame.draw.rect(self.win, COLOR_2, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
        nb = NB_FONT.render(self.value, 1, BLACK)
        self.win.blit(nb, (self.x + SQUARE_SIZE//2 - nb.get_rect()[2]//2, self.y + SQUARE_SIZE//2 - nb.get_rect()[3]//2))


    def move_right(self):
        while (self.x <= self.getX()):
            self.x += Square.SPEED


    def move_left(self):
        while (self.x >= self.getX()):
            self.x -= Square.SPEED


    def move_up(self):
        while (self.y >= self.getY()):
            self.y -= Square.SPEED


    def move_down(self):
        while (self.y <= self.getY()):    
            self.y += Square.SPEED


    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.row > 0:
            self.row -= 1
            Square.grid.updatePos(self)
            self.move_up()

        elif keys[pygame.K_DOWN] and self.row < 3:
            self.row += 1
            Square.grid.updatePos(self)
            self.move_down()

        elif keys[pygame.K_RIGHT] and self.col < 3:
            self.col += 1
            Square.grid.updatePos(self)
            self.move_right()
            
        elif keys[pygame.K_LEFT] and self.col > 0:
            self.col -= 1
            Square.grid.updatePos(self)
            self.move_left()


    def getAdj(self):
        pass
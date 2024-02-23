from constants import *
import random

class Square:
    """
    Grid Diagram:
        
        [ 0 , 1 , 2 , 3  ]
        [ 4 , 5 , 6 , 7  ]
        [ 8 , 9 , 10, 11 ]
        [ 12, 13, 14, 15 ]

    """
    SPEED = 5

    def __init__(self, win, pos):
        self.win = win
        self.pos = pos
        self.x = 100 + PADDING + (PADDING + SQUARE_SIZE) * (self.pos % 4)
        self.y = 100 + PADDING + (PADDING + SQUARE_SIZE) * (self.pos // 4)
        self.exp = 0
        self.update_exp()

    def update_exp(self):
        self.exp += 1
        self.value = str(2 ** self.exp)

    def draw_square(self):
        pygame.draw.rect(self.win, COLOR_2, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))
        nb = NB_FONT.render(self.value, 1, BLACK)
        self.win.blit(nb, (self.x + SQUARE_SIZE//2 - nb.get_rect()[2]//2, self.y + SQUARE_SIZE//2 - nb.get_rect()[3]//2))

    def move_right(self):
        self.x += Square.SPEED
    
    def move_left(self):
        self.x -= Square.SPEED

    def move_up(self):
        self.y -= Square.SPEED

    def move_down(self):
        self.y += Square.SPEED

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()
        elif keys[pygame.K_RIGHT]:
            self.move_right()
        elif keys[pygame.K_LEFT]:
            self.move_left()

    def getAdj(self):
        pass
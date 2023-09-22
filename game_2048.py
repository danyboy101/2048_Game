import pygame
import random

pygame.init()

WIDTH, HEIGHT = 660, 660
SQUARE_SIZE = 100
PADDING = 10
GRID_SIZE = 4 * SQUARE_SIZE + 5 * PADDING
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BG_COLOR = "white"
DARK_GREY = (96, 96, 96)
LIGHT_GREY = (192, 192, 192)
COLOR_2 = (240, 234, 223)
COLOR_4 = (224, 206, 166)
COLOR_8 = (232, 147, 72)
COLOR_16 = (212, 112, 55)

pygame.display.set_caption("2048")

grid = []

for g in range(16):
    grid.append(g)

print(grid)

class Square:
    def __init__(self, pos):
        self.pos = pos
        grid.remove(self.pos)
        self.exp = 1
        #value = 2^self.exp

    def draw_square(self, win):
        pygame.draw.rect(win, COLOR_2, (100 + PADDING + (PADDING + SQUARE_SIZE) * (self.pos % 4), 
                                        100 + PADDING + (PADDING + SQUARE_SIZE) * (self.pos // 4), SQUARE_SIZE, SQUARE_SIZE))

def draw_board(win):
    win.fill(BG_COLOR)
    pygame.draw.rect(win, DARK_GREY, (100, 100, GRID_SIZE, GRID_SIZE))
    for n in range(4):
        for k in range(4):
            pygame.draw.rect(win, LIGHT_GREY, (100 + PADDING + (PADDING + SQUARE_SIZE) * n, 
                                               100 + PADDING + (PADDING + SQUARE_SIZE) * k, SQUARE_SIZE, SQUARE_SIZE))

def main():
    run = True
    pos = random.choice(grid)
    s_1 = Square(pos)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw_board(WIN)
        s_1.draw_square(WIN)

        pygame.display.update()

    pygame.quit()

main()
print(grid)

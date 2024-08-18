import pygame
from Grid import *

pygame.display.set_caption("2048")

def draw_board(win, grid):
    
    win.fill(WHITE)
    pygame.draw.rect(win, DARK_GREY, (100, 100, GRID_SIZE, GRID_SIZE))
    for n in range(4):
        for k in range(4):
            pygame.draw.rect(win, LIGHT_GREY, (100 + PADDING + (PADDING + SQUARE_SIZE) * n, 
                                               100 + PADDING + (PADDING + SQUARE_SIZE) * k, SQUARE_SIZE, SQUARE_SIZE))
    for square in grid.tk_free[0]:
        square.draw_square(win)

def main():
    run = True
    clock = pygame.time.Clock()
    grid = Grid()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw_board(WIN, grid)

        if pygame.KEYDOWN and grid.dir == 0:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                grid.dir = 1
            elif keys[pygame.K_DOWN]:
                grid.dir = 3
            elif keys[pygame.K_LEFT]:
                grid.dir = 4
            elif keys[pygame.K_RIGHT]:
                grid.dir = 2

        if grid.dir == 1:
            grid.moveUp()
        elif grid.dir == 2:
            grid.moveRight()
        elif grid.dir == 3:
            grid.moveDown()
        elif grid.dir == 4:
            grid.moveLeft()

        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main() 
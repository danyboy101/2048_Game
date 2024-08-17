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
    for square in grid.taken:
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

        if pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                for s in grid.taken:
                    s.y -= SPEED
            elif keys[pygame.K_DOWN]:
                for s in grid.taken:
                    s.y += SPEED
            elif keys[pygame.K_LEFT]:
                for s in grid.taken:
                    s.x -= SPEED
            elif keys[pygame.K_RIGHT]:
                for s in grid.taken:
                    s.x += SPEED

        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main() 
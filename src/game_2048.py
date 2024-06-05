import pygame
#import random

from Square import *
from constants import *

pygame.init()
pygame.display.set_caption("2048")

def draw_board(win, s):
    
    win.fill(WHITE)
    pygame.draw.rect(win, DARK_GREY, (100, 100, GRID_SIZE, GRID_SIZE))
    for n in range(4):
        for k in range(4):
            pygame.draw.rect(win, LIGHT_GREY, (100 + PADDING + (PADDING + SQUARE_SIZE) * n, 
                                               100 + PADDING + (PADDING + SQUARE_SIZE) * k, SQUARE_SIZE, SQUARE_SIZE))
    s.draw_square(win)

def main():
    run = True
    clock = pygame.time.Clock()
    s = Square(5)
    moving = False

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if pygame.KEYDOWN:

                keys = pygame.key.get_pressed()

                if keys[pygame.K_UP] and s.row != 0:
                    s.row -= 1
                elif keys[pygame.K_DOWN] and s.row != 3:
                    s.row += 1
                elif keys[pygame.K_LEFT] and s.col != 0:
                    s.col -= 1 
                elif keys[pygame.K_RIGHT] and s.col != 3:
                    s.col += 1

        draw_board(WIN, s)
        
        if s.y > s.getY():
            s.y -= SPEED
        elif s.y < s.getY():
            s.y += SPEED
        elif s.x > s.getX():
            s.x -= SPEED
        elif s.x < s.getX():
            s.x += SPEED
        else:
            s.updatePos()
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main() 
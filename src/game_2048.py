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

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw_board(WIN, s)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            s.y -= SPEED
            pygame.display.update()
        elif keys[pygame.K_DOWN]:
            s.y += SPEED
            pygame.display.update()
        elif keys[pygame.K_LEFT]:
            s.x -= SPEED
            pygame.display.update()
        elif keys[pygame.K_RIGHT]:
            s.x += SPEED
            pygame.display.update()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main() 
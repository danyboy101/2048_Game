import pygame

from Square import *

pygame.init()
pygame.display.set_caption("2048")


def draw_board(win, square):
    win.fill(BG_COLOR)
    pygame.draw.rect(win, DARK_GREY, (100, 100, GRID_SIZE, GRID_SIZE))
    for n in range(4):
        for k in range(4):
            pygame.draw.rect(win, LIGHT_GREY, (100 + PADDING + (PADDING + SQUARE_SIZE) * n, 
                    100 + PADDING + (PADDING + SQUARE_SIZE) * k, SQUARE_SIZE, SQUARE_SIZE))
    square.draw_square()


def main():
    run = True
    s = Square(WIN, 5)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw_board(WIN, s)
        if pygame.KEYDOWN:
            s.movement()
        
        pygame.display.update()

    print(Square.grid)
    pygame.quit()

if __name__ == "__main__":
    main() 
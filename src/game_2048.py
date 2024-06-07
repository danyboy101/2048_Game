from Square import *
import random


pygame.display.set_caption("2048")

def draw_board(win):
    
    win.fill(WHITE)
    pygame.draw.rect(win, DARK_GREY, (100, 100, GRID_SIZE, GRID_SIZE))
    for n in range(4):
        for k in range(4):
            pygame.draw.rect(win, LIGHT_GREY, (100 + PADDING + (PADDING + SQUARE_SIZE) * n, 
                                               100 + PADDING + (PADDING + SQUARE_SIZE) * k, SQUARE_SIZE, SQUARE_SIZE))
    for sq in Square.grid.list:
        if sq != 0:
            sq.draw_square(win)

def main():
    run = True
    clock = pygame.time.Clock()
    Square(5)
    Square(10)
    print(Square.grid)
    
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print(Square.grid)
                break

            if pygame.KEYDOWN:

                keys = pygame.key.get_pressed()

                for sq in Square.grid.list:
                    if sq != 0:
                        if keys[pygame.K_UP]:
                            while sq.canUp():
                                sq.row -= 1
                        elif keys[pygame.K_DOWN]:
                            while sq.canDown():
                                sq.row += 1
                        elif keys[pygame.K_LEFT]:
                            while sq.canLeft():
                                sq.col -= 1 
                        elif keys[pygame.K_RIGHT]:
                            while sq.canRight():
                                sq.col += 1

        draw_board(WIN)

        for sq in Square.grid.list:
            if sq != 0:
                if sq.y > sq.getY():
                    sq.y -= SPEED
                elif sq.y < sq.getY():
                    sq.y += SPEED
                elif sq.x > sq.getX():
                    sq.x -= SPEED
                elif sq.x < sq.getX():
                    sq.x += SPEED
                else:
                    sq.updatePos()
        
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main() 
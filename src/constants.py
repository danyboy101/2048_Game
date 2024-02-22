import pygame

pygame.init()

WIDTH, HEIGHT = 660, 660
SQUARE_SIZE = 100
PADDING = 10
GRID_SIZE = 4 * SQUARE_SIZE + 5 * PADDING
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT_SIZE = 40
NB_FONT = pygame.font.SysFont("comicsans", FONT_SIZE)

BG_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (96, 96, 96)
LIGHT_GREY = (192, 192, 192)
COLOR_2 = (240, 234, 223)
COLOR_4 = (224, 206, 166)
COLOR_8 = (232, 147, 72)
COLOR_16 = (212, 112, 55)
import pygame
from src.Game import Game

pygame.init()
GAME_NAME = "N.O.O.T.G.O.O.D. - Trying to Keep Planes Intact"
pygame.display.set_caption(GAME_NAME)

WINDOW_RESOLUTIONS = (720, 500)
WIDTH, HEIGHT = WINDOW_RESOLUTIONS
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window icon
pygame.display.set_icon(pygame.image.load("assets/images/game-icon.ico"))

if __name__ == "__main__":
	game = Game(SCREEN)
	game.start()

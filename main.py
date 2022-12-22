# import menus TODO
import utility
import yaml
from game import Game

"""
This is a visual simulation based on the data from the AYI facebook app that
Quartz wrote an article about in 2013. Due to the resurgence in popular, it
was brought to my attention and this is a visualizaiton of its long term behavior. 

"""


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
WIN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

WIN = False


if __name__ == "__main__":

    size = WIN_SIZE
    game = Game(size)

    game.start()

    while not WIN:
        game._keyControls()

        game._screen.fill("WHITE")

        game.move()
        game.speedDate()
        game.update()

        game._clock.tick(60)

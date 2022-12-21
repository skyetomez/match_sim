import sys
import pygame
from pygame.locals import *
from time import sleep
from random import Random

from playerhandler import PlayerHandler

# Screen constants
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

MID_Y = SCREEN_HEIGHT // 2
MID_X = SCREEN_WIDTH // 2

CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
WHITE = (255, 255, 255)


TESTING = True

# Probability constants
LOWER = 30.0
UPPER = 30.0


class Game(PlayerHandler):
    def __init__(self, size: tuple[int, int]) -> None:
        """Initialize screen, clock, player components"""
        self.WIN_STATE = False
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(size)
        self._screen.fill(WHITE)
        pygame.init()
        # -------- rect and player bookkeeping --------------
        super().__init__()
        self._dirtyRects: list[str] = list()

        # ----------------- initial drawings ----------------
        return None

    # --------------------- public methods -------------------

    def start(self) -> None:
        self._generatePlayers(10000, "A")

        tmp._screen.fill("WHITE")

        for _player in self._playerRectPool.values():

            center = (MID_X, MID_Y)

            surf, rect = _player[0], _player[1]
            rect.center = center

            self._screen.blit(surf, rect)
            print("surf", surf, "rect:", rect, "pos", center)

        pygame.display.flip()

        sleep(1)
        return None

    # -------------------- controllers -----------------------

    def _keyControls(self) -> None:
        """keys required to close window"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._clexit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._clexit()
        return None

    def _clexit(self):
        """close and exit"""
        pygame.quit()
        sys.exit()

    # ------------------ Game Logic ----------------------

    def move(self) -> None:
        """Move each character some amount between upper and lower wrap around screen"""
        for _id, _player in self._playerPool.items():

            delta_x, delta_y = self._movementamount()
            _player._xpos += delta_x
            _player._ypos += delta_y
            x, y = (
                _player._xpos % SCREEN_WIDTH,
                _player._ypos % SCREEN_HEIGHT,
            )

            new_position = tuple([x, y])

            surf, rect = self._playerRectPool[_id]
            rect = rect.move(new_position)

            rect.center = new_position

            self._screen.blit(surf, rect)
            print("surf", surf, "rect:", rect, "pos", new_position)
            self._dirtyRects.append(_id)

        return None

    def _checkCollision(self):
        # for each type check if they colliding/same spot
        pass

    def _speedDate(self):
        # if compatible roll die to see if date or not
        # if compatible leave screen as not in pool anymore.
        # else move
        pass

    def _checkWin(self):
        # if none on screen win end game
        pass

    # ------------------ Graphics ----------------------
    def _renderDirtyRects(self) -> None:
        # pass list of dirty rects
        # self._dirtyRects()
        # blit background over old location
        # background surface same size as old object
        # _move()
        # draw sprite at new location
        # pygame.display.update(_dirtyrecs)

        return None

    def update(self) -> None:
        # update screen.
        # self._screen.blit()
        # for surect in self._playerRectPool.values():
        #     surf, rect = surect
        #     self._screen.blit(surf, rect)

        return None

    # -------------- utility ------------------------
    def _movementamount(self) -> tuple[float, float]:
        prob_dist = Random()
        value = tuple(prob_dist.uniform(a=-LOWER, b=UPPER) for _ in range(2))
        return value


# Test behavior
if __name__ == "__main__":
    print("This is the game logics module")

    tmp = Game(size)

    tmp.start()

    while TESTING:
        tmp._keyControls()

        tmp._screen.fill("WHITE")

        tmp.move()

        pygame.display.flip()
        tmp._clock.tick(60)

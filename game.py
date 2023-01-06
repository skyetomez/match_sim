import sys
import pygame
from pygame.locals import *
from time import sleep
from random import Random
from collections import Counter
from playerhandler import PlayerHandler
from persons import Person


# Screen constants
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

MID_Y = SCREEN_HEIGHT // 2
MID_X = SCREEN_WIDTH // 2

CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
WHITE = (255, 255, 255)
PINK = (222, 49, 99)

TESTING = True

# Probability constants
UPPER = LOWER = 1.0
PROB_DIST = Random()


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
        self._collisions: list[tuple[str, str]] = list()
        self._lovelist: Counter = Counter()
        # ----------------- initial drawings ----------------
        return None

    # --------------------- public methods -------------------

    def start(self) -> None:
        self._generatePlayers(100, "A")
        self._generatePlayers(100, "B")
        self._generatePlayers(100, "C")
        self._generatePlayers(100, "D")

        self._screen.fill(WHITE)

        for _id, _player in self._playerRectPool.items():

            coord = self._initPositionRoll()

            self._playerPool[_id].position = coord

            rect_center = coord

            surf, rect = _player[0], _player[1]
            rect.center = rect_center

            self._screen.blit(surf, rect)

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
        print(self._lovelist)
        pygame.quit()
        sys.exit()

    # ------------------ Game Logic ----------------------

    def move(self) -> None:
        """Move each character some amount between upper and lower wrap around screen"""
        for _id, _player in self._playerRectPool.items():

            delta_x, delta_y = self._movementamount()  # move amonut

            x_old, y_old = self._playerPool[_id].position  # get old position
            x_old += delta_x  # incr x
            y_old += delta_y  # incr y
            new_coor = (x_old, y_old)  # init new position
            self._playerPool[_id].position = new_coor  # set new positoon

            _, rect = _player
            rect = rect.move(new_coor)
            rect.center = new_coor
            _player[-1] = rect  # overwrite old rect

        return None

    def _checkCollision(self):
        """Check if Rects are colliding and return list of collided rects"""
        for _id, _player in self._playerRectPool.items():
            surf, rect = _player
            for _idwall, _playerwall in self._playerRectPool.items():
                _wall, wallrect = _playerwall
                if rect != wallrect and rect.colliderect(wallrect):
                    # surf.fill(PINK)
                    # wall.fill(PINK)
                    # self._resmovePlayers([_id, _idwall])
                    collision_pair = tuple([_id, _idwall])
                    self._collisions.append(collision_pair)

    def speedDate(self) -> None:
        """ "Roll to see if the rects stay on the screen or leave the screen"""

        self._checkCollision()

        for collison_pair in set(self._collisions):
            _id, _idwall = collison_pair

            player1, player2 = self._playerPool[_id], self._playerPool[_idwall]
            probability = self._getProbabiity(player1, player2)

            answer = self._simulate(probability)

            if answer:
                surf, _ = self._playerRectPool[_id]
                wall, _ = self._playerRectPool[_idwall]
                surf.fill(PINK)
                wall.fill(PINK)
                self._collisions.remove(collison_pair)
                # add to dict and increase count
                pair = (
                    str(self._playerPool[_id]._type),
                    str(self._playerPool[_idwall]._type),
                )
                self._lovelist.update(pair)
                return None
            else:
                self._collisions.remove(collison_pair)
                return None

    def _checkWin(self):
        """If screen is empty, win, otherwise lose"""
        # if none on screen win end game
        pass

    # ------------------ Graphics ----------------------
    def update(self) -> None:
        """Flips dispaly buffer"""
        for p in self._playerRectPool.values():
            surf, rect = p
            self._screen.blit(surf, rect)
        pygame.display.flip()
        return None

    # -------------- utility ------------------------
    def _movementamount(self) -> tuple[float, float]:
        value = tuple([PROB_DIST.uniform(a=-LOWER, b=UPPER) for _ in range(2)])
        return value

    def _initPositionRoll(self):
        x_pool = PROB_DIST.randrange(0, SCREEN_WIDTH)
        y_pool = PROB_DIST.randrange(0, SCREEN_HEIGHT)
        return x_pool, y_pool

    def _getProbabiity(self, person1: Person, person2: Person) -> float:
        _type1, _type2 = person1._type, person2._type
        _sex1, _sex2 = person1._sex, person2._sex

        if _sex1 != _sex2:

            if _type1 != _type2:
                comp1, comp2 = _type2[4], _type1[4]
                print("comp1: ", comp1, "comp2", comp2)
                attr1, attr2 = f"_prob_{comp1}", f"_prob_{comp2}"
                print("attr1: ", attr1, "attr1", attr2)
                prob1, prob2 = getattr(person1, attr1), getattr(person2, attr2)
                print("prob1 : ", prob1, "prob2", prob2)

                return prob1 * prob2
            else:
                return 0.0
        else:
            return 0.0

    def _simulate(self, probability: float) -> bool:
        """simulate draw"""
        draw = PROB_DIST.uniform(0, 1)
        if draw <= probability:
            return True
        else:
            return False


# Test behavior
if __name__ == "__main__":
    print("This is the game logics module")

    tmp = Game(size)

    tmp.start()

    while TESTING:
        tmp._keyControls()

        tmp._screen.fill("WHITE")

        tmp.move()
        tmp.speedDate()
        tmp.update()

        tmp._clock.tick(60)

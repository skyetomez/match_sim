from persons import Person, TypeA, TypeB, TypeC, TypeD
from pygame import Surface

# make new characters

# keep track of characters

POINT_SIZE = (10, 10)

COLORKEY = {
    "TypeA": (255, 255, 0),
    "TypeB": (0, 0, 0),
    "TypeC": (200, 173, 127),
    "TypeD": (0, 0, 255),
}


class PlayerHandler(Person):
    __slots__ = ("_k", "_playerPool", "_playerRectPool")

    def __init__(self) -> None:
        self._k = 0
        self._playerPool: dict[str, Person] = dict()
        self._playerRectPool: dict[str, list] = dict()
        return None

    # ------------- dunder methods ----------------------
    def __len__(self) -> int:
        return self._k

    def __repr__(self) -> str:
        return "PlayerHandler Object"

    def __str__(self) -> str:
        return f"PlayerHandler: Total players{len(self)}"

    # -------------- player generateion and removal ---------------
    def _removePlayers(self, player_id: str | list[str]) -> None:
        """removes players from by id or from a list of ids"""
        if isinstance(player_id, list):
            for ele in player_id:
                if player_id in self._playerPool:
                    self._playerPool.pop(player_id)
                    self._k -= 1
        if self._validatePlayer(player_id):
            if player_id in self._playerPool:
                self._playerPool.pop(player_id)
                self._k -= 1
        self._destroyPlayerRect(player_id)

        return None

    def _generatePlayers(self, n: int, _type: str) -> dict[str, Person]:
        """generates unique players for the game"""
        players = dict()

        if not isinstance(_type, str):
            _type = str(_type).upper()

        if _type == "A":
            while len(players) != n:
                new = TypeA()
                new_id = new._id
                if not self._validatePlayer(new):
                    players.update({new_id: new})
                    self._k += 1

        elif _type == "B":
            while len(players) != n:
                new = TypeB()
                new_id = new._id
                if not self._validatePlayer(new):
                    players.update({new_id: new})
                    self._k += 1

        elif _type == "C":
            while len(players) != n:
                new = TypeC()
                new_id = new._id
                if not self._validatePlayer(new):
                    players.update({new_id: new})
                    self._k += 1

        elif _type == "D":
            while len(players) != n:
                new = TypeD()
                new_id = new._id
                if not self._validatePlayer(new):
                    players.update({new_id: new})
                    self._k += 1
        else:
            raise NotImplementedError

        self._playerPool.update(players)
        self._generatePlayerRects()
        return players

    # ------------------ graphics ----------------------

    def _generatePlayerRects(self) -> None:
        for _id, _player in self._playerPool.items():
            # center = tuple([_player._xpos, _player._ypos])
            tmpSurf = Surface(POINT_SIZE)
            tmpSurf.fill(COLORKEY[_player._type])
            tmpRect = tmpSurf.get_rect()
            self._playerRectPool.update({_id: [tmpSurf, tmpRect]})
        return None

    def _destroyPlayerRect(self, player: str | list[str]) -> None:
        if isinstance(player, list):
            for ele in player:
                self._playerRectPool.pop(ele)
        else:
            self._playerRectPool.pop(player)
        return None

    # -------------- utility functions ------------------

    def _validatePlayer(self, player: object | str) -> bool:
        """auxiliary function to check if player with this id has been created"""
        if player in self._playerPool:
            return True
        else:
            return False


if __name__ == "__main__":

    tmp = PlayerHandler()
    players = tmp._generatePlayers(3, "A")

    for n in tmp._playerPool:
        print(n)

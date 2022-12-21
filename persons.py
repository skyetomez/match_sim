import random
from abc import abstractmethod
from string import ascii_uppercase, digits


"""
Simplied to people choosing only their min or max preference based on the AYI data.

"""
# ----- constants ------
ID_LENGTH = 16
VALID_CHARS = ascii_uppercase + digits
classes = {"TypeA": "a", "TypeB": "b", "TypeC": "c", "TypeD": "d"}
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Person:
    """
    Base class for all persons class. Requires 5 variables.
    """

    __slots__ = (
        "_id",
        "_type",
        "_sex",
        "_ypos",
        "_xpos",
        "_status",
        "_prob_A",
        "_prob_B",
        "_prob_C",
        "_prob_D",
    )

    @abstractmethod
    def __init__(self) -> None:
        self._type = "Base"
        self._setup()
        return None

    """
    Dunder methods defined for:
    string      string representation
    class       class representation 
    hash        required for efficient storage in set and dict
    equality    required for comprable objects
    """
    # ------------------ dunder methods ---------------------

    def __repr__(self) -> str:
        if self._id == None:
            return self._type + "ID intializing"
        else:
            return f"{self._type[-1]}_{self._id}"

    def __str__(self) -> str:
        return f"{self._type[-1]}_{self._id}"

    def __hash__(self) -> int:
        return hash(self._id)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, type(self)):
            return NotImplemented
        else:
            return self._id == __o.id

    def __ne__(self, __o: object) -> bool:
        return not (self == __o)

    # ----------------- read only attributes --------------------

    @property
    def id(self) -> str:
        if self._id == None:
            id = list(map(str, self._id_generator))
            id = "".join(id)
            self._id = id
            return self._id
        else:
            return self._id

    @property
    def _id_generator(self):
        return [random.choice(VALID_CHARS) for _ in range(ID_LENGTH)]

    @property
    def sex(self) -> str:
        if self._sex == None:
            sexes = ["M", "F"]
            self._sex = random.choice(sexes)
            self._interactionprobability()
            return self._sex
        else:
            return self._sex

    # ---------------------- settable attributes --------------------

    @property
    def status(self) -> int:
        return self._status

    @status.setter
    def status(self, current: int) -> None:
        """set status to either 1 (alive) or 0 (dead)"""
        assert (
            current == 1 or current == 0
        ), "Status must be either 1 (alive) or 0 (dead)"
        self._status = current
        return None

    @property
    def position(self) -> tuple[float, float]:
        return (self._xpos, self._ypos)

    @position.setter
    def position(self, pos: tuple[float, float]) -> None:
        """set position of person object to expects a tuple"""
        self._xpos = pos[0]
        self._ypos = pos[1]
        return None

    # -----------set up and utility functions --------------------

    def _setup(self) -> None:
        """Made to make classes look prettier"""
        self._sex = None
        self._id = None
        self._xpos = 0.0 % SCREEN_WIDTH
        self._ypos = 0.0 % SCREEN_HEIGHT
        self._status = 1
        self.id
        self.sex
        self.status

    def _interactionprobability(self) -> None:
        """Utility to set row probabilities given gender"""
        if self._sex == "M":
            self._prob_A = 0.0
            self._prob_B = 0.0
            self._prob_C = 0.0
            self._prob_D = 0.0
        else:
            self._prob_A = 1.0
            self._prob_B = 1.0
            self._prob_C = 1.0
            self._prob_D = 1.0


class TypeA(Person):
    """
    Person of Type A with 2 sexes 2 statuses and associated probabilities.
    """

    def __init__(self) -> None:
        self._type = "TypeA"
        self._setup()
        return None


class TypeB(Person):
    """
    Person of Type B with 2 sexes 2 statuses and associated probabilities.
    """

    def __init__(self) -> None:
        self._type = "TypeB"
        self._setup()
        return None


class TypeC(Person):
    """
    Person of Type C with 2 sexes 2 statuses and associated probabilities.
    """

    def __init__(self) -> None:
        self._type = "TypeC"
        self._setup()
        return None


class TypeD(Person):
    """
    Person of Type D with 2 sexes 2 statuses and associated probabilities.
    """

    def __init__(self) -> None:
        self._type = "TypeD"
        self._setup()
        return None


# Test behavior
if __name__ == "__main__":
    print("This is the persons module")

    tmpA = TypeA()
    tmpB = TypeB()
    tmpC = TypeC()
    tmpD = TypeD()
    tmp = Person()

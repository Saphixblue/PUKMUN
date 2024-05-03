# level_1
from levels.level_interface import LevelInterface
from map import Map
from pukmun import Pukmun


class Level1(LevelInterface):
    def __init__(self, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DIMENSION_MAP, CELL_SIZE)
        self.pukmun = Pukmun([12, 12], CELL_SIZE)
        # self.fantomes =
        # Initialiser un tableau de Fantomes

    def draw_level_on_map(self):
        print("a")

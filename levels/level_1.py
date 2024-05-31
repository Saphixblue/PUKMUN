# level_1
from fantomes.fantome_fantome import FantomeFantome
from levels.level_interface import LevelInterface
from pukmun import Pukmun
from fantomes.fantome_interface import FantomeInterface
from fantomes.fantome_ivre import FantomeIvre


class Level1(LevelInterface):
    def __init__(self, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DIMENSION_MAP, CELL_SIZE)
        self.pukmun = Pukmun([12, 12], CELL_SIZE)

        self.fantomes = [FantomeFantome([self.fantomes_depart[0][0], self.fantomes_depart[0][1]], DIMENSION_MAP, CELL_SIZE)]
        # Initialiser un tableau de Fantomes, les ajouter avec leurs coordonnées de départ

    def draw_level_on_map(self):
        self.level_map.draw_rectangle_obstacle(12, 1, 1, 3)

        self.level_map.draw_rectangle_obstacle(2, 2, 2, 2)
        self.level_map.draw_rectangle_obstacle(14, 2, 4, 2)
        self.level_map.draw_rectangle_obstacle(21, 2, 2, 2)
        self.level_map.draw_rectangle_obstacle(7, 2, 4, 2)

        self.level_map.draw_angle_obstacle(1, 5, 3)
        self.level_map.draw_angle_obstacle(9, 5, 7, 4, 2, "bas")
        self.level_map.draw_angle_obstacle(21, 5, 3)

        self.level_map.draw_angle_obstacle(2, 7, 4, 4, 5)
        self.level_map.draw_angle_obstacle(7, 7, 4, 1, 2)
        self.level_map.draw_angle_obstacle(14, 7, 4, 4, 2)
        self.level_map.draw_angle_obstacle(19, 7, 4, 1, 5)

        self.level_map.draw_rectangle_obstacle(7, 8, 1, 3)
        self.level_map.draw_rectangle_obstacle(17, 8, 1, 3)

        self.level_map.draw_rectangle_obstacle(7, 12, 1, 2)
        self.level_map.draw_rectangle_obstacle(17, 12, 1, 2)

        self.level_map.draw_angle_obstacle(9, 13, 7, 4, 2, "bas")

        self.level_map.draw_angle_obstacle(2, 15, 3, 3, 2, "bas")
        self.level_map.draw_angle_obstacle(6, 15, 5)
        self.level_map.draw_angle_obstacle(14, 15, 5)
        self.level_map.draw_angle_obstacle(20, 15, 3, 1, 2, "bas")

        self.level_map.draw_angle_obstacle(1, 17, 2)
        self.level_map.draw_angle_obstacle(8, 17, 9, 5, 2, "bas")
        self.level_map.draw_angle_obstacle(22, 17, 2)

        self.level_map.draw_angle_obstacle(2, 19, 9, 5, 2)
        self.level_map.draw_angle_obstacle(14, 19, 9, 5, 2)

# level_5
from levels.level_interface import LevelInterface
from pukmun import Pukmun
from fantomes.fantome_interface import FantomeInterface
from fantomes.fantome_ivre import FantomeIvre
from fantomes.fantome_mafieux import FantomeMafieux
from fantomes.fantome_fantome import FantomeFantome


class Level5(LevelInterface):
    def __init__(self, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DIMENSION_MAP, CELL_SIZE)
        self.pukmun = Pukmun([12, 12], CELL_SIZE)
        # self.fantomes =
        # Initialiser un tableau de Fantomes, les ajouter avec leurs coordonnées de départ

    def draw_level_on_map(self):
        self.level_map.draw_angle_obstacle(1, 1, 6, 6, 2, "bas")
        self.level_map.draw_hole(8, 1, 1, 2)
        self.level_map.draw_angle_obstacle(9, 1, 2, 1, 1, "bas")
        self.level_map.draw_rectangle_obstacle(12, 1, 1, 3)
        self.level_map.draw_angle_obstacle(14, 1, 2, 2, 1, "bas")
        self.level_map.draw_hole(16, 1, 1, 2)
        self.level_map.draw_angle_obstacle(18, 1, 6, 1, 2, "bas")

        self.level_map.draw_hole(5, 2)
        self.level_map.draw_hole(19, 2)

        self.level_map.draw_angle_obstacle(2, 3, 3)
        self.level_map.draw_hole(11, 3)
        self.level_map.draw_hole(13, 3)
        self.level_map.draw_angle_obstacle(20, 3, 3)

        self.level_map.draw_hole(3, 4)
        self.level_map.draw_hole(8, 4)
        self.level_map.draw_angle_obstacle(9, 4, 3)
        self.level_map.draw_angle_obstacle(13, 4, 3)
        self.level_map.draw_hole(16, 4)
        self.level_map.draw_hole(21, 4)

        self.level_map.draw_angle_obstacle(2, 5, 3)
        self.level_map.draw_hole(11, 5)
        self.level_map.draw_rectangle_obstacle(12, 5, 1, 3)
        self.level_map.draw_hole(13, 5)
        self.level_map.draw_angle_obstacle(20, 5, 3)

        self.level_map.draw_hole(5, 6)
        self.level_map.draw_hole(8, 6, 1, 2)
        self.level_map.draw_hole(16, 6, 1, 2)
        self.level_map.draw_hole(19, 6)

        self.level_map.draw_angle_obstacle(1, 7, 6, 6, 2)
        self.level_map.draw_angle_obstacle(9, 7, 2, 1, 1)
        self.level_map.draw_angle_obstacle(14, 7, 2, 2, 1)
        self.level_map.draw_angle_obstacle(18, 7, 6, 1, 2)

        self.level_map.draw_rectangle_obstacle(7, 9, 1, 3)
        self.level_map.draw_rectangle_obstacle(17, 9, 1, 3)

        self.level_map.draw_angle_obstacle(7, 13, 11)

        self.level_map.draw_hole(12, 14, 1, 2)

        self.level_map.draw_angle_obstacle(2, 15, 6, 6, 1)
        self.level_map.draw_hole(9, 15)
        self.level_map.draw_rectangle_obstacle(10, 15, 1, 3)
        self.level_map.draw_hole(15, 15)
        self.level_map.draw_angle_obstacle(17, 15, 6, 1, 1)

        self.level_map.draw_angle_obstacle(1, 17, 3)
        self.level_map.draw_angle_obstacle(6, 17, 3)
        self.level_map.draw_angle_obstacle(11, 17, 4, 4, 2)
        self.level_map.draw_angle_obstacle(16, 17, 3)
        self.level_map.draw_angle_obstacle(21, 17, 3)

        self.level_map.draw_angle_obstacle(2, 19, 4, 4, 3)
        self.level_map.draw_rectangle_obstacle(7, 19, 1, 2)
        self.level_map.draw_angle_obstacle(9, 19, 3, 3, 1)
        self.level_map.draw_angle_obstacle(13, 19, 3, 1, 1)
        self.level_map.draw_rectangle_obstacle(17, 19, 1, 2)
        self.level_map.draw_angle_obstacle(19, 19, 4, 1, 3)

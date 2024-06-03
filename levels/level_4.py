# level_4
from levels.level_interface import LevelInterface
from pukmun import Pukmun
from fantomes.fantome_interface import FantomeInterface
from fantomes.fantome_ivre import FantomeIvre
from fantomes.fantome_mafieux import FantomeMafieux
from fantomes.fantome_fantome import FantomeFantome


class Level4(LevelInterface):
    def __init__(self, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DIMENSION_MAP, CELL_SIZE)
        self.pukmun = Pukmun([12, 12], CELL_SIZE)
        self.fantomes = [
            FantomeFantome([self.fantomes_depart[0][0], self.fantomes_depart[0][1]], DIMENSION_MAP, CELL_SIZE),
            FantomeFantome([self.fantomes_depart[1][0], self.fantomes_depart[1][1]], DIMENSION_MAP, CELL_SIZE),
            FantomeFantome([self.fantomes_depart[2][0], self.fantomes_depart[2][1]], DIMENSION_MAP, CELL_SIZE),
            FantomeFantome([self.fantomes_depart[3][0], self.fantomes_depart[3][1]], DIMENSION_MAP, CELL_SIZE)]

        self.fantomes[2].compteur_sortie = 4
        self.fantomes[3].compteur_sortie = 7

        self.fantomes[2].controle = None
        self.fantomes[2].action = None

        self.fantomes[3].controle = None
        self.fantomes[3].action = None

    def draw_level_on_map(self):
        self.level_map.draw_hole(11, 1, 3)

        self.level_map.draw_angle_obstacle(2, 2, 4, 1, 3, "bas")
        self.level_map.draw_angle_obstacle(7, 2, 3, 1, 3, "bas")
        self.level_map.draw_angle_obstacle(15, 2, 3, 3, 3, "bas")
        self.level_map.draw_angle_obstacle(19, 2, 4, 4, 3, "bas")

        self.level_map.draw_hole(3, 3)
        self.level_map.draw_angle_obstacle(11, 3, 3, 2, 2, "bas")
        self.level_map.draw_hole(21, 3)

        self.level_map.draw_angle_obstacle(4, 5, 2, 2, 1)
        self.level_map.draw_angle_obstacle(9, 5, 2, 1, 1)
        self.level_map.draw_angle_obstacle(14, 5, 2, 2, 1)
        self.level_map.draw_angle_obstacle(19, 5, 2, 1, 1)

        self.level_map.draw_angle_obstacle(2, 7, 3)
        self.level_map.draw_angle_obstacle(6, 7, 3, 2, 4, "bas")
        self.level_map.draw_angle_obstacle(10, 7, 2)
        self.level_map.draw_angle_obstacle(13, 7, 2)
        self.level_map.draw_angle_obstacle(16, 7, 3, 2, 4, "bas")
        self.level_map.draw_angle_obstacle(20, 7, 3)

        self.level_map.draw_angle_obstacle(10, 13, 5, 3, 3, "bas")

        self.level_map.draw_hole(1, 14)
        self.level_map.draw_angle_obstacle(5, 14, 2, 2, 1)
        self.level_map.draw_angle_obstacle(18, 14, 2, 1, 1)
        self.level_map.draw_hole(23, 14)

        self.level_map.draw_angle_obstacle(10, 15, 1)
        self.level_map.draw_angle_obstacle(14, 15, 1)

        self.level_map.draw_angle_obstacle(2, 16, 3, 2, 1)
        self.level_map.draw_angle_obstacle(6, 16, 3, 3, 3)
        self.level_map.draw_angle_obstacle(16, 16, 3, 1, 3)
        self.level_map.draw_angle_obstacle(20, 16, 3, 2, 1)

        self.level_map.draw_angle_obstacle(14, 17, 1)

        self.level_map.draw_angle_obstacle(2, 18, 3, 1, 1, "bas")
        self.level_map.draw_angle_obstacle(6, 18, 3, 3, 1, "bas")
        self.level_map.draw_angle_obstacle(10, 18, 5, 1, 1)
        self.level_map.draw_angle_obstacle(16, 18, 3, 1, 1, "bas")
        self.level_map.draw_angle_obstacle(20, 18, 3, 3, 1, "bas")

        self.level_map.draw_hole(4, 20, 3)
        self.level_map.draw_hole(10, 20, 5)
        self.level_map.draw_hole(18, 20, 3)

        # Gros grailles
        self.level_map.map_data[4][4] = 1
        self.level_map.map_data[20][4] = 1
        self.level_map.map_data[1][18] = 1
        self.level_map.map_data[23][18] = 1

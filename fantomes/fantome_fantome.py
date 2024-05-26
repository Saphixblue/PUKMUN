# fantome_fantome.py
from fantomes.fantome_interface import FantomeInterface

# Le fantôme fantôme se déplace lentement de case en case en ignorant les obstacles.
# Il emprunte le chemin le plus court vers PUKMUN
# Lorsqu'il est affaibli, il redevient tangible et fuit PUKMUN dans le labyrinthe.
# Si PUKMUN le mange, celui-ci obtient la faculté de passer à travers les obstacles pendant un moment
# Mort, il rejoint le pit et se reforme



class FantomeFantome(FantomeInterface):
    def __init__(self, DEPART, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DEPART, DIMENSION_MAP, CELL_SIZE)

        # TODO: Importer tous les sprites

        # TODO: Update le sprite
        # self.sprite

        # TODO: Calibrer la collision box
        # self.collision_box

    # TODO: Override toutes les fonctions de l'interface

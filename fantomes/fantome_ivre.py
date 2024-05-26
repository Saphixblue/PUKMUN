# fantome_ivre.py
from fantomes.fantome_interface import FantomeInterface

# Le fantôme ivre se déplace aléatoirement dans le labyrinthe. (Comment exactement ? Peut-il revenir sur ses pas ? Si oui, quand ?)

# Lorsqu'il voit PUKMUN, il lui fonce dessus à pleine vitesse.
# S'il ne tue pas PUKMUN, il continue sa charge jusqu'à rencontrer un obstacle.
# Il la reprend s'il voit PUKMUN, sinon il reprendra ses déplacements aléatoires

# Lorsqu'il est affaibli, il ne change pas son comportement.
# Le manger donnera le statut "ivre" à PUKMUN (géré dans game), ce qui inverse ses contrôles (géré dans pukmun)

# Pour l'éliminer, passer dessus lorsqu'il est affaibli

# Mort, il rejoint le pit et se reforme


class FantomeIvre(FantomeInterface):
    def __init__(self, DEPART, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DEPART, DIMENSION_MAP, CELL_SIZE)

        # TODO: Importer tous les sprites

        # TODO: Update le sprite
        # self.sprite

        # TODO: Calibrer la collision box
        # self.collision_box

        self.rage = 0
        self.vitesse_rage = 4 * self.vitesse

    # TODO: Override toutes les méthodes de l'interface

    # TODO
    # Détaille le comportement du fantôme quand il est enragé
    def comportement_rage(self, game_map):
        print("Comportement rage")

    # TODO (Doit sûrement être basculée dans game)
    # Renvoie True si PUKMUN est sur la même ligne ou colonne sans obstacle entre eux
    def voit_pukmun(self, game_map):
        print("Voit PUKMUN")

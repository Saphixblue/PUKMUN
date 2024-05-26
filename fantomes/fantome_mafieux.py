# fantome_mafieux.py
from fantomes.fantome_interface import FantomeInterface

# Le fantôme mafieux tente de contourner PUKMUN pour lui tirer dessus.
# Il ne revient pas sur ses pas. S'il emprunte un chemin, c'est jusqu'à-ce qu'il puisse tourner ou rencontre un obstacle.

# Lorsqu'il voit PUKMUN, il s'immobilise, se tourne vers PUKMUN et tire une balle.
# Il reste immobile jusqu'à-ce que la balle atteigne PUKMUN
# Si PUKMUN renvoie la balle avec un bouclier classique, le fantôme mafieux reste immobile et esquive la balle.
# Si PUKMUN la renvoie avec un bouclier powered, la balle devient dorée et le fantôme mafieux part dans la direction opposée jusqu'à pouvoir échapper au tir.
# Si le fantôme mafieux est touché par la balle, il meurt.
# Un tir est le seul moment où le fantôme mafieux peut changer de direction au milieu d'une ligne

# L'affaiblir n'a aucun effet sur lui

# Si PUKMUN réussit à atteindre le fantôme mafieux, celui-ci l'esquive pour ne pas se salir les mains directement

# Mort, il revient au pit et se reforme


class FantomeMafieux(FantomeInterface):
    def __init__(self, DEPART, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DEPART, DIMENSION_MAP, CELL_SIZE)

        # TODO: Importer tous les sprites

        # TODO: Update le sprite
        # self.sprite

        # TODO: Calibrer la collision box
        # self.collision_box

        # Définit si le fantôme mafieux est en train de tirer
        self.tire = 0

        self.coordonnees_balle = self.coordonnees_pixels

        self.orientation_sprite_balle = self.orientation_sprite
        self.direction_sprite_balle = self.direction_sprite

        # TODO: Importer tous les sprites de la balle

        # TODO: Update le sprite de la balle
        # self.sprite_balle

        self.vitesse_balle = self.vitesse * 5

        self.golden_bullet = 0

    # TODO: Override toutes les méthodes de l'interface

    # TODO
    # Définit le comportement du fantôme mafieux et de sa balle lors d'un tir
    def tir(self):
        print("Tir")

    # TODO
    # Déplace la balle en fonction de sa direction et son orientation
    def balle_deplacement(self, game_map):
        print("Balle déplacement")

    # TODO
    # Permet à la balle de naviger d'un bord à l'autre de l'écran en sortant de la map
    def balle_update_coordonnees(self, game_map):
        print("Balle update coordonnées")

    # TODO
    # Update le sprite de la balle en fonction de son état, son orientation et sa direction
    def balle_update_sprite(self):
        print("Balle update coordonnées")

    # TODO
    # Met à jour la direction et l'orientation de la balle lorsqu'elle est renvoyée par un bouclier de PUKMUN
    def renvoi_balle(self, game_map):
        print("Renvoi balle")

    # TODO (Doit sûrement être basculée dans game)
    # Renvoie True si PUKMUN est sur la même ligne ou colonne sans obstacle entre eux
    def voit_pukmun(self, game_map):
        print("Voit PUKMUN")

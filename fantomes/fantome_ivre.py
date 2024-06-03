# fantome_ivre.py
from fantomes.fantome_interface import FantomeInterface
from sprite_handler import SpriteHandler
import random


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

        sprite_handler = SpriteHandler(self.CELL_SIZE)

        self.fantome_ivre_DL_image = sprite_handler.fantome_ivre_DL_image()
        self.fantome_ivre_DR_image = sprite_handler.fantome_ivre_DR_image()
        self.fantome_ivre_L_image = sprite_handler.fantome_ivre_L_image()
        self.fantome_ivre_R_image = sprite_handler.fantome_ivre_R_image()
        self.fantome_ivre_UL_image = sprite_handler.fantome_ivre_UL_image()
        self.fantome_ivre_UR_image = sprite_handler.fantome_ivre_UR_image()

        self.fantome_ivre_nrv_DL_image = sprite_handler.fantome_ivre_nrv_DL_image()
        self.fantome_ivre_nrv_DR_image = sprite_handler.fantome_ivre_nrv_DR_image()
        self.fantome_ivre_nrv_L_image = sprite_handler.fantome_ivre_nrv_L_image()
        self.fantome_ivre_nrv_R_image = sprite_handler.fantome_ivre_nrv_R_image()
        self.fantome_ivre_nrv_UL_image = sprite_handler.fantome_ivre_nrv_UL_image()
        self.fantome_ivre_nrv_UR_image = sprite_handler.fantome_ivre_nrv_UR_image()

        self.fantome_ivre_weak_blue_L_image = sprite_handler.fantome_ivre_weak_blue_L_image()
        self.fantome_ivre_weak_blue_R_image = sprite_handler.fantome_ivre_weak_blue_R_image()
        self.fantome_ivre_weak_white_L_image = sprite_handler.fantome_ivre_weak_white_L_image()
        self.fantome_ivre_weak_white_R_image = sprite_handler.fantome_ivre_weak_white_R_image()

        self.fantome_ivre_mort_DL_image = sprite_handler.fantome_ivre_mort_DL_image()
        self.fantome_ivre_mort_DR_image = sprite_handler.fantome_ivre_mort_DR_image()
        self.fantome_ivre_mort_L_image = sprite_handler.fantome_ivre_mort_L_image()
        self.fantome_ivre_mort_R_image = sprite_handler.fantome_ivre_mort_R_image()
        self.fantome_ivre_mort_UL_image = sprite_handler.fantome_ivre_mort_UL_image()
        self.fantome_ivre_mort_UR_image = sprite_handler.fantome_ivre_mort_UR_image()

        self.sprite = self.fantome_ivre_DL_image

        # TODO: Calibrer la collision box
        # self.collision_box

        self.rage = 0
        self.vitesse_rage = 2 * self.vitesse

    # TODO: Override toutes les méthodes de l'interface

    def fantome_update_action(self, game_map):
        if self.fantome_check_case():
            if self.weak == 0:
                if self.dead == 0:
                    self.fantome_deplacement(game_map)
                else:
                    self.fantome_deplacement_dead(game_map)
            elif self.weak == 1:
                self.fantome_deplacement_weak(game_map)

        self.fantome_update_coordonnees_pixels(game_map)
        self.fantome_update_case()

    def fantome_update_deplacement(self, game_map):
        if self.action == "LEFT":
            self.fantome_gauche(game_map)
        elif self.action == "RIGHT":
            self.fantome_droite(game_map)
        elif self.action == "DOWN":
            self.fantome_bas(game_map)
        elif self.action == "UP":
            self.fantome_haut(game_map)

    def fantome_deplacement(self, game_map):
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0] and self.coordonnees_cases[1] * self.CELL_SIZE == self.coordonnees_pixels[1]:
            if self.controle == "LEFT":
                self.action = "LEFT"
            elif self.controle == "RIGHT":
                self.action = "RIGHT"
            elif self.controle == "UP":
                self.action = "UP"
            elif self.controle == "DOWN":
                self.action = "DOWN"

    def fantome_deplacement_weak(self, game_map):
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0] and self.coordonnees_cases[1] * self.CELL_SIZE == self.coordonnees_pixels[1]:
            self.fantome_deplacement(game_map)

    def fantome_deplacement_dead(self, game_map):
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0] and self.coordonnees_cases[1] * self.CELL_SIZE == self.coordonnees_pixels[1]:
            if self.controle == "LEFT":
                if not self.fantome_check_collision_obstacle_left(game_map):
                    self.action = "LEFT"
                else:
                    self.controle = "STOP"
            elif self.controle == "RIGHT":
                if not self.fantome_check_collision_obstacle_right(game_map):
                    self.action = "RIGHT"
                else:
                    self.controle = "STOP"
            elif self.controle == "UP":
                if not self.fantome_check_collision_obstacle_up(game_map):
                    self.action = "UP"
                else:
                    self.controle = "STOP"
            elif self.controle == "DOWN":
                if not self.fantome_check_collision_obstacle_down(game_map):
                    self.action = "DOWN"
                else:
                    self.controle = "STOP"

    def fantome_check_case(self):
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0] and self.coordonnees_cases[1] * self.CELL_SIZE == self.coordonnees_pixels[1]:
            return True
        return False

    def fantome_check_collision_obstacle_left(self, game_map):
        next_x = self.coordonnees_cases[0] - 1 if self.coordonnees_cases[0] != 0 else game_map.DIMENSION_MAP[0] - 1
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[next_x][self.coordonnees_cases[1]] == 3:
                return True
        return False

    def fantome_check_collision_obstacle_right(self, game_map):
        next_x = self.coordonnees_cases[0] + 1 if self.coordonnees_cases[0] != game_map.DIMENSION_MAP[0] - 1 else 0
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[next_x][self.coordonnees_cases[1]] == 3:
                return True
        return False

    def fantome_check_collision_obstacle_up(self, game_map):
        next_y = self.coordonnees_cases[1] - 1 if self.coordonnees_cases[1] != 0 else game_map.DIMENSION_MAP[1] - 1
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[self.coordonnees_cases[0]][next_y] == 3:
                return True
        return False

    def fantome_check_collision_obstacle_down(self, game_map):
        next_y = self.coordonnees_cases[1] + 1 if self.coordonnees_cases[1] != game_map.DIMENSION_MAP[1] - 1 else 0
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[self.coordonnees_cases[0]][next_y] == 3 or \
                    (self.dead == 0 and game_map.map_data[self.coordonnees_cases[0]][next_y] == 5):
                return True
        return False

    def fantome_gauche(self, game_map):
        self.coordonnees_pixels = [self.coordonnees_pixels[0] - self.vitesse, self.coordonnees_pixels[1]]
        self.direction_sprite = "LEFT"
        self.orientation_sprite = "LEFT"
        self.fantome_update_case()

    def fantome_droite(self, game_map):
        self.coordonnees_pixels = [self.coordonnees_pixels[0] + self.vitesse, self.coordonnees_pixels[1]]
        self.direction_sprite = "RIGHT"
        self.orientation_sprite = "RIGHT"
        self.fantome_update_case()

    def fantome_haut(self, game_map):
        self.coordonnees_pixels = [self.coordonnees_pixels[0], self.coordonnees_pixels[1] - self.vitesse]
        self.direction_sprite = "UP"
        self.fantome_update_case()

    def fantome_bas(self, game_map):
        self.coordonnees_pixels = [self.coordonnees_pixels[0], self.coordonnees_pixels[1] + self.vitesse]
        self.direction_sprite = "DOWN"
        self.fantome_update_case()

    def fantome_update_case(self):
        if self.coordonnees_pixels[0] % self.CELL_SIZE == 0:
            self.coordonnees_cases[0] = int(self.coordonnees_pixels[0]) // self.CELL_SIZE
        if self.coordonnees_pixels[1] % self.CELL_SIZE == 0:
            self.coordonnees_cases[1] = int(self.coordonnees_pixels[1]) // self.CELL_SIZE

    def fantome_update_coordonnees_pixels(self, game_map):
        if self.coordonnees_pixels[0] < 0:
            self.coordonnees_pixels[0] = (game_map.DIMENSION_MAP[0] - 1) * self.CELL_SIZE + self.vitesse
        elif self.coordonnees_pixels[0] > (game_map.DIMENSION_MAP[0] - 1) * self.CELL_SIZE:
            self.coordonnees_pixels[0] = 0 - self.vitesse

        if self.coordonnees_pixels[1] < 0:
            self.coordonnees_pixels[1] = (game_map.DIMENSION_MAP[1] - 1) * self.CELL_SIZE + self.vitesse
        elif self.coordonnees_pixels[1] > (game_map.DIMENSION_MAP[1] - 1) * self.CELL_SIZE:
            self.coordonnees_pixels[1] = 0 - self.vitesse

    def fantome_update_sprite(self, frame, compteur):
        if self.weak == 0:
            if self.dead == 0:
                if self.rage == 0:
                    if self.direction_sprite == "LEFT":
                        self.sprite = self.fantome_ivre_L_image
                    elif self.direction_sprite == "RIGHT":
                        self.sprite = self.fantome_ivre_R_image
                    elif self.direction_sprite == "UP":
                        if self.orientation_sprite == "LEFT":
                            self.sprite = self.fantome_ivre_UL_image
                        elif self.orientation_sprite == "RIGHT":
                            self.sprite = self.fantome_ivre_UR_image
                    elif self.direction_sprite == "DOWN":
                        if self.orientation_sprite == "LEFT":
                            self.sprite = self.fantome_ivre_DL_image
                        elif self.orientation_sprite == "RIGHT":
                            self.sprite = self.fantome_ivre_DR_image
                if self.rage == 1:
                    if self.direction_sprite == "LEFT":
                        self.sprite = self.fantome_ivre_nrv_L_image
                    elif self.direction_sprite == "RIGHT":
                        self.sprite = self.fantome_ivre_nrv_R_image
                    elif self.direction_sprite == "UP":
                        if self.orientation_sprite == "LEFT":
                            self.sprite = self.fantome_ivre_nrv_UL_image
                        elif self.orientation_sprite == "RIGHT":
                            self.sprite = self.fantome_ivre_nrv_UR_image
                    elif self.direction_sprite == "DOWN":
                        if self.orientation_sprite == "LEFT":
                            self.sprite = self.fantome_ivre_nrv_DL_image
                        elif self.orientation_sprite == "RIGHT":
                            self.sprite = self.fantome_ivre_nrv_DR_image
            elif self.dead == 1:
                if self.direction_sprite == "LEFT":
                    self.sprite = self.fantome_ivre_mort_L_image
                elif self.direction_sprite == "RIGHT":
                    self.sprite = self.fantome_ivre_mort_R_image
                elif self.direction_sprite == "UP":
                    if self.orientation_sprite == "LEFT":
                        self.sprite = self.fantome_ivre_mort_UL_image
                    elif self.orientation_sprite == "RIGHT":
                        self.sprite = self.fantome_ivre_mort_UR_image
                elif self.direction_sprite == "DOWN":
                    if self.orientation_sprite == "LEFT":
                        self.sprite = self.fantome_ivre_mort_DL_image
                    elif self.orientation_sprite == "RIGHT":
                        self.sprite = self.fantome_ivre_mort_DR_image
        elif self.weak == 1:
            if self.orientation_sprite == "LEFT":
                if compteur > 2:
                    # 2 dernières secondes du compteur = clignote
                    self.sprite = self.fantome_ivre_weak_blue_L_image
                else:
                    if 0 <= frame < 30:
                        self.sprite = self.fantome_ivre_weak_blue_L_image
                    else:
                        self.sprite = self.fantome_ivre_weak_white_L_image
            elif self.orientation_sprite == "RIGHT":
                if compteur > 2:
                    # 2 dernières secondes du compteur = clignote
                    self.sprite = self.fantome_ivre_weak_blue_R_image
                else:
                    if 0 <= frame < 30:
                        self.sprite = self.fantome_ivre_weak_blue_R_image
                    else:
                        self.sprite = self.fantome_ivre_weak_white_R_image

    def fantome_comportement(self, game_map, pukmun_coordonnees_cases):
        if self.dead == 0:
            if self.rage == 0:
                if self.weak == 1:
                    self.vitesse = self.vitesse_weak
                else:
                    self.vitesse = self.vitesse_vivant
                x_diff = self.coordonnees_cases[0] - pukmun_coordonnees_cases[0]
                y_diff = self.coordonnees_cases[1] - pukmun_coordonnees_cases[1]

                if self.voit_pukmun(game_map, pukmun_coordonnees_cases):
                    if x_diff == 0:  # Pukmun est sur la colonne
                        if y_diff < 0: # Pukmun est en bas
                            if not self.fantome_check_collision_obstacle_down(game_map):
                                self.rage = 1
                                self.controle = "DOWN"
                            else:
                                rage = 0
                        if y_diff > 0:  # Pukmun est en haut
                            if not self.fantome_check_collision_obstacle_up(game_map):
                                self.rage = 1
                                self.controle = "UP"
                            else:
                                self.rage = 0
                    if y_diff == 0:  # Pukmun est sur la ligne
                        if x_diff < 0: # Pukmun est à droite
                            if not self.fantome_check_collision_obstacle_right(game_map):
                                self.rage = 1
                                self.controle = "RIGHT"
                            else:
                                self.rage = 0
                        if x_diff > 0:  # Pukmun est à gauche
                            if not self.fantome_check_collision_obstacle_left(game_map):
                                self.rage = 1
                                self.controle = "LEFT"
                            else:
                                self.rage = 0
                else:
                    if self.action != "STOP":
                        inverse_action_prob = 0.05
                    else:
                        inverse_action_prob = 0

                    if self.fantome_check_collision_obstacle_up(game_map):
                        up_prob = 0
                    else:
                        up_prob = 0.2

                    if self.fantome_check_collision_obstacle_down(game_map):
                        down_prob = 0
                    else:
                        down_prob = 0.2

                    if self.fantome_check_collision_obstacle_left(game_map):
                        left_prob = 0
                    else:
                        left_prob = 0.2

                    if self.fantome_check_collision_obstacle_right(game_map):
                        right_prob = 0
                    else:
                        right_prob = 0.2

                    stop_prob = 0.05

                    prob_total = up_prob + down_prob + left_prob + right_prob + stop_prob + inverse_action_prob

                    # Normalisation des probabilités pour qu'elles totalisent 1
                    up_prob /= prob_total
                    down_prob /= prob_total
                    left_prob /= prob_total
                    right_prob /= prob_total
                    stop_prob /= prob_total
                    inverse_action_prob /= prob_total

                    # Sélection aléatoire basée sur les probabilités
                    random_number = random.uniform(0, 1)
                    if random_number < up_prob:
                        self.controle = "UP"
                    elif random_number < up_prob + down_prob:
                        self.controle = "DOWN"
                    elif random_number < up_prob + down_prob + left_prob:
                        self.controle = "LEFT"
                    elif random_number < up_prob + down_prob + left_prob + right_prob:
                        self.controle = "RIGHT"
                    elif random_number < up_prob + down_prob + left_prob + right_prob + stop_prob:
                        self.controle = "STOP"
                    else:
                        # Choisir l'inverse de l'action actuelle
                        if self.action == "LEFT":
                            self.controle = "RIGHT"
                        elif self.action == "RIGHT":
                            self.controle = "LEFT"
                        elif self.action == "UP":
                            self.controle = "DOWN"
                        elif self.action == "DOWN":
                            self.controle = "UP"
                        else:
                            # Si aucune action précédente, choisir aléatoirement entre LEFT et RIGHT
                            self.controle = random.choice(["LEFT", "RIGHT"])

            else:
                self.vitesse = self.vitesse_rage
                self.comportement_rage(game_map)
        else:
            self.vitesse = self.vitesse_mort
            self.fantome_comportement_dead(game_map)


    def fantome_comportement_weak(self, game_map, pukmun_coordonnees_cases):
        pass

    def fantome_comportement_dead(self, game_map):
        x_diff = self.coordonnees_cases[0] - 12
        y_diff = self.coordonnees_cases[1] - 10

        left = 98
        right = 98
        up = 98
        down = 98

        # Calcul des distances pour les mouvements horizontaux
        if x_diff > 0:
            left = x_diff
            if self.coordonnees_cases[1] == 11:
                right = self.DIMENSION_MAP[0] - x_diff
            '''else:
                right = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]'''
        elif x_diff < 0:
            if self.coordonnees_cases[1] == 11:
                left = self.DIMENSION_MAP[0] + x_diff
            '''else:
                left = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]'''
            right = -x_diff
        '''else:
            left = right = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]'''  # Si sur la même colonne, éviter mouvement horizontal

        # Calcul des distances pour les mouvements verticaux
        if y_diff > 0:
            up = y_diff
            '''down = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]'''
        elif y_diff < 0:
            '''up = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]'''
            down = -y_diff
        '''else:
            up = down = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]'''  # Si sur la même ligne, éviter mouvement vertical

        # Encourager la direction actuelle
        if self.action == "LEFT":
            left = 97
            right = 99
        elif self.action == "RIGHT":
            right = 97
            left = 99
        elif self.action == "UP":
            up = 97
            down = 99
        elif self.action == "DOWN":
            down = 97
            up = 99

        # self.fantome_update_action(game_map)

        # Vérifier les collisions avec les obstacles
        if self.fantome_check_collision_obstacle_left(game_map):
            left = 100
        if self.fantome_check_collision_obstacle_right(game_map):
            right = 100
        if self.fantome_check_collision_obstacle_up(game_map):
            up = 100
        if self.fantome_check_collision_obstacle_down(game_map):
            down = 100

        # Choisir la direction avec la plus petite distance
        min_distance = min(left, right, up, down)
        if min_distance == left:
            self.controle = "LEFT"
        elif min_distance == right:
            self.controle = "RIGHT"
        elif min_distance == up:
            self.controle = "UP"
        elif min_distance == down:
            self.controle = "DOWN"

    # TODO
    # Détaille le comportement du fantôme quand il est enragé
    def comportement_rage(self, game_map):
        if self.action == "LEFT":
            if not self.fantome_check_collision_obstacle_left(game_map):
                self.controle = "LEFT"
            else:
                self.rage = 0
                self.action = "STOP"
        if self.action == "RIGHT":
            if not self.fantome_check_collision_obstacle_right(game_map):
                self.controle = "RIGHT"
            else:
                self.rage = 0
                self.action = "STOP"
        if self.action == "UP":
            if not self.fantome_check_collision_obstacle_up(game_map):
                self.controle = "UP"
            else:
                self.rage = 0
                self.action = "STOP"
        if self.action == "DOWN":
            if not self.fantome_check_collision_obstacle_down(game_map):
                self.controle = "DOWN"
            else:
                self.rage = 0
                self.action = "STOP"

    def fantome_check_collision_pukmun(self, game_map, pukmun_coordonnees_pixels):
        x_diff = self.coordonnees_pixels[0] - pukmun_coordonnees_pixels[0]
        y_diff = self.coordonnees_pixels[1] - pukmun_coordonnees_pixels[1]

        collision_horizontale = False
        collision_verticale = False

        if x_diff > 0:
            if self.orientation_sprite == "LEFT":
                if (self.coordonnees_pixels[0] + (3*self.CELL_SIZE/20)) <= (pukmun_coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE/10) <= (self.coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE/10):
                    collision_horizontale = True
            elif self.orientation_sprite == "RIGHT":
                if (self.coordonnees_pixels[0] + self.CELL_SIZE/10) <= (pukmun_coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE / 10) <= (self.coordonnees_pixels[0] + self.CELL_SIZE - (3*self.CELL_SIZE/20)):
                    collision_horizontale = True
        elif x_diff < 0:
            if self.orientation_sprite == "LEFT":
                if (self.coordonnees_pixels[0] + (3*self.CELL_SIZE/20)) <= (pukmun_coordonnees_pixels[0] + self.CELL_SIZE / 10) <= (self.coordonnees_pixels[0] + self.CELL_SIZE - (3*self.CELL_SIZE/20)):
                    collision_horizontale = True
            elif self.orientation_sprite == "RIGHT":
                if (self.coordonnees_pixels[0] + self.CELL_SIZE/10) <= (pukmun_coordonnees_pixels[0] + self.CELL_SIZE / 10) <= (self.coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE/10):
                    collision_horizontale = True
        else:
            collision_horizontale = True

        if y_diff > 0:
            if (self.coordonnees_pixels[1] + self.CELL_SIZE/5) <= (pukmun_coordonnees_pixels[1] + self.CELL_SIZE - self.CELL_SIZE / 10) <= (self.coordonnees_pixels[1] + self.CELL_SIZE - self.CELL_SIZE / 10):
                collision_verticale = True
        elif y_diff < 0:
            if (self.coordonnees_pixels[1] + self.CELL_SIZE/5) <= (pukmun_coordonnees_pixels[1] + self.CELL_SIZE / 10) <= (self.coordonnees_pixels[1] + self.CELL_SIZE - self.CELL_SIZE / 10):
                collision_verticale = True
        else:
            collision_verticale = True

        if collision_horizontale and collision_verticale:
            return True
        return False

    # TODO (Doit sûrement être basculée dans game)
    # Renvoie True si PUKMUN est sur la même ligne ou colonne sans obstacle entre eux
    def voit_pukmun(self, game_map, pukmun_coordonnees_cases):
        x_diff = self.coordonnees_cases[0] - pukmun_coordonnees_cases[0]
        y_diff = self.coordonnees_cases[1] - pukmun_coordonnees_cases[1]

        colonne = False
        ligne = False

        if x_diff == 0:  # Pukmun est sur la colonne
            colonne = True
            if y_diff < 0:
                for i in range(int(self.coordonnees_cases[1]), int(pukmun_coordonnees_cases[1])):
                    if game_map.map_data[int(self.coordonnees_cases[0])][i] == 3:
                        colonne = False
            elif y_diff > 0:
                for i in range(int(pukmun_coordonnees_cases[1]), int(self.coordonnees_cases[1])):
                    if game_map.map_data[int(self.coordonnees_cases[0])][i] == 3:
                        colonne = False

        if y_diff == 0:  # Pukmun est sur la ligne
            ligne = True
            if x_diff < 0:
                for i in range(self.coordonnees_cases[0], pukmun_coordonnees_cases[0]):
                    if game_map.map_data[i][self.coordonnees_cases[1]] == 3:
                        ligne = False
            elif x_diff > 0:
                for i in range(pukmun_coordonnees_cases[0], self.coordonnees_cases[0]):
                    if game_map.map_data[i][self.coordonnees_cases[1]] == 3:
                        ligne = False

        return ligne or colonne

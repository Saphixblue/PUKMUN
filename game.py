# game.py

import pygame
import sys
from levels.level_1 import Level1
from levels.level_2 import Level2
from levels.level_3 import Level3
from levels.level_4 import Level4
from levels.level_5 import Level5
from sound_handler import SoundHandler


class Game:
    def __init__(self):

        pygame.init()

        self.DIMENSION_MAP = (25, 22)  # (colonnes, lignes)
        self.CELL_SIZE = 30
        self.WINDOW_SIZE = (
        self.DIMENSION_MAP[0] * self.CELL_SIZE, self.DIMENSION_MAP[1] * self.CELL_SIZE + self.CELL_SIZE)

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        pygame.display.set_caption("PUKMUN")

        # Niveau actuel
        self.level = None

        self.game_map = None
        self.pukmun = None

        self.fps = 60
        self.clock = pygame.time.Clock()

        self.frame = 0

        self.level_number = 1

        self.score = 0
        # Score à incrémenter en même temps que score de base, on lui retire 10000 chaque fois qu'il le dépasse
        self.score_extra_life = 0

        # Permet de compter les secondes
        self.compteur = 0

        # Détermine si l'on est au début d'un niveau (1) ou non (0)
        self.level_start = 1

        # Détermine si le niveau est sous l'effet d'un gros graille (1) ou non (0)
        self.gros_graille = 0

        # Détermine le nombre de grailles dans un niveau
        self.nombre_de_grailles = None

        # Nombre de grailles mangés par PUKMUN
        self.grailles_manges = 0

        # Nombre de vies restantes de PUKMUN
        self.lives = 3

        sound_handler = SoundHandler()

        self.intro_sound = sound_handler.intro_sound()
        self.graille_1_sound = sound_handler.graille_1_sound()
        self.graille_2_sound = sound_handler.graille_2_sound()
        self.fantome_deplacement_sound = sound_handler.fantome_deplacement_sound()
        self.gros_graille_sound = sound_handler.gros_graille_sound()
        self.graille_fantome_sound = sound_handler.graille_fantome_sound()
        self.fantome_mort_sound = sound_handler.fantome_mort_sound()
        self.extra_life_sound = sound_handler.extra_life_sound()
        self.pukmun_mort_sound = sound_handler.pukmun_mort_sound()

        self.graille = 1

    def level_init(self):
        if self.level_number == 1:
            self.level = Level1(self.DIMENSION_MAP, self.CELL_SIZE)
        elif self.level_number == 2:
            self.level = Level2(self.DIMENSION_MAP, self.CELL_SIZE)
        elif self.level_number == 3:
            self.level = Level3(self.DIMENSION_MAP, self.CELL_SIZE)
        elif self.level_number == 4:
            self.level = Level4(self.DIMENSION_MAP, self.CELL_SIZE)
        elif self.level_number == 5:
            self.level = Level5(self.DIMENSION_MAP, self.CELL_SIZE)

        self.game_map = self.level.level_map
        self.pukmun = self.level.pukmun
        self.level.draw_level_on_map()

        self.clock.tick(self.fps)

        self.frame = 0

        # Détermine le nombre de grailles dans un niveau
        self.nombre_de_grailles = 0
        for i in range(self.DIMENSION_MAP[0]):
            for j in range(self.DIMENSION_MAP[1]):
                if self.game_map.map_data[i][j] == 0 or self.game_map.map_data[i][j] == 1:
                    self.nombre_de_grailles += 1

        # Nombre de grailles mangés par PUKMUN
        self.grailles_manges = 0

        self.start_level()

    # Fonction pour quitter le jeu
    def quit_game(self):
        pygame.quit()
        sys.exit()

    # TODO: Ajouter début de niveau
    # Boucle principale du jeu
    def game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.pukmun.controle = "LEFT"
                    elif event.key == pygame.K_d:
                        self.pukmun.controle = "RIGHT"
                    elif event.key == pygame.K_z:
                        self.pukmun.controle = "UP"
                    elif event.key == pygame.K_s:
                        self.pukmun.controle = "DOWN"
                    self.pukmun.pukmun_update_controle_ivre()

            if self.level_start == 1:
                self.level_init()
                self.level_start = 0

            # Limiter le nombre d'images par seconde
            self.clock.tick(60)

            # Effacer l'écran
            self.screen.fill((0, 0, 0))

            # Dessiner la carte
            self.game_map.draw_map(self.screen)

            self.pukmun.pukmun_update_case()
            self.pukmun.pukmun_update_action(self.game_map)
            self.pukmun.pukmun_update_deplacement(self.game_map)
            self.pukmun.pukmun_update_sprite(pygame.time.get_ticks() // (1000 // self.fps) % self.fps)

            '''
            print(pygame.time.get_ticks() // (1000 // self.fps) % self.fps)
            print(self.pukmun.coordonnees_pixels)
            print(self.pukmun.coordonnees_cases)
            '''

            # Update du score et des cases
            if self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] == 0:
                self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] = 2
                self.score += 10
                self.score_extra_life += 10
                self.grailles_manges += 1
                if self.graille == 1:
                    self.graille_1_sound.play()
                    self.graille = 2
                elif self.graille == 2:
                    self.graille_2_sound.play()
                    self.graille = 1
            if self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] == 1:
                self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] = 2
                self.score += 10
                self.score_extra_life += 10
                self.grailles_manges += 1
                # TODO: Parcourir le tableau de fantômes, mettre weak à 1 et compteur à 8 (8 secondes d'effet pour le gros graille)
                # self.pukmun.powered = 1

            print(self.score)

            if self.score_extra_life // 10000 == 1:
                self.score_extra_life -= 10000
                self.gagner_une_vie()

            # Update de la valeur de la frame
            self.frame = pygame.time.get_ticks() // (1000 // self.fps) % self.fps

            # Dessiner Pac-Man
            self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))

            # Mettre à jour l'affichage
            pygame.display.flip()

            if self.grailles_manges == self.nombre_de_grailles:
                self.level_complete()
                self.level_start = 1

    # TODO: Afficher GAME OVER (quelques secondes), si high score --> updateLeaderBoard(), remise du score à zéro puis renvoi du joueur à l'écran titre
    def game_over(self):
        print("Game over")

    # TODO: Faire disparaître toutes les entités, faire disparaître tous les sons du jeu, jouer l'animation + son de mort de PUKMUN et lui retirer une vie.
    # Si plus de vies --> game_over
    def perdre_une_vie(self):
        print("Perdre une vie")

    def gagner_une_vie(self):
        if self.lives < 5:
            self.lives += 1

    # TODO: Tous les éléments sont placés; tout est immobile pendant que la musique de début se joue
    def start_level(self):
        print("Start Level")

    # TODO: Décommenter quand level_start() est fait, et quand tous les niveaux sont implémentés
    def level_complete(self):
        self.level_number += 1
        if self.level_number == 6:
            self.level_number = 1

    # TODO: Décommenter quand level_start() est fait, et quand tous les niveaux sont implémentés
    def previous_level(self):
        self.level_number -= 1
        if self.level_number == 0:
            self.level_number = 5

    # TODO: Renvoie True si PUKMUN a collisionné avec le fantôme passé en paramètre
    def collision_pukmun_fantome(self, fantome):
        print("Collision pukmun_fantome")

    # Gestion de la collision entre PUKMUN et les fantômes en fonction de leur état
    # TODO: Si PUKMUN n'est pas sous gros graille :
    # Si fantôme ivre ou fantôme fantôme --> Perd une vie
    # Sinon :
    # Si fantôme ivre ou fantôme fantôme --> Le mange, obtient les points et les affiche, fantôme devient mort
    # Fantôme mafieux --> Dodge
    def gestion_collision_pukmun_fantome(self, fantome):
        print("Gestion collision pukmun_fantome")

    # Gestion de la collision entre PUKMUN et la balle en fonction de leur état
    # TODO: Si bouclier non déployé dans la bonne direction --> Perd une vie
    # Si déployé dans la bonne direction :
    # Si powered --> golden passe à 1 et balle renvoyée
    # Sinon --> Balle renvoyée
    def gestion_collision_pukmun_balle(self, fantome_mafieux):
        print("Gestion collision pukmun_balle")

    # Gestion de la collision entre la balle et le fantôme mafieux qui l'a tirée en fonction de leur état
    # TODO: Si golden --> fantome dead à 1
    # Sinon : Dodge
    def gestion_collision_balle_fantome(self, fantome_mafieux):
        print("Gestion collision pukmun_balle_fantome")


'''
if __name__ == "__main__":
    game()
'''

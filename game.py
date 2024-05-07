# game.py

import pygame
import sys
from levels.level_1 import Level1


class Game:
    def __init__(self):

        pygame.init()

        self.DIMENSION_MAP = (25, 22) # (colonnes, lignes)
        self.CELL_SIZE = 30
        self.WINDOW_SIZE = (self.DIMENSION_MAP[0] * self.CELL_SIZE, self.DIMENSION_MAP[1] * self.CELL_SIZE + self.CELL_SIZE)

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        pygame.display.set_caption("PUKMUN")

        self.level_1 = Level1(self.DIMENSION_MAP, self.CELL_SIZE)
        # self.level_2
        # self.level_3
        # self.level_4
        # self.level_5

        # Niveau actuel
        self.level = self.level_1

        self.game_map = self.level.level_map
        self.pukmun = self.level.pukmun
        self.level.draw_level_on_map()

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.clock.tick(self.fps)

        self.frame = 0

        self.level_number = 1

        self.score = 0

        # Permet de compter les secondes
        self.compteur = 0

        # Détermine si l'on est au début d'un niveau (1) ou non (0)
        self.level_start = 1

        # Détermine si le niveau est sous l'effet d'un gros graille (1) ou non (0)
        self.gros_graille = 0

        # Détermine le nombre de grailles dans un niveau
        self.nombre_de_grailles = 0
        for i in range(self.DIMENSION_MAP[0]):
            for j in range(self.DIMENSION_MAP[1]):
                if self.game_map.map_data[i][j] == 0 or self.game_map.map_data[i][j] == 1:
                    self.nombre_de_grailles += 1

        # Nombre de grailles mangés pr PUKMUN
        self.grailles_manges = 0

        # Nombre de vies restantes de PUKMUN
        self.lives = 3

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

            # Limiter le nombre d'images par seconde
            pygame.time.Clock().tick(60)

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
                self.grailles_manges += 1
            if self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] == 1:
                self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] = 2
                self.score += 10
                self.grailles_manges += 1
                # TODO: Parcourir le tableau de fantômes, mettre weak à 1 et compteur à 8 (8 secondes d'effet pour le gros graille)
                # self.pukmun.powered = 1


            print(self.score)

            # Update de la valeur de la frame
            self.frame = pygame.time.get_ticks() // (1000 // self.fps) % self.fps

            # Dessiner Pac-Man
            self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))

            # Mettre à jour l'affichage
            pygame.display.flip()

    # TODO: Afficher GAME OVER (quelques econdes), si high score --> updateLeaderBoard(), remise du score à zéro puis renvoi du joueur à l'écran titre
    def game_over(self):
        print("Game over")

    # TODO: Faire disparaître toutes les entités, faire disparaître tous les sons du jeu, jouer l'animation + son de mort de PUKMUN et lui retirer une vie.
    # Si plus de vies --> game_over
    def perdre_une_vie(self):
        print("Perdre une vie")

    # TODO: Tous les éléments sont placés; tout est immobile pendant que la musique de début se joue
    def level_start(self):
        print("Level start")

    # TODO: Si PUKMUN a mangé tous les grailles disponibles, passer au niveau suivant en conservant le score (si niveau 5, revenir au 1)
    def level_complete(self):
        print("Level complete")

    # TODO: A appeler quand PUKMUN tombe dans un trou. Revenir au niveau précédent (si niveau 1, revenir au 5 même si pas de trou dans le 1)
    def previous_level(self):
        print("Previous level")

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
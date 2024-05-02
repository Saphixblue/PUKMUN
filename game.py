# game.py

import pygame
import sys
import os
from Map import Map
from pukmun import Pukmun
from sprite_handler import SpriteHandler


class Game:
    def __init__(self):

        pygame.init()

        self.DIMENSION_MAP = (25, 22) # (colonnes, lignes)
        self.CELL_SIZE = 30
        self.WINDOW_SIZE = (self.DIMENSION_MAP[0] * self.CELL_SIZE, self.DIMENSION_MAP[1] * self.CELL_SIZE)

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        pygame.display.set_caption("PUKMUN")

        self.game_map = Map(self.DIMENSION_MAP, self.CELL_SIZE)

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.clock.tick(self.fps)

        self.frame = 0
        self.check_frame = 0

        # self.level = 1

        self.level_1()

        self.pukmun = Pukmun([0, 10], self.CELL_SIZE)

        self.score = 0

    # Fonction pour quitter le jeu
    def quit_game(self):
        pygame.quit()
        sys.exit()



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

            # Effacer l'écran
            self.screen.fill((0, 0, 0))

            # Dessiner la carte
            self.game_map.draw_map(self.screen)

            if pygame.time.get_ticks() // (1000 // self.fps) % self.fps != self.frame:
                self.pukmun.pukmun_update_case(self.game_map)
                self.pukmun.pukmun_update_action(self.game_map)
                self.pukmun.pukmun_update_deplacement(self.game_map)
                # self.pukmun.pukmun_update_deplacement_sprite(self.game_map)
                self.pukmun.pukmun_update_sprite(pygame.time.get_ticks() // (1000 // self.fps) % self.fps)

                '''
                print(pygame.time.get_ticks() // (1000 // self.fps) % self.fps)
                print(self.pukmun.coordonnees_pixels)
                print(self.pukmun.coordonnees_cases)
                '''
                print(self.score)



                if self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] == 0:
                    self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] = 2
                    self.score += 10

                # Update de la valeur de la frame
                self.frame = pygame.time.get_ticks() // (1000 // self.fps) % self.fps

            # Dessiner Pac-Man
            self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))


            # Mettre à jour l'affichage
            pygame.display.flip()

            # Limiter le nombre d'images par seconde
            # pygame.time.Clock().tick(60)

    def level_1(self):
        # Mettre en place un obstacle sur la carte
        self.game_map.draw_rectangle_obstacle(5, 10, 5,
                                              1)  # Dessine un rectangle à la case (10;10) longueur 5, largeur 1
        self.game_map.draw_angle_obstacle(2, 2, 3, 2, 1,
                                          "bas")  # dessin angle en (2,2); longueur 3; position angle 2, longueurangle 1; position "bas"
        self.game_map.draw_angle_obstacle(10, 20, 3, 2, 3,
                                          "haut")  # dessin angle en (2,2); longueur 3; position angle 2, longueurangle 1; position "bas"
        self.game_map.draw_rectangle_obstacle(0, 0, 2, 1)
        self.game_map.draw_rectangle_obstacle(12, 9, 1, 9)
        self.game_map.draw_rectangle_obstacle(14, 9, 1, 8)
        self.game_map.draw_rectangle_obstacle(1, 9, 1, 8)
        # self.game_map.draw_rectangle_obstacle(12, 9, 1, 9)
        # game_map.draw_rectangle_obstacle(0, 0, 30,30)  # Dessine un rectangle à la case (10;10) longueur 5, largeur 1

'''
if __name__ == "__main__":
    game()
'''
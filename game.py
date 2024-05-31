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
        pygame.mixer.pre_init(44100, -16, 2, 512)
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

        self.level_number = 3

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

        self.perte_vie = 0
        self.fin_de_jeu = 0

        self.initial = 1

        # Set volumes
        self.graille_1_sound.set_volume(1.0)
        self.graille_2_sound.set_volume(1.0)

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

        if self.initial:
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

    def handle_events(self):
        self.pukmun.shield_direction = "NONE"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.pukmun.controle = "LEFT"
                    self.pukmun.pukmun_update_controle_ivre()
                elif event.key == pygame.K_d:
                    self.pukmun.controle = "RIGHT"
                    self.pukmun.pukmun_update_controle_ivre()
                elif event.key == pygame.K_z:
                    self.pukmun.controle = "UP"
                    self.pukmun.pukmun_update_controle_ivre()
                elif event.key == pygame.K_s:
                    self.pukmun.controle = "DOWN"
                    self.pukmun.pukmun_update_controle_ivre()

            # Peut-être gérer différemment ici, mais ça fonctionne pas mal

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.pukmun.shield_controle = "LEFT"
            elif keys[pygame.K_RIGHT]:
                self.pukmun.shield_controle = "RIGHT"
            elif keys[pygame.K_UP]:
                self.pukmun.shield_controle = "UP"
            elif keys[pygame.K_DOWN]:
                self.pukmun.shield_controle = "DOWN"
            else:
                self.pukmun.shield_controle = "NONE"

        self.pukmun.pukmun_update_controle_shield()

    def update_game(self):
        if self.level_start == 1:
            self.level_init()
            self.initial = 0

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
            self.pukmun.powered = 1

            print(self.score)

        if self.score_extra_life // 10000 == 1:
            self.score_extra_life -= 10000
            self.gagner_une_vie()

        for fantome in self.level.fantomes:
            if fantome.fantome_check_collision_pukmun(self.game_map, self.pukmun.coordonnees_pixels):
                self.gestion_collision_pukmun_fantome(fantome)

        # Update de la valeur de la frame
        self.frame = pygame.time.get_ticks() // (1000 // self.fps) % self.fps

    # TODO: Ajouter début de niveau
    # Boucle principale du jeu
    def game(self):
        running = True
        while running:
            self.update_game()

            self.handle_events()

            # Limiter le nombre d'images par seconde
            self.clock.tick(60)

            # Effacer l'écran
            self.screen.fill((0, 0, 0))

            # Dessiner la carte
            self.game_map.draw_map(self.screen)

            self.pukmun.pukmun_update_case()
            self.pukmun.pukmun_update_action(self.game_map)
            self.pukmun.pukmun_update_deplacement()
            self.pukmun.pukmun_update_sprite(pygame.time.get_ticks() // (1000 // self.fps) % self.fps)
            self.pukmun.pukmun_update_controle_shield()
            self.pukmun.pukmun_update_sprite_shield()

            for fantome in self.level.fantomes:
                if fantome.compteur_sortie != 0 and fantome.compteur_frame_sortie == self.frame:
                    fantome.compteur_sortie -= 1
                if fantome.compteur_sortie == 0:
                    fantome.fantome_comportement(self.game_map, self.pukmun.coordonnees_cases)
                fantome.fantome_update_case()
                fantome.fantome_update_action(self.game_map)
                fantome.fantome_update_deplacement(self.game_map)

                fantome.fantome_check_collision_pukmun(self.game_map, self.pukmun.coordonnees_pixels)

                fantome.fantome_update_sprite()

            # Dessiner Pac-Man
            self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))
            if self.pukmun.shield_sprite is not None:
                self.screen.blit(self.pukmun.shield_sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))

            # Dessiner les fantômes
            for fantome in self.level.fantomes:
                self.screen.blit(fantome.sprite,(fantome.coordonnees_pixels[0], fantome.coordonnees_pixels[1]))

            # Mettre à jour l'affichage
            pygame.display.flip()

            if self.grailles_manges == self.nombre_de_grailles:
                self.level_complete()
                self.level_start = 1
                self.initial = 1

    # TODO: Afficher GAME OVER (quelques secondes), si high score --> updateLeaderBoard(), remise du score à zéro puis renvoi du joueur à l'écran titre
    def game_over(self):
        print("Game over")
        # Afficher "Game Over" à l'écran 3 secondes

        # Revenir au menu

    # TODO: Faire disparaître toutes les entités, faire disparaître tous les sons du jeu, jouer l'animation + son de mort de PUKMUN et lui retirer une vie.
    # Si plus de vies --> game_over
    def perdre_une_vie(self):
        # Limiter le nombre d'images par seconde
        self.clock.tick(60)

        # Figer le jeu pendant une demi-seconde
        self.pukmun.sprite = self.pukmun.pukmun_mort_1_image
        pygame.time.delay(500)

        # Effacer l'écran et redessiner la carte sans les fantômes
        self.screen.fill((0, 0, 0))
        self.game_map.draw_map(self.screen)

        # Jouer le son de mort de Pukmun
        self.pukmun_mort_sound.play()

        # Afficher l'animation de mort de Pukmun
        for frame in range(60):  # 60 frames pour l'animation de mort
            self.pukmun.pukmun_mort(frame)
            self.screen.fill((0, 0, 0))
            self.game_map.draw_map(self.screen)
            self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))
            pygame.display.flip()
            pygame.time.delay(16)  # Ajuster le délai pour une animation fluide
        self.pukmun.sprite = self.pukmun.image_vide

        # Réduire le nombre de vies de Pukmun
        self.lives -= 1

        # Vérifier si le jeu est terminé
        if self.lives <= 0:
            self.game_over()
        else:
            # Redémarrer le niveau
            self.level_start = 1
            self.level_init()
        print("Perdre une vie")

    def gagner_une_vie(self):
        if self.lives < 5:
            self.lives += 1

    # TODO: Si possible, afficher 3, 2, 1, Go! pendant la musique sous le pit des fantômes
    # TODO: Tous les éléments sont placés; tout est immobile pendant que la musique de début se joue
    def start_level(self):
        # Dessiner la carte
        self.screen.fill((0, 0, 0))
        self.game_map.draw_map(self.screen)

        # Placer Pukmun
        self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))

        # TODO: Placer les fantômes
        for fantome in self.level.fantomes:
            self.screen.blit(fantome.sprite, (fantome.coordonnees_pixels[0], fantome.coordonnees_pixels[1]))

        pygame.display.flip()

        self.intro_sound.play()
        pygame.time.delay(4000)  # Attendre 4 secondes

        self.level_start = 0

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

    # Gestion de la collision entre PUKMUN et les fantômes en fonction de leur état
    # TODO: Si PUKMUN n'est pas sous gros graille :
    # Si fantôme ivre ou fantôme fantôme --> Perd une vie
    # Sinon :
    # Si fantôme ivre ou fantôme fantôme --> Le mange, obtient les points et les affiche, fantôme devient mort
    # Fantôme mafieux --> Dodge
    def gestion_collision_pukmun_fantome(self, fantome):
        # Si PUKMUN pas sous gros graille
        self.perdre_une_vie()

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

    # TODO: Fantôme_déplacement (booléen) qui parcourt le tableau de fantômes et retourne True si au moins un est en vie et en train de se déplacer

'''
if __name__ == "__main__":
    game()
'''

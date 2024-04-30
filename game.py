# game.py

import pygame
import sys
import os
from map import Map

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 600
hauteur_fenetre = 600
DIMENSION_MAP = (15,15)   # Nombre de cellules en (largeur,hauteur) : exemple (23,20)

#WINDOW_SIZE = (DIMENSION_MAP[0]*30, DIMENSION_MAP[1]*30)
WINDOW_SIZE = (largeur_fenetre, hauteur_fenetre)
CELL_COLUMN_SIZE = WINDOW_SIZE[0] // DIMENSION_MAP[0]  # Définir la hauteur des cellules en pixels
CELL_ROW_SIZE = WINDOW_SIZE[1] // DIMENSION_MAP[1]  # Définir la longueur des cellules en pixels
CELL_SIZE = (CELL_COLUMN_SIZE,CELL_ROW_SIZE)

# Créer la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pac-Man")

# Instance de la classe Map
game_map = Map(WINDOW_SIZE, CELL_SIZE)

# Charger l'image de Pac-Man et redimensionner
current_path = os.path.dirname(__file__)  # Chemin du répertoire actuel du fichier
image_path = os.path.join(current_path, 'images')  # Chemin vers le dossier des images
pacman_image_path = os.path.join(image_path, 'pacman.png')
Pacman = pygame.image.load(pacman_image_path).convert()
Pacman = pygame.transform.scale(Pacman, CELL_SIZE)  # Redimensionner pour que pacman fasse 95% de la taille d'une case/cellule
#Pacman = pygame.transform.scale(Pacman, (CELL_SIZE[0]-10, CELL_SIZE[1]-10))  # Redimensionner pour que pacman fasse 95% de la taille d'une case/cellule

# image obstacle
obstacle_image_path = os.path.join(image_path, 'Tile_1.png')
obstacle = pygame.image.load(obstacle_image_path).convert()
obstacle = pygame.transform.scale(obstacle, CELL_SIZE)  # Redimensionner pour que l'obstacle fasse la taille d'une case/cellule

# Position de départ de Pac-Man
pacman_position = [300, 300]

# Vitesse de déplacement de Pac-Man
pacman_speed = 5

# Direction de départ de Pac-Man (vers la droite)
pacman_direction = "RIGHT"

# Fonction pour quitter le jeu
def quit_game():
    pygame.quit()
    sys.exit()

# Vérifier si Pac-Man entre en collision avec un obstacle
def check_collision(x, y):
    cell_x = x // CELL_SIZE[0]
    cell_y = y // CELL_SIZE[1]

    # Vérifier si les coordonnées sont dans les limites de la carte
    if cell_x < 0 or cell_x >= len(game_map.map_data[0]) or cell_y < 0 or cell_y >= len(game_map.map_data):
        return False

    if game_map.map_data[cell_y][cell_x] == 3:
        return True
    return False

# Boucle principale du jeu
def game():
    global pacman_direction
    global pacman_position

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman_direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    pacman_direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    pacman_direction = "UP"
                elif event.key == pygame.K_DOWN:
                    pacman_direction = "DOWN"

        next_position = pacman_position.copy()
        if pacman_direction == "LEFT":
            next_position[0] -= pacman_speed
        elif pacman_direction == "RIGHT":
            next_position[0] += pacman_speed
        elif pacman_direction == "UP":
            next_position[1] -= pacman_speed
        elif pacman_direction == "DOWN":
            next_position[1] += pacman_speed

        # Vérifier si Pac-Man entre en collision avec un obstacle
        if not check_collision(next_position[0], next_position[1]) \
                and not check_collision(next_position[0] + Pacman.get_width() - 1, next_position[1]) \
                and not check_collision(next_position[0], next_position[1] + Pacman.get_height() - 1) \
                and not check_collision(next_position[0] + Pacman.get_width() - 1, next_position[1] + Pacman.get_height() - 1):
            pacman_position = next_position

        # Limiter Pac-Man dans la fenêtre
        pacman_position[0] = max(0, min(pacman_position[0], WINDOW_SIZE[0] - Pacman.get_width()))
        pacman_position[1] = max(0, min(pacman_position[1], WINDOW_SIZE[1] - Pacman.get_height()))

        # Effacer l'écran
        screen.fill((0, 0, 0))

        # Dessiner la carte
        game_map.draw_map(screen)

        # Dessiner Pac-Man
        screen.blit(Pacman, pacman_position)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter le nombre d'images par seconde
        pygame.time.Clock().tick(60)

# Mettre en place un obstacle sur la carte
#game_map.draw_rectangle_obstacle(5, 10, 5,1)  # Dessine un rectangle à la case (10;10) longueur 5, largeur 1
game_map.draw_angle_obstacle(10,20,3,2,3,"haut") # dessin angle en (2,2); longueur 3; position angle 2, longueurangle 1; position "bas"
#game_map.draw_rectangle_obstacle(0, 0, 30,30)
game_map.draw_angle_obstacle(2,2,3,2,1,"bas")
game_map.draw_rectangle_obstacle(4, 1, 5,1)
game_map.draw_rectangle_obstacle(4, 3, 1,3)
game_map.draw_rectangle_obstacle(2, 5, 1,3)
game_map.draw_rectangle_obstacle(0, 0, 5,1)
game_map.draw_rectangle_obstacle(0, 0, 1,5)






if __name__ == "__main__":
    game()








'''
# game.py
import pygame
import sys
import os
from map import Map

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WINDOW_SIZE = (600, 600)
BLACK = (0, 0, 0)

# Créer la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pac-Man")

# Charger l'image de Pac-Man et redimensionner
current_path = os.path.dirname(__file__)  # Chemin du répertoire actuel du fichier
image_path = os.path.join(current_path, 'images')  # Chemin vers le dossier des images
pacman_image_path = os.path.join(image_path, 'pacman.png')
Pacman = pygame.image.load(pacman_image_path).convert()
Pacman = pygame.transform.scale(Pacman, (40, 40))  # Redimensionner à la taille souhaitée

# Position de départ de Pac-Man
pacman_position = [300, 300]
pacman_speed = 5

# Direction de départ de Pac-Man (vers la droite)
pacman_direction = "RIGHT"

# Instance de la classe Map
game_map = Map(WINDOW_SIZE)

# Fonction pour quitter le jeu
def quit_game():
    pygame.quit()
    sys.exit()

# Boucle principale du jeu
def game():
    global pacman_direction  # Déclaration de la variable globale car elle est définie en dehors de la fonction

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            # Gérer les événements des touches directionnelles
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman_direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    pacman_direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    pacman_direction = "UP"
                elif event.key == pygame.K_DOWN:
                    pacman_direction = "DOWN"

        # Déplacer Pac-Man dans la direction actuelle
        if pacman_direction == "LEFT":
            pacman_position[0] -= pacman_speed
        elif pacman_direction == "RIGHT":
            pacman_position[0] += pacman_speed
        elif pacman_direction == "UP":
            pacman_position[1] -= pacman_speed
        elif pacman_direction == "DOWN":
            pacman_position[1] += pacman_speed

        # Limitation de Pac-Man dans la fenêtre
        pacman_position[0] = max(0, min(pacman_position[0], WINDOW_SIZE[0] - Pacman.get_width()))
        pacman_position[1] = max(0, min(pacman_position[1], WINDOW_SIZE[1] - Pacman.get_height()))

        # Affichage de la carte
        screen.fill(BLACK)
        game_map.draw_map(screen)

        # Affichage de Pac-Man
        screen.blit(Pacman, pacman_position)

        pygame.display.flip()

        # Limiter le taux de rafraîchissement de l'écran
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    game()
'''








'''
# game.py
import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WINDOW_SIZE = (600, 600)
BLACK = (0, 0, 0)

# Créer la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pac-Man")

# Déterminer le chemin vers le dossier des images
current_path = os.path.dirname(__file__)  # Chemin du répertoire actuel du fichier
image_path = os.path.join(current_path, 'images')  # Chemin vers le dossier des images

# Charger l'image de Pac-Man et redimensionner
pacman_image_path = os.path.join(image_path, 'pacman.png')
Pacman = pygame.image.load(pacman_image_path).convert()
Pacman = pygame.transform.scale(Pacman, (40, 40))  # Redimensionner à la taille souhaitée

# Position de départ de Pac-Man
pacman_position = [300, 300]
pacman_speed = 5

# Direction de départ de Pac-Man (vers la droite)
pacman_direction = "RIGHT"

# Fonction pour quitter le jeu
def quit_game():
    pygame.quit()
    sys.exit()

# Boucle principale du jeu
def game():
    global pacman_direction  # Déclaration de la variable globale car elle est définie en dehors de la fonctions

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            # Gérer les événements des touches directionnelles
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman_direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    pacman_direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    pacman_direction = "UP"
                elif event.key == pygame.K_DOWN:
                    pacman_direction = "DOWN"


        # Déplacer Pac-Man dans la direction actuelle
        if pacman_direction == "LEFT":
            pacman_position[0] -= pacman_speed
        elif pacman_direction == "RIGHT":
            pacman_position[0] += pacman_speed
        elif pacman_direction == "UP":
            pacman_position[1] -= pacman_speed
        elif pacman_direction == "DOWN":
            pacman_position[1] += pacman_speed

        # Limitation de Pac-Man dans la fenêtre
        pacman_position[0] = max(0, min(pacman_position[0], WINDOW_SIZE[0] - Pacman.get_width()))
        pacman_position[1] = max(0, min(pacman_position[1], WINDOW_SIZE[1] - Pacman.get_height()))

        # Affichage de Pac-Man et de la carte
        screen.fill(BLACK)
        screen.blit(Pacman, pacman_position)
        pygame.display.flip()

        # Limiter le taux de rafraîchissement de l'écran
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    game()
'''
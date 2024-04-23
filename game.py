# game.py
import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WINDOW_SIZE = (800, 600)
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
import main  # Importer main.py pour lancer le jeu principal
import menu  # Importer game.py pour lancer le jeu principal
import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WINDOW_SIZE = (600, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Créer la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pac-Man")

# Charger l'image de Pac-Man et redimensionner
Pacman = pygame.image.load('pacman.png').convert()
Pacman = pygame.transform.scale(Pacman, (40, 40))  # Redimensionner à la taille souhaitée

# Position de départ de Pac-Man
pacman_position = [300, 300]
pacman_speed = 5

# Direction de départ de Pac-Man (vers la droite)
pacman_direction = "RIGHT"

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

pygame.quit()
sys.exit()
'''
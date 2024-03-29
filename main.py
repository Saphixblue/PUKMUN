import pygame
import sys

# Define constants
GAME_WIDTH, GAME_HEIGHT = 28, 31
GAME_SPEED = 10
# Dimensions de la fenêtre
"""
largeur_fenetre = 28 * 16  # Taille d'une case (16 pixels) multipliée par le nombre de cases en largeur
hauteur_fenetre = 31 * 16  # Taille d'une case (16 pixels) multipliée par le nombre de cases en hauteur
"""
largeur_fenetre = 400
hauteur_fenetre = 460
# Couleurs
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
BLANC = (255, 255, 255)

# Initialize pygame
pygame.init()

"""
# Create the game window
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pygame.FULLSCREEN)

"""

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre), pygame.FULLSCREEN)
#fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('Pacman')

# Chargement des images
Fantome_ivre = pygame.image.load('Fantome_ivre_test.png').convert_alpha()

# Define the starting position of Pacman
Fantome_ivre_x = largeur_fenetre // 2
Fantome_ivre_y = hauteur_fenetre // 2

# Carte de jeu (exemple)
carte = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.#.##########.#.####.#",
    "#.####.#.##########.#.####.#",
    "#......#....##....#.....#..#",
    "######.#####.##.#####.######",
    "######.#####.##.#####.######",
    "######.##..........##.######",
    "######.##.###  ###.##.######",
    "      .   .##  ##.   .      ",
    "######.##.########.##.######",
    "######.##.########.##.######",
    "######.##.########.##.######",
    "######.##..........##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..##..................##..#",
    "###.##.#.##########.#.##.###",
    "###.##.#.##########.#.##.###",
    "#......#....##....#.....#..#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################",
]

# Fonction pour dessiner la carte
def dessiner_carte():
    for y, ligne in enumerate(carte):
        for x, case in enumerate(ligne):
            if case == "#":  # Mur
                pygame.draw.rect(fenetre, BLEU, (x * 16, y * 16, 16, 16))

# Game loop
running = True
while running:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Draw on the screen
    fenetre.fill(NOIR)
    # Add code here to draw the Pacman character, ghosts, and maze

    # Dessiner la carte
    #dessiner_carte()

    # Update the screen
    pygame.display.update()

# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    fenetre.fill(NOIR)

    # Dessiner la carte
    dessiner_carte()

    # Mettre à jour l'affichage
    pygame.display.flip()




# Exit the game
pygame.quit()
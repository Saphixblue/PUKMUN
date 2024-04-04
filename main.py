import pygame
import sys


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

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
#fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('Pacman')

# Chargement des images
#Fantome_ivre = pygame.image.load('Fantome_ivre_test.png').convert_alpha()

# Define the starting position of Pacman
#Fantome_ivre_x = largeur_fenetre // 2
#Fantome_ivre_y = hauteur_fenetre // 2


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
Jeu = True
while Jeu:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logique du jeu

    # Dessiner l'ecran
    fenetre.fill(NOIR)

    # Code pour dessiner Pacman les ghosts, et la map

    # Dessiner la carte
    #dessiner_carte()

    # Mettre à jour les modifs de la boucle sur l'écran
    pygame.display.update()


# Exit the game
pygame.quit()
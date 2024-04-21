import pygame
import button
import example

pygame.init()

# Paramètres de la fenêtre
WINDOW_SIZE = (800, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Créer la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pac-Man")

# Charger l'image de Pac-Man
Pacman = pygame.image.load('pacman.png').convert()
Pacman = pygame.transform.scale(Pacman, (40, 40))  # Redimensionner à la taille souhaitée


screen = pygame.display.set_mode((WINDOW_SIZE))
pygame.display.set_caption("Main Menu")



#define fonts
font = pygame.image.load("menu/ecran_menu.png")

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
back_button = button.Button(332, 450, back_img, 1)


def draw_text(text, font, text_col, x, y):
# img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


def accueil():
  #game loop
  #game variables
  menu_state = "main"
  game_paused = False
  run = True
  while run:

    screen.fill((0, 0, 0))

    #check if game is paused
    if game_paused == True:
      #check menu state
      if menu_state == "main":

        #draw pause screen buttons
        if resume_button.draw(screen):
          game_paused = False
          example.jeu(WINDOW_SIZE)

        if options_button.draw(screen):
          menu_state = "options"
        if quit_button.draw(screen):
          run = False

      #check if the options menu is open
      if menu_state == "options":

        #draw the different options buttons
        if audio_button.draw(screen):
          print("Audio Settings")
        if back_button.draw(screen):
          menu_state = "main"
    else:
      draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    #event handler
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_paused = True
      if event.type == pygame.QUIT:
        run = False

    pygame.display.update()

accueil ()

pygame.quit()
sys.exit()
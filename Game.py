import pygame
import random
from Maze.Maze import Maze
from Consumables.Ether import Ether
from Consumables.Syringe import Syringe





pygame.init()

# Création de l'instance
maze = Maze()


# Appel des méthodes
maze.load_maze_from_file()

# win = window
win = pygame.display.set_mode((len(maze.array) * 20, len(maze.array) * 20))

# Nommer la fenêtre
pygame.display.set_caption("Macgyver")


# Coordonnées
pos_macgyver_x = 0
pos_macgyver_y = 0
width = 32
height = 43
vel = 20

Syringe = Syringe()
Ether = Ether()
Ether.place_object_randomly(maze)
Syringe.place_object_randomly(maze)

# Boucle principale
run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    """Cell1.remove_item(MacGyver)
    Cell2.add_item(MacGyver)
    if keys[pygame.K_LEFT]:
        move_left()"""
    if keys[pygame.K_LEFT] and pos_macgyver_x > 0:
        pos_macgyver_x -= vel
    elif keys[pygame.K_RIGHT] and pos_macgyver_x < (len(maze.array) * 20) - 20:
        pos_macgyver_x += vel
    elif keys[pygame.K_UP] and pos_macgyver_y > 0:
        pos_macgyver_y -= vel
    elif keys[pygame.K_DOWN] and pos_macgyver_y < (len(maze.array) * 20) - 20:
        pos_macgyver_y += vel

    # Pour qu'il n'y ait qu'une image de MacGyver
    win.fill((0,0,0))

    # boucles pour maze.array

    for line_number, line in enumerate(maze.array, start=0):
        y = line_number * 20

        for cell_number, cell in enumerate(line, start=0):
            x = cell_number * 20
            Img_path = cell.load_img()
            Img = pygame.image.load(Img_path)
            win.blit(Img, (x, y))

            items = cell.get_items()
            for item in items:
                Img_path = item.load_img()
                Img = pygame.image.load(Img_path)
                win.blit(Img, (x, y))





    # Chargement des images
    MacGyverImg = pygame.image.load('Images/MacGyver.png')
    win.blit(MacGyverImg, (pos_macgyver_x, pos_macgyver_y))


    # mise à jour de la fenêtre
    pygame.display.update()



# quitter le jeu
pygame.quit()

maze.save_maze()

# Créer objet Macgyver
# Et un objet characters (macgyver et gardien sont enfants)
# utilisr l'objet macgyver dans game.py
# créer une fonction get macgyver_position pour déplacer le gros pâté
# créer des items (seringue..) et les faire apparaître randomly sur des paths avec random.choice(list)
# créer une fonction add_item dans cell.py puis créer une fonction qui récupère les items des cases

# mettre les objets (gestion) en aléatoire à la l37 (get random cell from array) puis afficher
# faire la différence entre mur et chemin (récupérer toutes les cases puis retirer les mauvaises)
# dans game, seulement création d'instance et appel de fonctions

# compléter fonction macgver

# commandes pip
# python -m pip install abc = installer un pip dans le dossier
# python -m pip freeze = voir ce qui est installé dans le dossier

# objet + class macgyver + collision
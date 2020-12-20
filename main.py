import pygame
import os


# Sprites from https://opengameart.org/content/animated-snake provided by Calciumtrice

pygame.init()

# Screen dimensions i2c screen

SCREEN_HEIGHT = 64
SCREEN_WIDTH = 128
SCREEN = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)


RUNNING = [pygame.image.load(os.path.join("CutSprites/walk/tile020.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile021.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile022.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile023.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile024.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile025.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile026.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile027.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile028.png")),
           pygame.image.load(os.path.join("CutSprites/walk/tile029.png"))]

JUMPING = [pygame.image.load(os.path.join("CutSprites/strike/tile030.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile031.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile032.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile033.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile034.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile035.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile036.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile037.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile038.png")),
           pygame.image.load(os.path.join("CutSprites/strike/tile039.png"))]

BIRD = [pygame.image.load(os.path.join("CutSprites/Assets/bird1")),
        pygame.image.load(os.path.join("CutSprites/Assets/bird2"))]

CACTUS = [pygame.image.load(os.path.join("CutSprites/Assets/Cactus1.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/Cactus2.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/Cactus3.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/Cactus4.png"))]



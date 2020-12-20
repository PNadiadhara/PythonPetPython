import pygame
import os


# Sprites from https://opengameart.org/content/animated-snake provided by Calciumtrice

pygame.init()

# Screen dimensions i2c screen

SCREEN_HEIGHT = 64 #600
SCREEN_WIDTH = 128 #1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


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

BIRD = [pygame.image.load(os.path.join("CutSprites/Assets/bird1.png")),
        pygame.image.load(os.path.join("CutSprites/Assets/bird2.png"))]

CACTUS = [pygame.image.load(os.path.join("CutSprites/Assets/Cactus1.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/Cactus2.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/Cactus3.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/Cactus4.png"))]


class Snake:
    # to be adjusted to fit small scree
    X_POS = 8 #80
    Y_POS = 20 #310

    def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.snake_run = True
        self.snake_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.snake_rect = self.image.get_rect()
        self.snake_rect.x = self.X_POS
        self.snake_rect.y = self.Y_POS


    def update(self, userInput):
        if self.snake_run:
            self.run()
        if self.snake_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.snake_jump:
            self.snake_jump = True
            self.snake_run = False
        elif not self.snake_jump:
            self.snake_run = True
            self.snake_jump = False


    def run(self):
        self.image = self.run_img[self.step_index]
        self.snake_rect = self.image.get_rect()
        self.snake_rect.x = self.X_POS
        self.snake_rect.y = self.Y_POS
        self.step_index += 1  # used to cycle from frames 1-10 of walk cycle


    def draw(self, SCREEN):
        # Note sprites originally face oposite direction, easier to just flip with transform
        SCREEN.blit(pygame.transform.flip(self.image, True, False), (self.snake_rect.x, self.snake_rect.y))

def main():
    run = True
    clock = pygame.time.Clock()
    player = Snake()

    while run:
        for event in pygame.event.get():
            # if x is clicked on window
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255)) # set BG to black for oled
        userInput = pygame.key.get_pressed() # update to respond to pushbutton switch

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(10)
        pygame.display.update()


main()
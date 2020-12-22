import pygame
import os
import random


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

DUCKING = [pygame.image.load(os.path.join("CutSprites/spin/tile010.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile011.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile012.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile013.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile014.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile015.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile016.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile017.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile018.png")),
           pygame.image.load(os.path.join("CutSprites/spin/tile019.png"))]

BIRD = [pygame.image.load(os.path.join("CutSprites/Assets/bird1.png")),
        pygame.image.load(os.path.join("CutSprites/Assets/bird2.png"))]

CACTUS = [pygame.image.load(os.path.join("CutSprites/Assets/smallCactus1.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/smallCactus2.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/smallCactus3.png")),
          pygame.image.load(os.path.join("CutSprites/Assets/smallCactus4.png"))]

CLOUD = pygame.image.load(os.path.join("CutSprites/Assets/Cloud.png"))

BG = pygame.image.load(os.path.join("CutSprites/Assets/track.png"))




class Snake:
    # to be adjusted to fit small scree
    X_POS = 8 #80
    Y_POS = 20 #310
    Y_POS_DUCK = 25
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.duck_img = DUCKING

        self.snake_run = True
        self.snake_jump = False
        self.snake_duck = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.snake_rect = self.image.get_rect()
        self.snake_rect.x = self.X_POS
        self.snake_rect.y = self.Y_POS
        self.jump_vel = self.JUMP_VEL

    def update(self, userInput):
        if self.snake_run:
            self.run()
        if self.snake_jump:
            self.jump()
        if self.snake_duck:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.snake_jump:
            self.snake_jump = True
            self.snake_duck = False
            self.snake_run = False
        elif userInput[pygame.K_DOWN] and not self.snake_jump:
            self.snake_run = False
            self.snake_jump = False
            self.snake_duck = True
        elif not (self.snake_jump or userInput[pygame.K_DOWN]):
            self.snake_run = True
            self.snake_jump = False
            self.snake_duck = False


    def run(self):
        self.image = self.run_img[self.step_index]
        self.snake_rect = self.image.get_rect()
        self.snake_rect.x = self.X_POS
        self.snake_rect.y = self.Y_POS
        self.step_index += 1  # used to cycle from frames 1-10 of walk cycle

    def jump(self):
        self.image = self.jump_img[self.step_index]
        if self.snake_jump:
            self.snake_rect.y -= self.jump_vel
            self.jump_vel -= 0.8 * 2
        if self.jump_vel < -self.JUMP_VEL:
            self.snake_jump = False
            self.jump_vel = self.JUMP_VEL


    def duck(self):
        self.image = self.duck_img[self.step_index]
        self.snake_rect = self.image.get_rect()
        self.snake_rect.x = self.X_POS
        self.snake_rect.y = self.Y_POS_DUCK
        self.step_index += 1  # used to cycle from frames 1-10 of walk cycle

    def draw(self, SCREEN):
        # Note sprites originally face oposite direction, easier to just flip with transform
        SCREEN.blit(pygame.transform.flip(self.image, True, False), (self.snake_rect.x, self.snake_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(0, 7)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(250, 1000)
            self.y = random.randint(5, 10)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

# this will be parent class for bird and cactus
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 3)
        super().__init__(image, self.type)
        self.rect.y = 36


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 2
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1




def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    game_speed = 14
    run = True
    clock = pygame.time.Clock()
    player = Snake()
    cloud = Cloud()
    x_pos_bg = 0
    y_pos_bg = 50
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 10)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1

        if points % 100 == 0:
            game_speed += 1

        text = font.render(str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (100, 5)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed


    while run:
        for event in pygame.event.get():
            # if x is clicked on window
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255)) # set BG to black for oled
        userInput = pygame.key.get_pressed() # update to respond to pushbutton switch

        player.draw(SCREEN)
        player.update(userInput)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(Cactus(CACTUS))
            elif random.randint(0, 1) == 1:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.snake_rect.colliderect(obstacle.rect):
                # Use to debug hitbox
                # pygame.draw.rect(SCREEN, (255, 0, 0), player.snake_rect, 2)
                pygame.time.delay(1500)
                death_count += 1
                menu(death_count)


        clock.tick(10)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((000, 000, 000))
        font = pygame.font.Font("freesansbold.ttf", 10)

        if death_count == 0:
            text = font.render("Press to Begin", True, (255, 255, 255))
        elif death_count > 0:
            text = font.render("Press to Begin", True, (255, 255, 255))
            score = font.render("Score: " + str(points), True, (255, 255, 255))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10)
            SCREEN.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 16, SCREEN_HEIGHT // 2 + 16))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\user\Desktop\week7\week 8\AnimatedStreet.png")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\week7\week 8\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -random.randint(50, 150))

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = -random.randint(50, 150)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), self.rect.top)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\week7\week 8\coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -random.randint(50, 150))

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -random.randint(50, 150))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\user\Desktop\week7\week 8\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

background_y = 0

def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (130, 250))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:  
                    return True
                elif event.key == K_ESCAPE:  
                    return False

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pygame.sprite.spritecollideany(P1, enemies):
        if not game_over_screen():
            pygame.quit()
            sys.exit()
        else:
            SCORE = 0
            COINS = 0
            SPEED = 10
            P1.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)

    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        C1.respawn()

    background_y = (background_y + SPEED) % SCREEN_HEIGHT
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - SCREEN_HEIGHT))

    scores_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(scores_text, (10, 10))

    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(coins_text, (320, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        if isinstance(entity, Enemy) or isinstance(entity, Coin):
            entity.move()
    
    P1.move()
    pygame.display.update()
    FramePerSec.tick(FPS)

import sys
import pygame
import random


class Dino():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/dino.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx / 2
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.jumping_up = False
        self.droping_down = True

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1

        if self.jumping_up and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= 1

        if self.droping_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)  #这里的blit相当于文本的print，把一个图像打印出来

class Rockbig():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rock_big.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 1200
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        self.rect.centerx -= 1
        if self.rect.centerx < 0:
            self.rect.centerx =1200

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Rocksmall():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rock_small.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 1200
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        self.rect.centerx -= 1
        if self.rect.centerx < 0:
            self.rect.centerx =930

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("jumpy dinosaur")
    bg_color = (230, 230, 230)
    dino = Dino(screen)
    rock_b = Rockbig(screen)
    rock_s = Rocksmall(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dino.moving_right = True
                if event.key == pygame.K_UP:
                    dino.jumping_up = True
                    dino.droping_down = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    dino.moving_right = False
                if event.key == pygame.K_UP:
                    dino.jumping_up = False
                    dino.droping_down = True

        dino.update()
        rock_b.update()
        rock_s.update()
        screen.fill(bg_color)
        dino.blitme()
        rock_s.blitme() or rock_b.blitme()
        pygame.display.flip()


run_game()

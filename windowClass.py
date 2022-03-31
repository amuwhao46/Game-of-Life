import pygame
from cellClass import *
vec = pygame.math.Vector2 #Pygames vector library

class Window:
    #Constructor
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = 800, 400 #Game interface size
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        #Grid
        self.row = 10
        self.col = 10
        self.grid = [[Cell for x in range(self.col)] for x in range(self.row)]
    
    def update(self):
        self.rect.topleft = self.pos


    def draw(self):
        self.image.fill((100, 100, 100))
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

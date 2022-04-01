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
        self.row = 20
        self.col = 40
        self.grid = [[Cell(self.image, x, y) for x in range(self.col)] for y in range(self.row)]
    
    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()


    def draw(self):
        self.image.fill((100, 100, 100))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

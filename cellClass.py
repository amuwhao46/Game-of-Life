import pygame

class Cell:
    #Constructor
    def __init__(self, surface, gridX, gridY):
        self.alive = False
        self.surface = surface
        self.gridX = gridX
        self.gridY = gridY 
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.gridX * 20, self.gridY * 20)

    def draw(self):
        pygame.draw()
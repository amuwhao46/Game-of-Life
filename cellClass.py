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
        if self.alive:
            self.image.fill((0, 0, 0)) #Alive
        else:
            self.image.fill((0, 0, 0)) #Border color
            pygame.draw.rect(self.image, (255, 255, 255), (2, 2, 16, 16)) #Dead cell, and border size
        self.surface.blit(self.image, (self.gridX * 20, self.gridY * 20)) #Shows squares in interface
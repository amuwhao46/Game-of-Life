import pygame
import random

class Cell:
    #Constructor
    def __init__(self, surface, gridX, gridY):
        #self.alive = random.choice([True, False, False, False])
        self.alive = False
        self.surface = surface
        self.gridX = gridX
        self.gridY = gridY 
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.neighbor = []

    def update(self):
        self.rect.topleft = (self.gridX * 20, self.gridY * 20)

    def draw(self):
        if self.alive:
            self.image.fill((255, 255, 255)) #Alive
        else:
            self.image.fill((0, 0, 0)) #Border color
            pygame.draw.rect(self.image, (25, 25, 25), (1, 1, 18, 18)) #Dead cell, and border size
        self.surface.blit(self.image, (self.gridX * 20, self.gridY * 20)) #Shows squar es in interface
    
    def getNeighbor(self, grid):
        #tracks surrounding cells
        neighborList = [[0,1], [1,0], [1,1], [-1,0], [0,-1], [1,-1], [-1,-1], [-1,1]]
        for neigh in neighborList:
            neigh[0] += self.gridX
            neigh[1] += self.gridY
        
        for neigh in neighborList:
            if neigh[0] < 0:
                neigh[0] += 30
            if neigh[1] < 0:
                neigh[1] += 30
            if neigh[0] > 29:
                neigh[0] -= 30
            if neigh[1] > 29:
                neigh[1] -= 30

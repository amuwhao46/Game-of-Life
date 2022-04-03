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
        self.checker = False #looks for adjacent neighbors

    def update(self):
        self.rect.topleft = (self.gridX * 20, self.gridY * 20)
        for cell in self.neighbor:
            if self.alive:
                self.checker = True

    def draw(self):
        if self.alive:
            self.image.fill((255, 255, 255)) #Alive
        else:
            self.image.fill((0, 0, 0)) #Border color
            pygame.draw.rect(self.image, (25, 25, 25), (1, 1, 18, 18)) #Dead cell, and border size
        self.surface.blit(self.image, (self.gridX * 20, self.gridY * 20)) #Shows squar es in interface
    
    #tracks surrounding cells
    def getNeighbor(self, grid):
        neighborList = [[0,1], [1,0], [1,1], [-1,0], [0,-1], [1,-1], [-1,-1], [-1,1]]
        for neighbor in neighborList:
            neighbor[0] += self.gridX #Left to right
            neighbor[1] += self.gridY #Top to bottom
        
        for neighbor in neighborList:
            if neighbor[0] < 0:
                neighbor[0] += 40
            if neighbor[1] < 0:
                neighbor[1] += 20
            if neighbor[0] > 39:
                neighbor[0] -= 40
            if neighbor[1] > 19:
                neighbor[1] -= 20
        for neighbor in neighborList:
            try:
                self.neighbor.append(grid[neighbor[1]][neighbor[0]])
            except:
                print(neighbor)
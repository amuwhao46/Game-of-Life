import pygame
vec = pygame.math.Vector2 #Pygames vector library

class window:

    #Constructor
    def __init__(self, screen, x, y):
        self.screen = screen
        self.width, self.height = 800, 400 #Game interface size
        self.pos = vec(x, y)
    
    def update():
        pass

    def draw():
        pass
    
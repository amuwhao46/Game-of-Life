import sys
import pygame
from windowClass import *

#Constants
WIDTH, HEIGHT = 960, 540
BACKGROUND = (120, 120, 120)
FPS = 60 #Refresh rate

#Functions
def getEvents():
    global running
    for event in pygame.event.get(): #Returns list of events since last call
        if event.type == pygame.QUIT:
             running = False
def update():
    window.update() 

def draw():
    screen.fill(BACKGROUND)
    window.draw()

#Main
pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
window = Window(screen, 80, 120) #positioned center, bottom

running = True
#Checks these on a functions while "running"
while running:
    getEvents()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()
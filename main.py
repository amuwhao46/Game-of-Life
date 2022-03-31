from pickle import TRUE
import sys
from turtle import width
import pygame

#Constants
WIDTH, HEIGHT = 1080, 1080

#Functions
def getEvents():
    global running
    for event in pygame.event.get(): #Returns list of events since last call
        if event.type == pygame.QUIT:
             running = False

def update():
    break 

def draw():
    break

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    getEvents()
    update()
    draw()
pygame.quit()
sys.exit()
import sys
import pygame
from windowClass import *
#from buttonClass import *

#Constants
WIDTH, HEIGHT = 960, 540
BACKGROUND = (120, 120, 120)
FPS = 24 #Refresh rate


#Functions
def getEvents():
    global running
    for event in pygame.event.get(): #Returns list of events since last call
        if event.type == pygame.QUIT:
             running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if mouseOnGrid(mousePos):
                clickCell(mousePos)
                #print(mousePos) #(Debugging)

def update():
    window.update() 
    '''for button in buttons:
        button.update(mousePos)'''
        

def draw():
    screen.fill(BACKGROUND)
    '''for button in buttons:
        button.draw()'''
    window.draw()

#mOG & cC used to track cell click state
def mouseOnGrid(pos):
    if pos[0] > 80 and pos[0] < WIDTH - 80:
        if pos[1] > 120 and pos[1] < HEIGHT - 20:
            return True
        return False

def clickCell(pos):
    grid_pos = [pos[0] - 80, pos[1] - 120]
    grid_pos[0] = grid_pos[0] // 20 #X pos
    grid_pos[1] = grid_pos[1] // 20 #Y pos

    #Sets cell dead/alive when clicked
    if window.grid[grid_pos[1]][grid_pos[0]].alive:
        window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        window.grid[grid_pos[1]][grid_pos[0]].alive = True
    #print("Clicked") #(Debugging)

'''def makeButton():
    buttons = []
    buttons.append(Button(window, WIDTH//2 - 50, 50, 100, 20, text='Run', colour = (10, 140, 30), hover_colour = (40, 180, 70)))
    return buttons'''


#Main
pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
window = Window(screen, 80, 120) #positioned center, bottom
#buttons = makeButton()

running = True
#Checks these on a functions while "running"
while running:
    mousePos = pygame.mouse.get_pos()
    getEvents()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()
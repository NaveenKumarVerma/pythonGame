import pygame, sys
import math
from pygame.locals import *

pygame.init()

white = (255,255,255)
red = (128,0,0)
blue = (0,255,0)
green = (0,0,255)
black = (0,0,0)
light_red = (255,0,0)

display_width = 800
display_height = 600



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chain Reaction')
gameDisplay.fill(white)

def button():
    click = pygame.mouse.get_pressed()
    #u = round((((click[0]/100.0)*100)+100)/2)
    #v = round((((click[1]/100.0)*100)+100)/2)
    pygame.draw.circle(gameDisplay,red,(click[0],click[1]),50,0)
    
def drawGrid(display_width,display_height):
    block_x=100
    block_y=100

    while block_x<display_width:
        pygame.draw.line(gameDisplay, black,(block_x,0),(block_x,display_height))
        block_x = block_x+100

    while block_y < display_height:
        pygame.draw.line(gameDisplay, black,(0,block_y),(display_width,block_y))
        block_y = block_y+100
        
def gameLoop():
    trackX={0:0,100:0,200:0,300:0,400:0,500:0,600:0,700:0}
    trackY={0:0,100:0,200:0,300:0,400:0,500:0}
    drawGrid(display_width,display_height)    
    pygame.display.update()
    
    #pygame.draw.rect(gameDisplay,green,((round((cur[0]/100.0)*100),round((cur[1]/100.0)*100)),100,100))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        u = int(math.floor(cur[0]/100.0))*100
        v = int(math.floor(cur[1]/100.0))*100
        
        if click[0] == 1 and trackX[u]==0 and trackY[v]==0:
            trackX[u]=1
            trackY[v]=1
            pygame.draw.ellipse(gameDisplay,light_red,(u,v,100,100))
            pygame.display.update()
        if trackX[u] == 1 and trackY[v] == 1 and click[0] == 1:
            if (u == 0 and v == 0) or (u == 0 and v == 500) or(u == 700 and v == 0) or(u == 700 and v == 500):
                trackX[u]=2
                trackY[v]=2
            else :
                trackX[u]=1
                trackY[v]=1
            pygame.draw.ellipse(gameDisplay,black,(u+25,v+25,75,75))
            pygame.display.update()
            
            
#    button()
        
    pygame.display.update()
gameLoop()
#def drawGrid(display_width,display_height):
##    x,y=100,100
##    for x in range(100,800):
##        pygame.draw.line(gameDisplay, black,(x,0),(x,600))
##        x+=100
##    for y in range(100,600):
##        pygame.draw.line(gameDisplay, black,(0,y),(800,y))
##        y+=100
##
##def gameLoop():
##    drawGrid(display_width,display_height)
##    pygame.display.update();
##
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit()





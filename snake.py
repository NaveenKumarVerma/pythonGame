import pygame
import time
import random
from pygame.locals import *


pygame.init()

white = (255,255,255)
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)
black = (0,0,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither') #title for the project

pygame.display.update() #To update the frame


clock = pygame.time.Clock()
block_size = 10
FPS = 5

font = pygame.font.SysFont(None, 25)


def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, black,[XnY[0],XnY[1],block_size,block_size])
        
def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color):
    textSurf, textRect = text_objects(msg ,color)
##    screen_text = font.render(msg,True,color)
##    gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    textRect.center = (display_width/ 2),(display_height / 2)
    gameDisplay.blit(textSurf,textRect)


def gameLoop():
      
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0,display_width-block_size)) #/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0

    while not gameExit:
        while gameOver == True:
            message_to_screen("Game Over,Press q to Quit and c to play again",red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == K_c:
                        gameLoop()



        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == K_UP:
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == K_DOWN:
                    lead_x_change = 0
                    lead_y_change = block_size
                    
#in order to make the snake stationary if any of the button is
#not pressed remove the below code from comments
##            if event.type == pygame.KEYUP:
##                if event.key == K_LEFT or event.key ==  K_RIGHT:
##                    lead_x_change=0
##                elif event.key == K_UP or event.key == K_DOWN:
##                    lead_y_change=0

        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0: #boundary
                gameOver = True
                
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
        gameDisplay.fill(white)

        AppleThickness = 20
        pygame.draw.rect(gameDisplay, red,[randAppleX,randAppleY,AppleThickness,AppleThickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength :
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeLength:
                gameOver = True
                
        snake(block_size, snakeList)
        
        pygame.display.update() #To update the frame

##        if lead_x == randAppleX and lead_y ==randAppleY:
##            randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
##            randAppleY = round(random.randrange(1,display_height-block_size)/10.0)*10.0
##            snakeLength+=1


        
        

##
##        if lead_x >= randAppleX and lead_x<=randAppleX+AppleThickness:
##            if lead_y >= randAppleY and lead_y<=randAppleY+AppleThickness:
##                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(1,display_height-block_size))#/10.0)*10.0
##                snakeLength+=1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(1,display_height-block_size))#/10.0)*10.0
                snakeLength+=1
              
                          
        clock.tick(FPS)



    message_to_screen("You lose",red)
    pygame.display.update() #To update the frame
    time.sleep(2)
    pygame.quit()
    quit()

gameLoop()


import pygame
import time
import random
from pygame.locals import *


pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)
black = (0,0,0)

display_width = 800
display_height = 600



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither') #title for the project


snakehead = pygame.image.load("snakehead.png")
icon = pygame.image.load("snakehead.png")

pygame.display.set_icon(icon)
pygame.display.update() #To update the frame


clock = pygame.time.Clock()
block_size = 20
FPS = 10

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)



def snake(block_size, snakelist):
    if direction == "right":
       head = pygame.transform.rotate(snakehead,270)
    if direction == "left":
       head = pygame.transform.rotate(snakehead,90)
    if direction == "up":
       head = snakehead
    if direction == "down":
       head = pygame.transform.rotate(snakehead,180)
       
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green,[XnY[0],XnY[1],block_size,block_size])
        
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
         textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)    
    
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf, textRect = text_objects(msg ,color,size)
    textRect.center = (display_width/ 2),(display_height / 2)+y_displace
    gameDisplay.blit(textSurf,textRect)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    quit()
                if event.key == K_c:
                    intro = False

        
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          "large")
        message_to_screen("Objective of the game is to eat the red apples",
                          black,
                          -30,
                          "small")
        message_to_screen("The more apples you eat ,the longer you get",
                          black,
                          10,
                          "small")
        
        message_to_screen("If you run over the bpundaries ,you will DIE",
                          red,
                          50,"small")
        
        message_to_screen("Press C to PLAY or Q to QUIT",
                          black,
                          180,
                          "small")
        pygame.display.update()
        clock.tick(15)


def gameLoop():
    global direction
    #global FPS
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0,display_width-block_size)) #/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0

    while not gameExit:
        while gameOver == True:
            message_to_screen("Game Over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press C to Play and Q to Quit",
                              black,
                              50,
                              size="medium")
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
                    direction= "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction= "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == K_UP:
                    direction= "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == K_DOWN:
                    direction= "down"
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

        AppleThickness = 30
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
##              
##        if(snakeLength%10 == 0):
##            FPS+=2
        clock.tick(FPS)



    message_to_screen("You lose",red,-50,"large")
    pygame.display.update() #To update the frame
    time.sleep(1)
    pygame.quit()
    quit()

game_intro()
gameLoop()


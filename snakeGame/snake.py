#!/usr/bin/env python

import pygame
import time
import random
import math
from pygame.locals import *


pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)
black = (0,0,0)
yellow = (255,255,0)

display_width = 800
display_height = 600



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither') #title for the project


snakehead = pygame.image.load("snakehead.png")
icon = pygame.image.load("snakehead.png")
apple = pygame.image.load("apple.png")

pygame.display.set_icon(icon)#To set icon
pygame.display.update() #To update the frame


clock = pygame.time.Clock()
block_size = 20
FPS = 10

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def wall():
    pygame.draw.rect(gameDisplay, yellow,[210,200,block_size*20+1,block_size+10])
    pygame.draw.rect(gameDisplay, yellow,[210,400,block_size*20+1,block_size+10])
    pygame.draw.rect(gameDisplay, yellow,[0,0,display_width,block_size])#upper boundary
    pygame.draw.rect(gameDisplay, yellow,[0,0,block_size,display_height])#left boundary
    pygame.draw.rect(gameDisplay, yellow,[display_width-block_size,0,block_size,display_height])#right boundary
    pygame.draw.rect(gameDisplay, yellow,[0,display_height-block_size,display_width,block_size])#bottom boundary
    
    
    pygame.display.update()

#def randApple():
    
    



def pause():
    paused = True
    message_to_screen("Pause",
                      black,
                      -100,
                      size="large")
    
    message_to_screen("Press C to continue or Q to Quit",
                      black,
                      25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    paused = False

                elif event.key == K_q:
                    pygame.quit()
                    quit()


        clock.tick(5)
        
def score(score):
  
    Score_text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(Score_text, [0,0])
    
##def level(level):
##    level = int((math.log(snakeLength))/((math.log(2))))
##    level = level - 2
##    if level < 2:
##        level_text = smallfont.render("Level:  1", True, black)
##    else:
##        level_text = smallfont.render("Level: "+str(level), True, black)
##    gameDisplay.blit(level_text,[0,30])
    


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
        message_to_screen("Objective of the Game is to eat the RED Apples",
                          black,
                          -30,
                          "small")
        message_to_screen("The more Apples you eat ,the LONGER you get",
                          black,
                          10,
                          "small")
        
        message_to_screen("If you Run Over the Boundaries ,you will DIE",
                          red,
                          50,"small")
        
        message_to_screen("Press C to PLAY ,P to Pause and Q to QUIT",
                          black,
                          180,
                          "small")
        pygame.display.update()
        clock.tick(15)


def gameLoop():
    global direction
    global FPS
    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    randAppleX = round(random.randrange(0,display_width-block_size)) 
    randAppleY = round(random.randrange(0,display_height-block_size))
    
    if (610 >= randAppleX >= 190 and (230 >= randAppleY >= 190 or 430 >= randAppleY >= 390)):
        gameLoop()
    if  20 >= randAppleX >= 0 or 800 >= randAppleX >= 780 or 20 >= randAppleY >= 0 or randAppleX == 580 :
        gameLoop()
    if 800 >= randAppleX >= 0 and (30 >= randAppleY >= 0 or 600 >= randAppleX >= 570 ) :
        gameLoop()
    if (30 >= randAppleX >= 0 or 800 >= randAppleX >= 770 ) and 600 >= randAppleY >= 0 :
        gameLoop()
    
        
    
    while not gameExit:
        if gameOver == True:
            FPS = 10
            #gameDisplay.fill(white)
            message_to_screen("Game Over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press C to Play and Q to Quit ",
                              black,
                              50,
                              size="medium")
            pygame.display.update()
        while gameOver == True:
            
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
                if event.key == K_LEFT or event.key == K_a:
                    direction= "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == K_d:
                    direction= "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == K_UP or event.key == K_w:
                    direction= "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == K_DOWN or event.key == K_s:
                    direction= "down"
                    lead_x_change = 0
                    lead_y_change = block_size
                    


                elif event.key == K_p:
                    pause()
        if lead_x >= display_width - 20 or lead_x < 20 or lead_y >= display_height - 20 or lead_y < 20: #boundary
            gameOver = True

        if (600 >= lead_x >= 200 and (220 >= lead_y >= 200 or 420 >= lead_y >= 400)) :
            gameOver = True
        
##        if (lead_x>200 or lead_x<400) or (lead_y>200 or lead_y<400 ):
##            gameover = True
##                
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
        gameDisplay.fill(white)

        AppleThickness = 20
        wall()
        
        gameDisplay.blit(apple,(randAppleX, randAppleY))




        
        
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

        score(snakeLength-1)
        pygame.display.update() #To update the frame

        #level(snakeLength)
        
        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness or lead_x + block_size >= randAppleX and lead_x + block_size <= randAppleX + AppleThickness:
             if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness or lead_y + block_size >= randAppleY and lead_y + block_size <= randAppleY + AppleThickness:
                 randAppleX = round(random.randrange(0,display_width-block_size))
                 randAppleY = round(random.randrange(1,display_height-block_size))
                 snakeLength+=1
        
        
        clock.tick(FPS)        



    message_to_screen("You lose",red,-100,"medium")
    message_to_screen("Your Score is "+str(snakeLength-1),green,-50,"medium")

    pygame.display.update() #To update the frame
    time.sleep(1)
    pygame.quit()
    quit()

game_intro()

gameLoop()


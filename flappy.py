import pygame as pyg
import random

#initialize pygame
pyg.init()

#define colours
black = (0,0,0)
blue = (0,0,225)
white = (225,225,225)
red =(255,0,0)
lightblue = (224,255,255)

#create the window size
display_width = 1000
display_height = 300
display = pyg.display.set_mode((display_width,display_height))
pyg.display.set_caption("Flappy Bird")
display.fill(white)

#set up the bird
bird_height = 20
bird_width = 30
bird_speed = 0
bird_pull = 1

#obstacles
bricki_xpos = display_width
brickii_xpos = display_width
bricki_ypos = 0 
# brickii_ypos = 
# brick_width = 

#define variables
game_start = True
game_over = False
#clock = pyg.time.Clock()

#define functions

#game loop
while game_start:
    
    for event in pyg.event.get():
        #checks if the user clicked the window close button
        if event.type == pyg.QUIT:
            exit()
        # else:    
        #note the user can only move up while the game hopes they fall or hits something    
            #if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    #if event.key == pyg.K_UP:
                    
    #fill up the background with a white color
    display.fill(white)
    #draws a simple bird
    #pygame.draw."shape"("where to draw","color",["fromleft to right(0 - display with)","from top to bottom(0 - height)","width","height"]
    pyg.draw.rect(display, black, [50,130,bird_width,bird_height])
    #drawing the vertical starting line
    pyg.draw.rect(display,lightblue , [90,0,10,800])
    pyg.draw.rect(display,red, [200,200,10,20])
    #clock.tick(60)    
    #flip the display
    pyg.display.flip()
#quit the game
pyg.quit()    

import pygame
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,128,0)
grey=(169,169,169)
wheat=(245,222,179)

display_width = 800
display_height = 600
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game - Amar')

icon=pygame.image.load('ic.jpg')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

block_size=10

smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("Yu Mincho Demibold",80)

def score(score):
    text=smallfont.render("Score: "+str(score)+"                                            "
                                               "                            Press p to pause",True,black,"small")
    gamedisplay.blit(text,[0,0])


def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gamedisplay, black, [XnY[0],XnY[1], block_size, block_size])

def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    if size=="med":
        textSurface=medfont.render(text,True,color)
    if size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0,size=""):
    textSurf , textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2),(display_height/2)+y_displace
    gamedisplay.blit(textSurf,textRect)
    #screen_text=font.render(msg,True,color)
    #gamedisplay.blit(screen_text,[300,300])


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        gamedisplay.fill(wheat)
        message_to_screen("PAUSED",black,-100,"large")
        message_to_screen("Press C to continue or Q to quit",black,25,"small")
        pygame.display.update()
        clock.tick(5)

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    intro = False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        gamedisplay.fill(black)
        message_to_screen("Welcome" , red ,-100,"large")
        message_to_screen("Objective is to eat RED block", grey, 40, "small")
        message_to_screen("The more block you eat the longer snake becomes", grey,90,"small")
        message_to_screen("If you run into youself or in the boundries , YOU DIE!! ", grey,140, "small")
        message_to_screen("Press P to play or Q to Exit ", white, 210, "med")
        message_to_screen("Created by - Amar Kumar ", white, 280, "small")
        pygame.display.update()
        clock.tick(8)


def gameLoop():
    gameExit=False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change=0
    lead_y_change=0

    snakelist = []
    snakelength=1

    randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10.0

    while not gameExit:
        while gameOver == True:
            gamedisplay.fill(black)
            message_to_screen("GAME OVER", red , y_displace=-80,size="large")
            message_to_screen("Press C to Continue or  Q to Quit", white, y_displace=50,size="small")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver= False
                    gameExit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -10
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gamedisplay.fill(white)
        pygame.draw.rect(gamedisplay,red,[randAppleX,randAppleY,block_size,block_size])


        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist)>snakelength:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
               gameOver = True
        snake(block_size, snakelist)
        score(snakelength-1)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            snakelength += 1

        clock.tick(10)

    pygame.quit()
    quit()

game_intro()
gameLoop()
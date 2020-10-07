# importing modules
import pygame
import random
import math
from pygame import mixer


# initializing it
pygame.init()

# starting the display
start = pygame.display.set_mode((600, 600))


# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)


# background
bg = pygame.image.load('asas.jpg')


# bullet
drop = pygame.image.load('h.png')
e = 0
f = 480

#this is used to change the speed of bullet
bulletchange = 10

#this is to reload the bullet in bottle
dropmode = "ready"


# titles and icons etc all that stuff
pygame.display.set_caption("Ramen Warriors!")
icon = pygame.image.load('breakfast.png')
pygame.display.set_icon(icon)


# MILKBOTTLE
bottle = pygame.image.load('feeding-bottle.png')
a = 280
b = 500
x = 0
g = 0


#COUNTING SCORE
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)


#Enemy variables
c = []
d = []
enemychange = []


# GAME OVER
lafont = pygame.font.Font('freesansbold.ttf', 70)


# Targets for shooting
cereal = []


#creating a list of enemies by using loop function
noofenemies = 3
for i in range(noofenemies):
    cereal.append(pygame.image.load('soup.png'))
    c.append(random.randint(0, 570))
    d.append(random.randint(30, 200))
    enemychange.append(4)


# positioning Game over text
def gameo():
    go = lafont.render("GAME OVER! ", True, (255, 255, 255))
    start.blit((go), (75, 200))
    la = True


#positioning the ketchup bottle
def milkbottle(a, b):
    start.blit((bottle), (a, b))


#positioning the enemies
def cereals(c, d, i):
    start.blit((cereal[i]), (c, d))

#positioning the bullets-ketchup drop
def bullets(x, y):
    global dropmode
    dropmode = "fire"
    start.blit((drop), (x, y))

#positioning the score count
def showscore():
    scr = font.render("Score:- " + str(score), True, (255, 255, 255))
    start.blit((scr), (10, 10))

#collision detection function
def collisionoccured(e, f, c, d):

    #maths formula to detect the proximity of the bullet

    dist = math.sqrt(math.pow((e - c), 2) + math.pow((f - d), 2))
    if dist <= 40:
        return True
    else:
        return False


# Game loop-> the loop which runs infinie time until the game has been closed
running = True
while running == True:
    for event in pygame.event.get():

        # condition  for closing the game because it has to be closed one day


        if event.type == pygame.QUIT:
            running = False



        # movement of object i.e ketchup bottle

        #assigning movements key wise

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = -4
            if event.key == pygame.K_RIGHT:
                x = +4
            if event.key == pygame.K_SPACE:
                if dropmode == "ready":
                    bulletsound = mixer.Sound('laser.wav')
                    bulletsound.play()
                    bullets(e, f)
                    e = a



        # to stop the continuous movement of object


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                g = 0
                x = 0


    # setting bg colour
    start.fill((0, 0, 0))

    #setting background image

    start.blit((bg), (0, 0))


    # various object conditions


    #bullet reset condition
    if f <= 0:
        f = 490
        dropmode = "ready"



    #bullet movement condition
    if dropmode == "fire":
        bullets(e, f)
        f -= bulletchange


    #condition to prevent the main object to go outside the game zone
    if a <= 0:
        a = 0;
    if a >= 570:
        a = 570


    #Gameover condition to basically stop the game
    for i in range(noofenemies):
        if d[i] >= 430:
            for j in range(noofenemies):
                d[j] = 2000


        #game over text function
            gameo()

            break


# to  detect if the collision occured

        #Using loop to detect collision occured for each enemy


        collision = collisionoccured(e, f, c[i], d[i])

        c[i] += enemychange[i]
        d[i] += 0.5
        if c[i] <= 0:
            enemychange[i] = 8
            # d+=30
        elif c[i] > 570:
            enemychange[i] = -8
            # d+=30
        if collision:
            coll = mixer.Sound('explosion.wav')
            coll.play()
            f = 490
            dropmode = "ready"
            score += 1
            c[i] = random.randint(0, 570)
            d[i] = random.randint(30, 200)
        cereals(c[i], d[i], i)
    a += x
    b += g
    milkbottle(a, b)


    showscore()




    # screen updater
    pygame.display.update()


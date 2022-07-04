import pygame
import random
import math
from pygame import mixer

pygame.init()

screen =  pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)


# Icon
pygame.display.set_caption('Invaders Game')


#player
playerImg = pygame.image.load('player.png')
playerX, playerY = 370, 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 3, 30

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 10
bullet_state = 'ready'

#Score
score_value = 0

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16,  y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY , 2))
    if distance < 27: 
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change =  5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()

                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736   

    #Enemy
    if enemyY > 440:
        break
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change = -3
        enemyY += enemyY_change 

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    #Bullet Movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #Score
    font = pygame.font.SysFont(None, 32)
    score = font.render(f"Score : {str(score_value)} " , True,(255,255,255))
    screen.blit(score, (20,50))

    player(playerX, playerY)  
    enemy(enemyX, enemyY)

    pygame.display.update()







 
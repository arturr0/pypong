import math
import random
import sys
import pygame
import random
import tkinter as tk
from tkinter import messagebox
left = False
right = True
up = False
down = False
x1 = 0
y1 = 0
x2 = 20
y2 = 60
class Ball:
    x = 400
    y = 300
    speedx = 15
    speedy = 3
class Player():
    def __init__(self):
        x = 0
        y = 0
    speed = 8
    up = False
    down = True

def MoveBall(ball):
    global left
    global right
    global up
    global down
    if (left == True and right == False and up == False and down == False):
        ball.x -= ball.speedx
        ball.y -= ball.speedy
    elif (right == True and left == False and up == False and down == False):
        ball.x += ball.speedx
        ball.y -= ball.speedy
    elif (down == True):
        ball.y += ball.speedy
        if (left == True):
            ball.x -= ball.speedx
        elif (right == True):
            ball.x += ball.speedx
    elif (up == True):
        ball.y -= ball.speedy
        if (left == True):
            ball.x -= ball.speedx
        elif (right == True):
            ball.x += ball.speedx
    #collide pallete
    if (ball.x - 5 <= 20):
        right = True
        left = False
    elif (ball.y - 5 < 0):
        down = True
    elif (ball.x + 5 >= 800):
        right = False
        left = True
        
    elif (ball.y + 5 > 600):
        up = True
        down = False
    if (ball.x < 0):
        ball.x = 400
        ball.y = 300
def MoveComputer(computer, computer2, ball):
    if (ball.x > 60 and left):
        if (ball.y > computer.y+60):
            computer.up = False
            computer.down = True
        elif (ball.y < computer.y):

            computer.up = True
            computer.down = False
        if (computer.up):
            computer.y -= computer.speed
            #computer.y1 -= computer.speed
        elif (computer.down):
            computer.y += computer.speed;
            #computer.y1 += computer.speed;
    elif (ball.x < 840 and right):
        if (ball.y > computer2.y+60):
            computer2.up = False
            computer2.down = True
        elif (ball.y < computer2.y):

            computer2.up = True
            computer2.down = False
        if (computer2.up):
            computer2.y -= computer2.speed
            #computer.y1 -= computer.speed
        elif (computer2.down):
            computer2.y += computer2.speed;
x = 0
FPS = 60.0
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
delta = 0.0
ball = Ball
computer = Player() 

computer.x = 0
computer.y = 0
#computer.speed = 8
computer2 = Player() 

computer2.x = 780
computer2.y = 0
#computer2.speed = 8


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    delta += clock.tick()/1000.0
    while delta > 1/FPS:
        delta -= 1/FPS
        MoveBall(Ball)
        MoveComputer (computer,computer2,Ball)
        
    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0), (ball.x, ball.y), 10)
    pygame.draw.rect (screen, (255,0,0),pygame.Rect(computer.x,computer.y,20,60))
    pygame.draw.rect (screen, (255,0,0),pygame.Rect(computer2.x,computer2.y,20,60))

    pygame.display.flip()



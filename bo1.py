from pygame import *
from pygame.sprite import *
import pygame
import math 
import time 
import random 
import os, sys
from pygame.locals import *


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (70,130,180)
green = (127,255,212)
Width = 800
Height = 600
x_pos = 350
y_pos = 580
# x = 400
# y = 300
# a = 400
# b = 400


 
class Paddle(pygame.sprite.Sprite):


	def __init__(self):
		pygame.sprite.Sprite. __init__ (self)
		self.width = 100
		self.height = 20
		self.image = pygame.Surface([self.width,self.height])
		self.image.fill(blue)

		self.rect = self.image.get_rect()
		self.rect.x = x_pos
		self.rect.y = y_pos

	def update(self):
		self.rect.x = x_pos
		screen.fill(white)
	

class Block(pygame.sprite.Sprite):
 
    def __init__(self, color, x, y):
        pygame.sprite.Sprite. __init__ (self)

        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Falling(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30,40))
		self.image.fill(red)
		self.rect = self.image.get_rect()
	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.range(0, Height)

	def update(self):
		self.rect.y += 3
		if self.rect.y>610:
			self.back_to_top()
# class Mob(pygame.sprite.Sprite):
#     # mob sprite - spawns above top and moves downward
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((30, 40))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(Width - self.rect.width)
#         self.rect.y = random.randrange(-80, -50)
#         self.speedy = random.randrange(1, 8)

#     def update(self):
#         self.rect.y += self.speedy
#         if self.rect.top > Height + 10:
#             self.rect.y = random.randrange(-80, -50)
#             self.rect.x = random.randrange(WIDTH - self.rect.width)
#             self.speedy = random.randrange(1, 8)		

init()
top = 50
blockcount = 32
block_width = 100
block_height = 20

clock = pygame.time.Clock()


blocks = pygame.sprite.Group()
sprites = pygame.sprite.Group()
# ball = Ball()
# sprites.add(ball)
paddle = Paddle()
sprites.add(paddle)
 
falling = pygame.sprite.Group()
falling = Falling()
sprites.add(falling)

for row in range(5):
    for column in range(0, blockcount):
        block = Block(green, column * (block_width + 2) , top)
        blocks.add(block)
        sprites.add(block)
    top += block_height + 2
gameDisplay = pygame.display.set_mode((Width, Height))
screen = gameDisplay


pygame.display.set_caption("Jack's Project")

screen.fill(white)



gameExit = False
mixer.music.load("closer.wav")
mixer.music.play(-1)

while not gameExit:
	# Ball()
	# Paddle()
	# Block()
	
	clock.tick(50)

	
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_pos -= 10
		if event.key == pygame.K_RIGHT:
			x_pos += 10


	sprites.update()
	sprites.draw(screen)
	pygame.display.update()		




#required
pygame.quit()
quit()	





# class Ball(pygame.sprite.Sprite):


#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.speed = 10.0
#         self.width = 20
#         self.x = 0.0
#         self.y = 200.0
#         self.height = 20
#         self.direction = 180

#         self.image = pygame.Surface([self.width, self.height])
#         self.image.fill(black)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
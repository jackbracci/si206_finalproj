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
speed = 5 
x_pos = 350
y_pos = 580

# x = 400
# y = 300
# a = 400
# b = 400


 
class Paddle(pygame.sprite.Sprite):


	def __init__(self):
		pygame.sprite.Sprite. __init__ (self)
		self.width = 40
		self.height = 40
		self.image = pygame.Surface([self.width,self.height])
		self.image.fill(blue)

		self.rect = self.image.get_rect()
		self.rect.x = x_pos
		self.rect.y = y_pos

	def update(self):
		self.rect.x = x_pos
		screen.fill(black)
	

class Block(pygame.sprite.Sprite):
 
    def __init__(self, color, x, y):
        pygame.sprite.Sprite. __init__ (self)

        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Bullet(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([4, 10])
        self.image.fill(red)

        self.rect = self.image.get_rect()

    def update(self):



        self.rect.y -= 10

class Falling(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30,40))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(Width - self.rect.width)
	def back_to_top(self):
		self.rect.y = random.randrange(-400, -50)
		self.rect.x = random.randrange(0, Height)

	def update(self):
		self.rect.y += 15
		if self.rect.y>610:
			self.back_to_top()

class Score(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.score = 0
		self.font = pygame.font.SysFont('monospace', 20)

	def draw(self, screen):
		txt = self.font.render("SCORE:" + str(self.score) + " Lives 1", True, white)
		screen.blit(txt, (0, 0))

	def add(self):
		self.score += 1

	def val(self):
		return self.score

	def gameover(self, screen):
		txt = self.font.render('GAMEOVER! You Scored ' + str(self.score)+ ' points!', True , white)
		screen.blit(txt, (400 - txt.get_width() / 2, 100))


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
block_width = 50
block_height = 20
f = font.Font(None, 25)
clock = pygame.time.Clock()

bullet = pygame.sprite.Group()
blocks = pygame.sprite.Group()
sprites = pygame.sprite.Group()
# ball = Ball()
# sprites.add(ball)
score = Score()
paddle = Paddle()
sprites.add(paddle)
bullet_list = pygame.sprite.Group()
falling = pygame.sprite.Group()
# falling = Falling()
sprites.add(falling)

for row in range(5):
    for column in range(0, blockcount):
        block = Block(green, column * (block_width + 2) , top)
        blocks.add(block)
        sprites.add(block)
    top += block_height + 2
gameDisplay = pygame.display.set_mode((Width, Height))
screen = gameDisplay

for i in range(10):
	fall = Falling()
	sprites.add(fall)
	falling.add(fall)

pygame.display.set_caption("Jack's Project")

screen.fill(white)



gameExit = False
game_over = False
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
		elif event.type == pygame.MOUSEBUTTONDOWN:
			bullet = Bullet()
			bullet.rect.x = paddle.rect.x
			bullet.rect.y = paddle.rect.y
			sprites.add(bullet)
			bullet_list.add(bullet)

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_pos -= 10
		if event.key == pygame.K_RIGHT:
			x_pos += 10

	for bullet in bullet_list:
		block_hit_list = pygame.sprite.spritecollide(bullet, blocks, True)

		for block in block_hit_list:
			bullet_list.remove(bullet)
			sprites.remove(bullet)
			score.add()
			
			# score += 1 
			# print (score)
		if bullet.rect.y < -10:
			bullet_list.remove(bullet)
			sprites.remove(bullet)

	if pygame.sprite.spritecollide(bullet,sprites):
		game_over = True
	if game_over == True:
		score.gameover(screen)



	t = f.render("Score = " + str(score), False, (0,0,0))
	screen.blit(t, (320, 0))

	sprites.update()
	sprites.draw(screen)
	score.draw(screen)
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
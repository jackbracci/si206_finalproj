from pygame import *
from pygame.sprite import *
import pygame
import math 
import time 
import random 
import os, sys
from pygame.locals import *

# Attributes used in classes
myname = input("Write your Name")
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (70,130,180)
green = (127,255,212)
Width = 800
Height = 600
# speed = 5 
x_pos = 350
y_pos = 580


init()
 
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
		if self.rect.right > Width:
			self.rect.right = Width
		if self.rect.left < 0:
			self.rect.left = 0
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

	def fall_collide_with(self, paddle):
		if self.rect.colliderect(paddle.rect) == True:
			game_over = True

	def update(self):
		self.rect.y += 20
		if self.rect.y>610:
			self.back_to_top()

class Score(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.score = 0
		self.life = 3
		self.font = pygame.font.SysFont('monospace', 20)

	def draw(self, screen):
		txt = self.font.render("SCORE:" + str(self.score) + " Lives 1", True, white)
		screen.blit(txt, (0, 0))

	def add(self):
		self.score += 1
		if self.score == 1: 
			txt = self.font.render('Half Way There with ' + str(self.score)+ ' points!', True , white)
			screen.blit(txt, (200, 300)) 
			score.draw(screen)
			pygame.display.update()
			pygame.time.delay(4000)
			WIN = True

	def lose(self):
		self.life -=1

	def gameover(self, screen):
		txt = self.font.render('GAMEOVER! You Scored ' + str(self.score)+ ' points!', True , white)
		screen.blit(txt, (250 , 300)) 
		score.draw(screen)
		pygame.display.update()
		print('bye') 
		pygame.time.delay(2000)



	



#Sprite Groups
bullet = pygame.sprite.Group()
blocks = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
falling = pygame.sprite.Group()
sprites = pygame.sprite.Group()

#Class call variable
fall = Falling()
score = Score()
paddle = Paddle()

#Add sprites
sprites.add(paddle)
sprites.add(falling)
sprites.add(fall)


#Attributes for the blocks at the top that get passed through the for loop
top = 50
blockcount = 32
block_width = 50
block_height = 20

#Create the rows of blocks at the top of the screen
for row in range(5):
    for column in range(0, blockcount):
        block = Block(green, column * (block_width + 2) , top)
        blocks.add(block)
        sprites.add(block)
    top += block_height + 2
gameDisplay = pygame.display.set_mode((Width, Height))
screen = gameDisplay

# Iteration to cycle through falling class to generate multiple falling blocks
for i in range(16):
	fall = Falling()
	sprites.add(fall)
	falling.add(fall)

#Display settings for pygame
pygame.display.set_caption("Jack's Project")
screen.fill(white)
f = font.Font(None, 25)
clock = pygame.time.Clock()

end_it=False

while (end_it==False):
    screen.fill(black)
    myfont=pygame.font.SysFont("Britannic Bold", 30)
    welcome=myfont.render("Welcome "+myname+" click to start", 1, (70,130, 180))
    appendix = myfont.render("Controls: Space bar = fire, left_key = move left. right_key = move right", 1 , (70,130,180))
    objective = myfont.render("Objectives: Dodge the falling blocks and shoot the blocks above", 1, (70,130,180))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            end_it=True
    screen.blit(welcome,(250,200))
    screen.blit(appendix, (50, 300))
    screen.blit(objective, (50, 330))
    pygame.display.flip()

#To play music 
pygame.mixer.music.load("closer.wav")
pygame.mixer.music.play(-1)
bomb = pygame.mixer.Sound("bomb.wav")
laser = pygame.mixer.Sound("laser.wav")
#Game set variables
gameExit = False
game_over = False


while not gameExit:

	
	clock.tick(30)

	
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				laser.play()
				bullet = Bullet()
				bullet.rect.x = paddle.rect.x + paddle.width/2
				bullet.rect.y = paddle.rect.y
				sprites.add(bullet)
				bullet_list.add(bullet)
			if event.key == pygame.K_LEFT:
				x_pos -= 20
			if event.key == pygame.K_RIGHT:
				x_pos += 20

	for hit in falling:
		if paddle.rect.colliderect(hit):
			print("Hello")
			game_over = True

	if game_over == True:
		print("HI")
		score.gameover(screen)
		break


	for bullet in bullet_list:
		block_hit_list = pygame.sprite.spritecollide(bullet, blocks, True)

		for block in block_hit_list:
			bullet_list.remove(bullet)
			sprites.remove(bullet)
			bomb.play()
			score.add()

			
			# score += 1 
			# print (score)
		if bullet.rect.y < -10:
			bullet_list.remove(bullet)
			sprites.remove(bullet)


	sprites.update()
	sprites.draw(screen)
	score.draw(screen)
	pygame.display.update()		

pygame.quit()
quit()	
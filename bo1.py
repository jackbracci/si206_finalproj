import pygame
import math 
pygame.init();

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (70,130,180)
green = (127,255,212)
Width = 800
Height = 600
x_pos = 350
y_pos = 580
x = 400
y = 300



 
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
	

class Ball(pygame.sprite.Sprite):
	degree = 180 
	speed = 10

	def __init__(self):
		pygame.sprite.Sprite. __init__ (self)
		self.width = 15
		self.height = 15
		self.image = pygame.Surface([self.width,self.height])
		self.image.fill(blue)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


class Block(pygame.sprite.Sprite):
 
    def __init__(self, color, x, y):
        pygame.sprite.Sprite. __init__ (self)

        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


top = 50
 
# Number of blocks to create
blockcount = 32
 
block_width = 100
block_height = 20

clock = pygame.time.Clock()

blocks = pygame.sprite.Group()
sprites = pygame.sprite.Group()
ball = Ball()
sprites.add(ball)
paddle = Paddle()
sprites.add(paddle)
 

for row in range(5):
    for column in range(0, blockcount):
        block = Block(green, column * (block_width + 2) , top)
        blocks.add(block)
        sprites.add(block)
    top += block_height + 2
gameDisplay = pygame.display.set_mode((Width, Height))
screen = gameDisplay


pygame.display.set_caption("Breakout Project")

screen.fill(white)

gameExit = False

while not gameExit:
	# Ball()
	# Paddle()
	# Block()
	
	#clock.tick(0)
	
	
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
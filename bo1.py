import pygame
import math 
pygame.init();

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (125,175,125)
Width = 800
Height = 600
x_pos = 350
y_pos = 580
x = 400
y = 300



 
class Paddle(pygame.sprite.Sprite):


	def __init__(self):
		super().__init__()
		self.width = 100
		self.height = 20
		self.image = pygame.Surface([self.width,self.height])
		self.image.fill(blue)

		self.rect = self.image.get_rect()
		self.rect.x = x_pos
		self.rect.y = y_pos

	def update(self):
		# self.rect.x = x_pos
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			self.x_pos -= 10
		#if event.key == pygame.K_RIGHT:
			# paddle.self.x_pos+= 10

class Ball(pygame.sprite.Sprite):
	degree = 180 
	speed = 10

	def __init__(self):
		super().__init__()
		self.width = 15
		self.height = 15
		self.image = pygame.Surface([self.width,self.height])
		self.image.fill(blue)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


class Block(pygame.sprite.Sprite):
 
    def __init__(self, color, x, y):
        super().__init__()

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
# --- Create blocks
 
# Five rows of blocks
for row in range(5):
    # 32 columns of blocks
    for column in range(0, blockcount):
        # Create a block (color,x,y)
        block = Block(green, column * (block_width + 2) , top)
        blocks.add(block)
        sprites.add(block)
    # Move the top of the next row down
    top += block_height + 2
gameDisplay = pygame.display.set_mode((Width, Height))
screen = gameDisplay
screen.fill(black)

pygame.display.set_caption("Breakout Project")



gameExit = False

while not gameExit:
	Ball()
	Paddle()
	# Block()
	# Paddle.update()
	
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	
	# if event.type == pygame.KEYDOWN:
		# if event.key == pygame.K_LEFT:
		# 	paddle.self.x_pos -= 10
		# if event.key == pygame.K_RIGHT:
		# 	paddle.self.x_pos+= 10


	sprites.update()
	sprites.draw(screen)
	pygame.display.update()		




#required
pygame.quit()
quit()	
import pygame
pygame.init();

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
Width = 800
Height = 600
x_pos = 350
y_pos = 580
x = 400
y = 300
clock = pygame.time.Clock()
paddle_speed = 10
Bricknum = 30
gameDisplay = pygame.display.set_mode((Width, Height))
screen = gameDisplay
screen.fill(black)

pygame.display.set_caption("Breakout Project")

pygame.display.update()

 
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
		self.rect.x = x_pos
	

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

class Bricks(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		for i in range(8)
		self.width = 100
		self.height = 20
		self.image = pygame.Surface([self.width,self.height])
		self.image.fill(blue)

		self.rect = self.image.get_rect()
		self.bricks = []
		for i in range(9):

sprites = pygame.sprite.Group()
bricks = Bricks()
sprites.add(bricks)
ball = Ball()
sprites.add(ball)
paddle = Paddle()
sprites.add(paddle)


gameExit = False

while not gameExit:
	Ball()
	Paddle()
	Bricks()
	
	
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_pos -= 10
		if event.key == pygame.K_RIGHT:
			x_pos+= 10


	sprites.update()
	sprites.draw(screen)
	pygame.display.update()		




#required
pygame.quit()
quit()	
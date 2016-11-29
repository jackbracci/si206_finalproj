import pygame


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)


block_width = 20
block_heigh = 10 
paddle_speed = 10 
ball_speed = 5
screen_height = 800
x_position = 0 
y_position = 0 

clock = pygame.time.Clock()

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([block_width, block_height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

  
class Ball(pygame.sprite.Sprite):
    """ This class represents the ball
        It derives from the "Sprite" class in Pygame """
 
    # Speed in pixels per cycle
    speed = 10.0
 
    # Floating point representation of where the ball is
    x = 0.0
    y = 180.0
 
    # Direction of ball (in degrees)
    direction = 200
 
    width = 10
    height = 10
 
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
 
        # Create the image of the ball
        self.image = pygame.Surface([self.width, self.height])
 
        # Color the ball
        self.image.fill(white)
 
        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()
 
        # Get attributes for the height/width of the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls. """
 
    def __init__(self):
        """ Constructor for Player. """
        # Call the parent's constructor 
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((white))
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        self.rect.x = 0
        self.rect.y = self.screenheight-self.height

pygame.init()
GameDisplay = pygame.display.set_mode([800,600])
pygame.display.set_caption("Breakout Final Project")
pygame.display.update()
# font = pygame.font.Font(none, 44)
background = pygame.Surface(screen.get_size())

gameExit = False 
while not gameExit:
	screen.fill(white)
	clock.tick(30)

	for event in pygame.event.get():
		print(event)
pygame.quit()
quit()
    # if game_over:
    # 	text = font.render("Game Over", True, white)
    # 	textpos = text.get_rect(centerx=background.get_width()/2)
    # 	textpos.top = 300
    # 	screen.blit(text, textpos)
	# if event.type == pygame.KEYDOWN:
	# 	x_delta=0;
	# 	y_delta=0;
	# 	if event.key == pygame.K_LEFT:
	# 		x_delta -= 10
	# 	if event.key == pygame.K_RIGHT:
	# 		x_delta += 10
	# 	if event.key == pygame.K_UP:
	# 		y_delta -= 10
	# 	if event.key == pygame.K_DOWN:
	# 		y_delta += 10
	
	# x_pos +=x_delta
	# y_pos +=y_delta
	#screen.fill(blue, rect=[x_pos,y_pos, 20,20])
	# pygame.display.update()		
	# clock.tick(30)

#Sprites 
# blocks
# balls 
# allsprites

# # Create the player paddle object
# player = Player()
# allsprites.add(player)
 
# # Create the ball
# ball = Ball()
# allsprites.add(ball)
# balls.add(ball)

#required
# pygame.quit()
# quit()

# class paddle(pygame.sprite.Sprite):
# 	def __init__(self, x, y):

#pygame template with dubble buffer
import pygame
from settings import * # * => behöver inte skriva t.ex. settings.WIDTH

WIDTH=320
HEIGHT=640
FPS = 30
TITLE="Game"

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0 ,0 )
BLUE = (0,255,0)
GREEN = (0,0,255)


#Create window and setting up pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# gameloop below

running = True
while running:
	#fixing fps
	clock.tick(FPS) #nu körs den alltid på samma tid , om längre=>laggggggg om kortare => vänta

	#process input ( events)
	#controlls etc
	for event in pygame.event.get(): #samla upp alla event vi ej han
		#close window
		if event.type == pygame.QUIT:
			running = False 
	#update
	

	#render

	screen.fill(BLACK)

	pygame.display.flip() # flip display if it is finished


pygame.quit() #syntax=> ej i loop
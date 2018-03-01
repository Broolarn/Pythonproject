#mainfile
import pygame as pg
from settings import * # * => behöver inte skriva t.ex. settings.WIDTH
from sprites import * 
from os import path

class Game:
	def __init__(self): 
		#initialize game window
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		pg.key.set_repeat(500,100) #wait halv  sekund o kolla var tionddels
		self.running = True
		self.load_data()

	def load_data(self):
		game_folder = path.dirname(__file__)
		self.map_data = []
		with open(path.join(game_folder,'map.txt'),'rt') as f:
			for line in f:
				self.map_data.append(line)

	def start(self):
		#restart game
		self.all_sprites =pg.sprite.Group()
		self.walls = pg.sprite.Group()
		#self.player = Player(self,0,0)
		for row , tiles in enumerate(self.map_data):
			for col,tile in enumerate(tiles):
				if tile=='1':
					Wall(self,col,row)
				if tile=='S':
					self.player=Player(self,col,row)
			


	def run(self): 
		#gameloop
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(FPS) / 1000 #nu körs den alltid på samma tid , om längre=>laggggggg om kortare => vänta 
			self.events()
			self.update()
			self.render()


	def update(self):
		#game loop update
		self.all_sprites.update()


	def draw_grid(self):
		for x in range(0,WIDTH,TILESIZE):
			pg.draw.line(self.screen,DIMGRAY,(x,0),(x,HEIGHT))
		
		for y in range(0,HEIGHT,TILESIZE):
			pg.draw.line(self.screen,DIMGRAY,(0,y),(WIDTH,y))


	def events(self):
		for event in pg.event.get(): #samla upp alla event vi ej han
		#close window
			if event.type == pg.QUIT:
				if self.playing:
					self.playing=False
				self.running = False 

			if event.type == pg.KEYDOWN: 
				if event.key == pg.K_ESCAPE:
					self.quit()
				#flytta moment till sprites
				
				# if event.key == pg.K_LEFT:
				# 	self.player.move(dx=-1)

				# if event.key == pg.K_RIGHT:
				# 	self.player.move(dx=1)

				# if event.key == pg.K_UP:
				# 	self.player.move(dy=-1)

				# if event.key == pg.K_DOWN:
				# 	self.player.move(dy=1)

	def render(self):
		#render
		self.screen.fill(BLACK)
		self.draw_grid()
		self.all_sprites.draw(self.screen)
		pg.display.flip() # flip display if it is finished


	def show_start_screen(self):
		#STARTSCREEN
		pass
	def show_gameover_screen(self):
		#gameover
		pass


#definees game object
g = Game()
g.show_start_screen()

while g.running:
	g.start()
	g.run()
	g.show_gameover_screen()

pg.quit()


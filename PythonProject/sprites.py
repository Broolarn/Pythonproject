#sprites
import pygame as pg
from settings import * 


class Player(pg.sprite.Sprite):
	def __init__(self,game,x,y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self,self.groups)
		self.game=game
		self.image=pg.Surface((TILESIZE,TILESIZE))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.vx, self.vy = 0 , 0
		self.x=x * TILESIZE
		self.y=y * TILESIZE


	def get_keys(self):
		self.vx,self.vy = 0 ,0
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT] or keys[pg.K_a] :
			self.vx = -PLAYERSPEED
		if keys[pg.K_RIGHT] or keys[pg.K_d] :
			self.vx = PLAYERSPEED
		if keys[pg.K_UP] or keys[pg.K_w] :
			self.vy = -PLAYERSPEED
		if keys[pg.K_DOWN] or keys[pg.K_s] :
			self.vy = PLAYERSPEED
		#diagonal lite långsammare
		if self.vx != 0 and self.vy !=0:
			self.vx *= 0.71
			self.vy *= 0.71#sqrt2


	def move(self,dx=0,dy=0): # ifall inget sagt 0 som default
		if not self.collide_with_walls(dx,dy):
			self.x+=dx
			self.y+=dy	


	def collide_with_walls(self,dir):
		if dir == 'x':
			hits = pg.sprite.spritecollide(self,self.game.walls ,False) 
			if hits:
				if self.vx > 0:#moved 2 the right
					self.x = hits[0].rect.left -self.rect.width
				if self.vx <0:
					self.x = hits[0].rect.right
				self.vx = 0
				self.rect.x = self.x
		if dir == 'y':
			hits = pg.sprite.spritecollide(self,self.game.walls ,False) 
			if hits:
				if self.vy > 0:#moved 2 the right
					self.y = hits[0].rect.top -self.rect.height
				if self.vy <0:
					self.y = hits[0].rect.bottom
				self.vy = 0
				self.rect.y = self.y



	def update(self):
		# fixar så man går en tile i taget
		self.get_keys()
		self.x += self.vx * self.game.dt
		self.y += self.vy * self.game.dt
		self.rect.x = (self.x)
		self.collide_with_walls('x')
		self.rect.y = self.y
		self.collide_with_walls('y')
		# if pg.sprite.spritecollideany(self, self.game.walls):
		# 	self.x -= self.vx * self.game.dt
		# 	self.y -= self.vy * self.game.dt
		# 	self.rect.topleft = (self.x,self.y)

class Wall(pg.sprite.Sprite):
	def __init__(self,game,x,y):
		self.groups = game.all_sprites,game.walls
		pg.sprite.Sprite.__init__(self,self.groups)
		self.game=game
		self.image=pg.Surface((TILESIZE,TILESIZE))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.x=x
		self.y=y
		self.rect.x = x*TILESIZE
		self.rect.y = y*TILESIZE
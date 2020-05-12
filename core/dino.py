import pygame

class Dino(object):

	def __init__(self, path='resources/images/'):
		self.poses = {'run' :[pygame.image.load(path + 'run1.png'), pygame.image.load(path + 'run2.png')], 'duck' : [pygame.image.load(path + 'duck1.png'), pygame.image.load(path + 'duck2.png')], 'jump' : pygame.image.load(path + 'jump.png')}
		self.legPosition = False
		self.time = 0
		self.position = 0
		self.acceleration = 2
		self.velocity = 0
		self.jumpActive = False
		self.duckActive = False

	def jump(self):
		if not self.jumpActive and not self.duckActive:
			self.velocity = 30
			self.jumpActive = True

	def setDuck(self, duck : bool):
		self.duckActive = duck

	def update(self):
		if self.jumpActive:
			self.velocity -= self.acceleration
			self.position += self.velocity
			if self.position < 0:
				self.position = 0
				self.jumpActive = False

		if pygame.time.get_ticks() - self.time >= 100:
			self.time = pygame.time.get_ticks()
			self.legPosition = not self.legPosition

	def show(self, screen : pygame.Surface):
		if self.jumpActive:
			screen.blit(self.poses['jump'], (20, 250 - self.position))
		else:
			key = 'duck' if self.duckActive else 'run'
			screen.blit(self.poses[key][self.legPosition], (0 if self.duckActive else 20, 250 - self.position))

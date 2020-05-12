import pygame
from .dino import Dino
from .bird import Bird
from .cloud import Cloud
from .cactus import Cactus

class Universe(object):

	def __init__(self, velocity=10):
		self.groundPosition = 320
		self.velocity = velocity
		self.dino = Dino()
		self.birds = []
		self.cacti = []
		self.clouds = []

	def addItem(self, item : str):
		if item == 'cactus':
			self.cacti.append(Cactus())

	def setVelocity(self, velocity):
		self.velocity = velocity

	def update(self):
		for cloud in self.clouds:
			cloud.update(0.6 * self.velocity)
			if not cloud.isAlive():
				self.clouds.remove(cloud)
		for cactus in self.cacti:
			cactus.update(self.velocity)
			if not cactus.isAlive():
				self.cacti.remove(cactus)
		for bird in self.birds:
			bird.update(self.velocity)
			if not bird.isAlive():
				self.birds.remove(bird)
		self.dino.update()

	def show(self, screen : pygame.Surface):
		pygame.draw.line(screen, (51, 51, 51), (0, self.groundPosition), (1000, self.groundPosition), 2)
		for cloud in self.clouds:
			cloud.show(screen)
		for cactus in self.cacti:
			cactus.show(screen)
		for bird in self.birds:
			bird.show(screen)
		self.dino.show(screen)

	def dinoJump(self):
		self.dino.jump()

	def dinoSetDuck(self, value : bool):
		self.dino.setDuck(value)

import pygame
import random
from .dino import Dino
from .bird import Bird
from .cloud import Cloud
from .cactus import Cactus

class Universe(object):

	def __init__(self, velocity=15):
		self.font = pygame.font.Font('resources/fonts/P2P.ttf', 20)
		self.groundPosition = 320
		self.velocity = velocity
		self.score = 0
		self.dino = Dino()
		self.birds = []
		self.birdTime = 0.
		self.newBirdLimit = 0.5
		self.cacti = []
		self.cactusTime = 0.
		self.newCactusLimit = 500
		self.clouds = []
		self.addItem('cloud')

	def addItem(self, item : str):
		if item == 'cluster':
			if (random.random() < 0.8):
				self.cacti.append(Cactus(type=random.randint(1, 3)))
				self.cacti.append(Cactus(type=random.randint(1, 3), offset=60))
				self.cacti.append(Cactus(type=random.randint(1, 3), offset=120))
			else:
				self.cacti.append(Cactus(size=True, type=random.randint(1, 3)))
				self.cacti.append(Cactus(size=True, type=random.randint(1, 3), offset=30))
				self.cacti.append(Cactus(size=True, type=random.randint(1, 3), offset=60))

		if item == 'cloud':
			self.clouds.append(Cloud([1000 + random.random() * 200, 20 + random.random() * 100]))

		if item == 'bird':
			self.birds.append(Bird(220))

	def setVelocity(self, velocity):
		self.velocity = velocity

	def update(self):
		for cloud in self.clouds:
			cloud.update(0.5 * self.velocity)
			if not cloud.isAlive():
				self.clouds.remove(cloud)
				self.addItem('cloud')
		for cactus in self.cacti:
			cactus.update(self.velocity)
			if not cactus.isAlive():
				self.cacti.remove(cactus)
		for bird in self.birds:
			bird.update(1.2 * self.velocity)
			if not bird.isAlive():
				self.birds.remove(bird)
		self.dino.update()
		self.score += 0.15
		self.birdTime += 1e-3
		self.cactusTime += 1e-3
		if (random.random() < (self.birdTime / self.newBirdLimit)**2):
			self.addItem('bird')
			self.birdTime = 0
		if (random.random() < (self.cactusTime / self.newCactusLimit)**2):
			self.addItem('cluster')
			self.cactusTime = 0


	def show(self, screen : pygame.Surface):
		pygame.draw.line(screen, (51, 51, 51), (0, self.groundPosition), (1000, self.groundPosition), 2)
		pygame
		for cloud in self.clouds:
			cloud.show(screen)
		for cactus in self.cacti:
			cactus.show(screen)
		for bird in self.birds:
			bird.show(screen)
		self.dino.show(screen)
		screen.blit(self.font.render(str(int(self.score)).zfill(5), False, (51, 51, 51)), (880, 20))

	def dinoJump(self):
		self.dino.jump()

	def dinoSetDuck(self, value : bool):
		self.dino.setDuck(value)

import pygame
import random
from .dino import Dino
from .bird import Bird
from .cloud import Cloud
from .cactus import Cactus
from playsound import playsound

class Universe(object):

	def __init__(self, velocity=15.):
		self.font = pygame.font.Font('resources/fonts/P2P.ttf', 20)
		self.groundPosition = 320
		self.velocity = velocity
		self.score = 1
		self.reload = pygame.image.load('resources/images/reload.png')
		self.dino = Dino()
		self.birds = []
		self.birdTime = 0.
		self.newBirdLimit = 5
		self.cacti = []
		self.cactusTime = 0.
		self.newCactusLimit = 0.5
		self.clouds = []
		self.isAlive = True
		self.addItem('cloud')

	def addItem(self, item : str):
		if item == 'cactus':
			self.cacti.append(Cactus(size=(random.random() < 0.5), type=random.randint(1, 3)))

		if item == 'cluster':
			if (random.random() < 0.7):
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

	def update(self):
		points = self.dino.update()
		for cloud in self.clouds:
			cloud.update(0.5 * self.velocity)
			if not cloud.isAlive():
				self.clouds.remove(cloud)
				self.addItem('cloud')
		for cactus in self.cacti:
			cactus.update(self.velocity)
			for point in points:
				self.isAlive = self.isAlive and not cactus.colliding(point)
			if not cactus.isAlive():
				self.cacti.remove(cactus)
		for bird in self.birds:
			bird.update(1.2 * self.velocity)
			for point in points:
				self.isAlive = self.isAlive and not bird.colliding(point)
			if not bird.isAlive():
				self.birds.remove(bird)
		self.score += 0.15
		if (self.score / 100.) - int(self.score / 100.) <= 0.0015:
			playsound('resources/sounds/point.wav', False)
			self.velocity += 1.25
			factor = (self.velocity - 1.25) / self.velocity
			self.cactusTime *= factor
			self.birdTime *= factor

		self.birdTime += 1e-3
		self.cactusTime += 1e-3
		if (random.random() < (self.birdTime / self.newBirdLimit)**2):
			self.addItem('bird')
			self.birdTime = 0
		if (random.random() < (self.cactusTime / self.newCactusLimit)**2):
			if (random.random() < 0.8):
				self.addItem('cluster')
			else:
				self.addItem('cactus')
			self.cactusTime = 0
		if not self.isAlive:
			playsound('resources/sounds/over.wav', False)


	def show(self, screen : pygame.Surface):
		pygame.draw.line(screen, (51, 51, 51), (0, self.groundPosition), (1000, self.groundPosition), 2)
		pygame
		for cloud in self.clouds:
			cloud.show(screen)
		for cactus in self.cacti:
			cactus.show(screen)
		for bird in self.birds:
			bird.show(screen)
		self.dino.show(screen, self.isAlive)
		screen.blit(self.font.render(str(int(self.score)).zfill(5), False, (51, 51, 51)), (880, 20))
		if not self.isAlive:
			screen.blit(self.font.render('G A M E  O V E R', False, (51, 51, 51)), (350, 100))
			screen.blit(self.reload, (490, 150))
		return self.isAlive

	def dinoJump(self):
		self.dino.jump()

	def dinoSetDuck(self, value : bool):
		self.dino.setDuck(value)

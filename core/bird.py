import pygame

class Bird(object):

	def __init__(self, position, path='resources/images/'):
		self.position = [1000, position]
		self.time = 0
		self.wingPosition = False
		self.poses = [pygame.image.load(path + 'bird1.png'), pygame.image.load(path + 'bird2.png')]

	def update(self, velocity):
		if pygame.time.get_ticks() - self.time >= 200:
			self.time = pygame.time.get_ticks()
			self.wingPosition = not self.wingPosition

		self.position[0] -= velocity

	def show(self, screen : pygame.Surface):
			screen.blit(self.poses[self.wingPosition], tuple(self.position))

	def isAlive(self):
		return self.position[0] > -60

import pygame

class Cactus(object):

	def __init__(self, size=False, type=1, path='resources/images/'):
		self.pose = pygame.image.load(path + 'cactus' + str(type) + '.png')
		self.size = size
		if size:
			self.pose = pygame.transform.scale(self.pose, (10, 20))
		self.position = [1000, 230]

	def update(self, velocity):
		self.position[0] -= velocity

	def show(self, screen : pygame.Surface):
		screen.blit(self.pose, tuple(self.position))

	def isAlive(self):
		return self.position[0] > -60

	def colliding(self, point):
		if point[0] > self.position[0] + 5:
			return False
		if point[0] < self.position[0] - 5:
			return False
		if point[1] < self.position[1]:
			return False
		return True

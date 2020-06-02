import pygame

class Cactus(object):

	def __init__(self, size=False, type=1, offset=0, path='resources/images/'):
		self.pose = pygame.image.load(path + 'cactus' + str(type) + '.png')
		self.size = size
		self.position = [1000 + offset, 230]
		if size:
			self.position[1] += 48
			self.pose = pygame.transform.scale(self.pose, (60, 72))

	def update(self, velocity):
		self.position[0] -= velocity

	def show(self, screen : pygame.Surface):
		screen.blit(self.pose, tuple(self.position))

	def isAlive(self):
		return self.position[0] > -100

	def colliding(self, point):
		if point[0] > self.position[0] + 5:
			return False
		if point[0] < self.position[0] - 5:
			return False
		if point[1] < self.position[1]:
			return False
		return True

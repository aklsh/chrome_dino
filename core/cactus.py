import pygame

class Cactus(object):

	def __init__(self, size=False, type=1, offset=0, path='resources/images/'):
		self.pose = pygame.image.load(path + 'cactus' + str(type) + '.png')
		self.size = size
		self.position = [1000 + offset, 230]
		self.bbox = [15, 5, 70, 100]
		if size:
			self.position[1] += 48
			self.pose = pygame.transform.scale(self.pose, (60, 72))
			self.bbox = [10, 10, 40, 70]

	def update(self, velocity):
		self.position[0] -= velocity

	def show(self, screen : pygame.Surface):
		screen.blit(self.pose, tuple(self.position))
		pygame.draw.rect(screen, (0, 255, 0), (self.position[0] + self.bbox[0], self.position[1] + self.bbox[1], self.bbox[2], self.bbox[3]), 2)

	def isAlive(self):
		return self.position[0] > -100

	def colliding(self, point):
		if point[0] > self.position[0] + self.bbox[0] + self.bbox[2]:
			return False
		if point[0] < self.position[0] + self.bbox[0]:
			return False
		if point[1] < self.position[1] + self.bbox[1]:
			return False
		if point[1] > self.position[1] + self.bbox[1] + self.bbox[3]:
			return False
		return True

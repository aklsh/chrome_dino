import pygame

class Bird(object):

	def __init__(self, position, path='resources/images/'):
		self.position = [1000, position]
		self.time = 0
		self.wingPosition = False
		self.poses = [pygame.image.load(path + 'bird1.png'), pygame.image.load(path + 'bird2.png')]
		self.bbox = [0, 10, 80, 50]

	def update(self, velocity):
		if pygame.time.get_ticks() - self.time >= 200:
			self.time = pygame.time.get_ticks()
			self.wingPosition = not self.wingPosition

		self.position[0] -= velocity

	def show(self, screen : pygame.Surface, showBBox=False):
		screen.blit(self.poses[self.wingPosition], tuple(self.position))
		if showBBox:
			pygame.draw.rect(screen, (0, 255, 0), (self.position[0] + self.bbox[0], self.position[1] + self.bbox[1], self.bbox[2], self.bbox[3]), 2)

	def isAlive(self):
		return self.position[0] > -60

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

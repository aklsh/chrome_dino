import pygame

class Cloud(object):

	def __init__(self, position, path='resources/images/'):
		pose = pygame.image.load(path + 'cloud.png')
		self.position = [1000, position]

	def update(self, velocity):
		self.position[0] -= velocity

	def show(self, screen : pygame.Surface):
		screen.blit(self.pose, tuple(self.position))

	def isAlive(self):
		return self.position[0] < -60
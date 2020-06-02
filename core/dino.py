import pygame

class Dino(object):

	def __init__(self, path='resources/images/'):
		self.poses = {'run' :[pygame.image.load(path + 'run1.png'), pygame.image.load(path + 'run2.png')], 'duck' : [pygame.image.load(path + 'duck1.png'), pygame.image.load(path + 'duck2.png')], 'jump' : pygame.image.load(path + 'jump.png')}
		self.deadPose = pygame.image.load(path + 'dead.png')
		self.legPosition = False
		self.time = 0
		self.position = 0
		self.acceleration = 2
		self.velocity = 0
		self.jumpActive = False
		self.duckActive = False
		self.bodyPoints = [[115, 260], [100, 300]]
		self.bodyPointsDuck = [[125, 320], [125, 290]]
		self.bodyPointsJump = [[115, 260], [100, 300], [25, 305]]

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

		points = self.bodyPoints
		if self.duckActive:
			points = self.bodyPointsDuck
		if self.jumpActive:
			points = [[115, 260], [100, 300], [25, 305]]
			for point in points:
				point[1] -= self.position

		return points

	def show(self, screen: pygame.Surface, isAlive: bool, showBodyPoints=False):
		if isAlive:
			if self.jumpActive:
				screen.blit(self.poses['jump'], (20, 250 - self.position))
			else:
				key = 'duck' if self.duckActive else 'run'
				screen.blit(self.poses[key][self.legPosition], (0 if self.duckActive else 20, 250))
		else:
			screen.blit(self.deadPose, (20, 250 - self.position))

		if showBodyPoints:
			if self.duckActive:
				for point in self.bodyPointsDuck:
					pygame.draw.circle(screen, (0, 0, 255), point, 4)
			elif self.jumpActive:
				for point in self.bodyPointsJump:
					pygame.draw.circle(screen, (0, 0, 255), (point[0], point[1] - self.position), 4)
			else:
				for point in self.bodyPoints:
					pygame.draw.circle(screen, (0, 0, 255), point, 4)
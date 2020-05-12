import pygame
import sys
from core.universe import Universe

pygame.init()
window_name = '.'.join(sys.argv[0].split('.')[:-1])
pygame.display.set_caption(window_name if window_name != '' else 'pygame')
SCREEN = pygame.display.set_mode((1000, 400))
done = False
clock = pygame.time.Clock()
FRAME_RATE = 60

#-----------------------------------------------------------------------

universe = Universe()

def setup():
	pass

def draw():
	SCREEN.fill((245, 245, 245))
	universe.update()
	universe.show(SCREEN)

#-----------------------------------------------------------------------

setup()
while not done:
	draw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				universe.dinoJump()
			if event.key == pygame.K_DOWN:
				universe.dinoSetDuck(True)
			if event.key == pygame.K_SPACE:
				universe.addItem('cactus')
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				universe.dinoSetDuck(False)
	pygame.display.flip()
	clock.tick(FRAME_RATE)
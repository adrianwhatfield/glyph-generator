import random
import pygame

class Glyph:
	horizontal = [] # Top -> Middle -> Bottom
	vertical = [] # Left -> Middle -> Right

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    
    pygame.draw.line(screen, pygame.Color(75, 80, 45), pygame.Vector2(10, 10), pygame.Vector2(20, 30))
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


def generate_glyph(complexity): # Generate the glyph line values, with complexity amount
	new_glyph = Glyph()
	
	i = 0
	while i < 3:
		i += 1
		if random.random() > float(complexity):
			new_glyph.horizontal.append(True)
		else:
			new_glyph.horizontal.append(False)
	
	j = 0
	while j < 3:
		j += 1
		if random.random() > float(complexity):
			new_glyph.vertical.append(True)
		else:
			new_glyph.vertical.append(False)
	
	return new_glyph

value = input("Enter complexity (0.1 to 0.9): ")
new = generate_glyph(value)

print(new.horizontal + new.vertical)

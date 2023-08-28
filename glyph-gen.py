import random
import pygame

class Glyph:
	horizontal = [] # Top -> Middle -> Bottom
	vertical = [] # Left -> Middle -> Right

# HORIZONTAL LINES -----------

top_start = pygame.Vector2(10, 10)
top_end = pygame.Vector2(110, 10)

middle_h_start = pygame.Vector2(10, 60)
middle_h_end = pygame.Vector2(110, 60)

bottom_start = pygame.Vector2(10, 110)
bottom_end = pygame.Vector2(110, 110)

# VERTICAL LINES -------------

left_start = pygame.Vector2(10, 10)
left_end = pygame.Vector2(10, 110)

middle_v_start = pygame.Vector2(60, 10)
middle_v_end = pygame.Vector2(60, 110)

right_start = pygame.Vector2(110, 10)
right_end = pygame.Vector2(110, 110)

# ----------------------------

button_rect = pygame.Rect(10, 120, 100, 40)
black = pygame.Color("black")

# pygame setup
pygame.init()
screen = pygame.display.set_mode((120, 170))
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

    # RENDER YOUR GAME HERE ---------------
    
    pygame.draw.line(screen, black, top_start, top_end)
    pygame.draw.line(screen, black, middle_h_start, middle_h_end)
    pygame.draw.line(screen, black, bottom_start, bottom_end)
    
    pygame.draw.line(screen, black, left_start, left_end)
    pygame.draw.line(screen, black, middle_v_start, middle_v_end)
    pygame.draw.line(screen, black, right_start, right_end)
    
    pygame.draw.rect(screen, black, button_rect, border_radius=5)
    
    # RENDER YOUR GAME HERE ----------------

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


def generate_glyph_lines(complexity): # Generate the glyph line values, with complexity amount
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

# value = input("Enter complexity (0.1 to 0.9): ")
# new = generate_glyph(value)


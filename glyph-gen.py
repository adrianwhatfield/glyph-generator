import random
import pygame
import pygame_widgets

from pygame_widgets.button import Button

class Glyph:
	horizontal = [] # Top -> Middle -> Bottom
	vertical = [] # Left -> Middle -> Right

# HORIZONTAL LINES -----------

top_start = pygame.Vector2(20, 20)
top_end = pygame.Vector2(100, 20)

middle_h_start = pygame.Vector2(20, 60)
middle_h_end = pygame.Vector2(100, 60)

bottom_start = pygame.Vector2(20, 100)
bottom_end = pygame.Vector2(100, 100)

# VERTICAL LINES -------------

left_start = pygame.Vector2(20, 20)
left_end = pygame.Vector2(20, 100)

middle_v_start = pygame.Vector2(60, 20)
middle_v_end = pygame.Vector2(60, 100)

right_start = pygame.Vector2(100, 20)
right_end = pygame.Vector2(100, 100)

# ----------------------------

is_generated = False

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((120, 170))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Glyph Generator")

button = Button(screen, 10, 120, 100, 40, text="New", radius=5, onClick=lambda: render_glyph(generate_glyph_lines(0.4)))

black = pygame.Color("black")

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

def render_glyph(glyph_list):
	this_glyph = glyph_list
	
	for index, line in enumerate(this_glyph.horizontal):
		if line == True:
			match index:
				case 0:
					pygame.draw.line(screen, black, top_start, top_end, width=2)
				case 1:
					pygame.draw.line(screen, black, middle_h_start, middle_h_end, width=2)
				case 2:
					pygame.draw.line(screen, black, bottom_start, bottom_end, width=2)
		else:
			continue
	
	for index, line in enumerate(this_glyph.vertical):
		if line == True:
			match index:
				case 0:
					pygame.draw.line(screen, black, left_start, left_end, width=2)
				case 1:
					pygame.draw.line(screen, black, middle_v_start, middle_v_end, width=2)
				case 2:
					pygame.draw.line(screen, black, right_start, right_end, width=2)
		else:
			continue

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


	# fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

	# RENDER YOUR GAME HERE ---------------
	
    render_glyph(generate_glyph_lines(0.4))
    
    pygame_widgets.update(event)
    pygame.display.update()
    
	# RENDER YOUR GAME HERE ----------------

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


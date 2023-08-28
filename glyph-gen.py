import random

class Glyph:
	horizontal = [] # Top -> Middle -> Bottom
	vertical = [] # Left -> Middle -> Right

def generate_glyph(complexity): # Generate the glyph line values, with complexity amount
	new_glyph = Glyph()
	
	i = 0
	while i < 3:
		i += 1
		if random.random() > complexity:
			new_glyph.horizontal.append(True)
		else:
			new_glyph.horizontal.append(False)
	
	j = 0
	while j < 3:
		j += 1
		if random.random() > complexity:
			new_glyph.vertical.append(True)
		else:
			new_glyph.vertical.append(False)
	
	return new_glyph

value = input("Enter complexity (0.1 to 0.9): ")
new = generate_glyph(value)

print(new.horizontal + new.vertical)

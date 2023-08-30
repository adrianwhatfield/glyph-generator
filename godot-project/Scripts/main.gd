extends Node

@onready var glyph_image = $HBoxContainer/Result/GlyphImage
@onready var complexity_num = $HBoxContainer/Options/Complexity/ComplexityNum


var current_glyph = generate_lines(0.4)

# Horizontal Lines
var top_start = Vector2(100, 100)
var top_end = Vector2(400, 100)

var middle_h_start = Vector2(100, 250)
var middle_h_end = Vector2(400, 250)

var bottom_start = Vector2(100, 400)
var bottom_end = Vector2(400, 400)

# Vertical Lines
var left_start = Vector2(100, 100)
var left_end = Vector2(100, 400)

var middle_v_start = Vector2(250, 100)
var middle_v_end = Vector2(250, 400)

var right_start = Vector2(400, 100)
var right_end = Vector2(400, 400)

func _ready():
	randomize()

func generate_lines(complexity) -> Glyph:
	var glyph = Glyph.new()
	
	for i in 3:
		if randf() < complexity:
			glyph.horizontal.append(true)
		else:
			glyph.horizontal.append(false)
	
	for j in 3:
		if randf() < complexity:
			glyph.vertical.append(true)
		else:
			glyph.vertical.append(false)
	
	return glyph

func draw_lines(glyph):
	var i = 0
	for line in glyph.horizontal:
		if i >= 3:
			break
		if line == true:
			match i:
				0: 
					glyph_image.draw_line(top_start, top_end, Color.WHITE, 1, true)
				1: 
					glyph_image.draw_line(middle_h_start, middle_h_end, Color.WHITE, 1, true)
				2: 
					glyph_image.draw_line(bottom_start, bottom_end, Color.WHITE, 1, true)
		else:
			continue
		i += 1
	
	var j = 0
	for line in glyph.vertical:
		if j >= 3:
			break
		if line == true:
			match j:
				0: 
					glyph_image.draw_line(left_start, left_end, Color.WHITE, 1, true)
				1: 
					glyph_image.draw_line(middle_v_start, middle_v_end, Color.WHITE, 1, true)
				2: 
					glyph_image.draw_line(right_start, right_end, Color.WHITE, 1, true)
		else:
			continue
		j += 1


func _on_glyph_image_draw():
	draw_lines(current_glyph)


func _on_new_glyph_pressed():
	var complexity = complexity_num.value
	current_glyph = generate_lines(complexity)
	glyph_image.queue_redraw()

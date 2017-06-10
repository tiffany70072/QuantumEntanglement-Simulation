from __future__ import division
from visual import*

scene = display(center = (0, 0, 10), width = 750, height = 400, y = 100, 
	range = 22, background = (0.93, 0.93, 0.83), forward = (0, -1, -5))

# define position
pos1_cen = vector(0, 0, 0)
dist = 18
start_pos = 2
pos1 = [pos1_cen + vector(-dist, 0, 0), pos1_cen + vector(dist, 0, 0)]

# define size
box_len = 6
box_hei = 5
box_wid = 3
theta = [-30/180*3.14, 0, 30/180*3.14]

# velocity
v = 0.4
p_v = [vector(-v, 0, 0), vector(v, 0, 0)]

# define color
dark_color = [(0.05, 0.3, 0.2), (0.5, 0.05, 0.05)] # green and red
light_color = [(0.05, 0.7, 0.4), (1, 0.1, 0.1)]
box_color = (0.6, 0.8, 0.85) #(0.5, 0.5, 0.5)
arrow_dark_color = (0.3, 0.3, 0.3)
arrow_light_color = (0.85, 0.7, 0)
particle_color = (0.4, 0.4, 0.5)

# object container
source = []
launcher = []
detector = []
switch = []
switch_id_text = [] # 1, 2, 3
switch_text = []
light = []
light_text = []
p = [] # particle

for i in range(2):
	p.append(sphere(pos = pos1_cen, radius = 0.6, color = particle_color))

content = label(pos = pos1_cen + vector(0, -12, 0), height = 15,
	box = False, line = False, color = (0.1, 0.2, 0.4), font = 'monospace', opacity = 0)

def source_detector(p):
	source.append(box(pos = pos1_cen, length = box_hei, height = box_hei, width = box_wid, color = box_color))
	launcher.append(cylinder(pos = pos1_cen + vector(-4, 0, 0), axis = (8, 0, 0), color = box_color))

	# label
	label(pos = pos1_cen + vector(0, -box_hei/2.0 - 3, 0), text = "Source", height = 15,
		box = False, line = False, color = (0.1, 0.1, 0.1), font = 'monospace', opacity = 0)
	label(pos = pos1[0] + vector(0, -box_hei/2.0-3, 0), text = 'Detector A', height = 15,
		box = False, line = False, color = (0.1, 0.1, 0.1), font = 'monospace', opacity = 0)
	label(pos = pos1[1] + vector(0, -box_hei/2.0-3, 0), text = 'Detector B', height = 15,
		box = False, line = False, color = (0.1, 0.1, 0.1), font = 'monospace', opacity = 0)

	for i in range(2):
		detector.append(box(pos = pos1[i], length = box_len, height = box_hei, width = box_wid, color = box_color))
		cylinder(pos = pos1[i], axis = (4-8*i, 0, 0), color = box_color)

	content.text = "There are 3 devices in Mermin's device:\n1 source and 2 detectors, A and B."	

	sleep(6)
	content.text = "Each time, the source sends a pair of particles to A and B."
	for j in range(3):
		for i in range(2):
			p[i].pos = pos1_cen + vector(-start_pos + 2*start_pos*i, 0, 0)
		detect_time = int((dist - start_pos)/v)
		for time in range(detect_time):
			rate(20)
			for i in range(2): p[i].pos += p_v[i]

def switch_light():
	for i in range(2):
		switch.append([])
		switch_id_text.append([])
		for j in range(3):
			switch[i].append(arrow(pos = pos1[i] + vector(-0.5+0.5*j, -2, box_wid/2.0), 
				axis = 3*vector(sin(theta[j]), cos(theta[j]), 0), 
				shaftwidth = 0.25, color = arrow_dark_color))
			switch_id_text[i].append(label(pos = pos1[i] + vector(-1.9+1.9*j, 1.6, box_wid/2.0), text = str(j+1),
				box = False, line = False, color = (0.1, 0.1, 0.1), font = 'monospace', background = box_color, opacity = 0))

		light.append([])
		for j in range(2):
			light[i].append(sphere(pos = pos1[i] + vector(-1.5 + 3*j, box_hei/2.0 + 0.5, 0), radius = 1, color = dark_color[j]))

	for i in range(2):
		switch_text.append(label(pos = pos1[i] + vector(1-2*i, box_hei/2.0 + 5.5, 0), visible = False, height = 15, 
			box = False, line = False, color = (0.1, 0.1, 0.1), font = 'monospace', opacity = 0))
		light_text.append(label(pos = pos1[i] + vector(1-2*i, box_hei/2.0 + 3.5, 0), visible = False, height = 15, 
			box = False, line = False, color = (0.1, 0.1, 0.1), font = 'monospace', opacity = 0))
	content.text = "There are 3 switches (1, 2, 3) and\n2 lights (red, green) on both detectors."

def introduce():
	content.text = "Each switch points to a number randomly and uniformly.\n\
	P(switch = 1) = P(2) = P(3) = 1/3"
	for j in range(3):
		for i in range(2):
			switch[i][(j+2*i)%3].color = arrow_light_color
			#switch_text_visible(switch_id)
			l_text = "Switch = " + str((j+2*i)%3+1)
			switch_text[i].text = l_text
			switch_text[i].visible = True
		sleep(3)
		for i in range(2):
			switch[i][(j+2*i)%3].color = arrow_dark_color
			switch_text[i].visible = False

def light_text_visible(colors):
	for i in range(2):
		if colors[i] == 0: l_text = "Green light fires"
		elif colors[i] == 1: l_text = "Red light fires"
		else: l_text = "No light"
		light_text[i].text = l_text
		light_text[i].color = light_color[colors[i]]
		light_text[i].visible = True

def switch_text_visible(switch_id):
	for i in range(2):
		l_text = "Switch = " + str(switch_id[i]+1)
		switch_text[i].text = l_text
		switch_text[i].visible = True

# animation start
def detect_light_id(left, right):
	if left == "G": x = 0
	elif left == "R": x = 1
	else: print "Error: wrong color"
	if right == "G": y = 0
	elif right == "R": y = 1
	else: print "Error: wrong color"
	return [x, y]

def launch(p, light_id, switch_id, t):
	colors = detect_light_id(light_id[0], light_id[1])
	
	# particle launching
	for i in range(2):
		p[i].pos = pos1_cen + vector(-start_pos + 2*start_pos*i, 0, 0)
		switch[i][switch_id[i]].color = arrow_light_color
		switch_text_visible(switch_id)
	sleep(1)
	
	detect_time = int((dist - start_pos)/v)
	for time in range(detect_time):
		rate(20)
		for i in range(2): p[i].pos += p_v[i]
		
	# detectors accept particles
	for i in range(2): light[i][colors[i]].color = light_color[colors[i]]

	light_text_visible(colors)
	sleep(t)

	# reset
	for i in range(2):
		switch[i][switch_id[i]].color = arrow_dark_color
		light[i][colors[i]].color = dark_color[colors[i]]
		light_text[i].visible = False
		switch_text[i].visible = False

	sleep(1)

source_detector(p)
sleep(1)
switch_light()
sleep(5)
introduce()
sleep(0.5)

content.text = "In each round, each switch points randomly to a position.\n\
-> The source launches.\n-> A light fires."
#launch(p, light_id = ["G", "R"], switch_id = [2, 1], t = 4)
launch(p, light_id = ["G", "R"], switch_id = [2, 1], t = 4)
content.text = "If two switches point to the same number, \n\
the lights' colors must be opposite: 'RG' or 'GR'."
launch(p, light_id = ["R", "G"], switch_id = [0, 0], t = 5)
content.text = "If two switches point to different numbers, \nthe lights' colors follow certain instruction sets \n\
that will be introduced later."
launch(p, light_id = ["R", "R"], switch_id = [0, 1], t = 7)

scene.delete()
print "\n-------- End! ---------"
exit()




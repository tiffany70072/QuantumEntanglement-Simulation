from __future__ import division
from visual import*
import random

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
	box = False, line = False, color = (0.1, 0.1, 0.1), font = 'monospace', opacity = 0)

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

def introduce():
	label(pos = pos1_cen + vector(0, box_hei/2.0 + 5.5, 0), height = 15,
		text = "The case of {RNG-GGR}", 
		box = False, line = False, color = (0.1, 0.1, 0.1), font = 'monospace', opacity = 0)
	label(pos = pos1[0] + vector(0, -7, 0), text = 'Set = {RNG}', height = 15,
		box = False, line = False, color = (0.1, 0.25, 0.5), font = 'monospace', opacity = 0)
	label(pos = pos1[1] + vector(0, -7, 0), text = 'Set = {GGR}', height = 15,
		box = False, line = False, color = (0.1, 0.25, 0.5), font = 'monospace', opacity = 0)

def light_text_visible(colors):
	for i in range(2):
		if colors[i] == 0: l_text = "Green light fires"
		elif colors[i] == 1: l_text = "Red light fires"
		else: l_text = "No light"
		if colors[i] != 2:
			light_text[i].text = l_text
			light_text[i].color = light_color[colors[i]]
			light_text[i].visible = True
		else:
			light_text[i].text = l_text
			light_text[i].color = (0.1, 0.1, 0.1)
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
	else: x = 2 
	if right == "G": y = 0
	elif right == "R": y = 1
	else: y = 2 
	return [x, y]

def launch(p, light_id, switch_id, t):
	colors = detect_light_id(light_id[0], light_id[1])
	
	# particle launching
	for i in range(2):
		p[i].pos = pos1_cen + vector(-start_pos + 2*start_pos*i, 0, 0)
		switch[i][switch_id[i]].color = arrow_light_color
		switch_text_visible(switch_id)
	sleep(7)
	
	detect_time = int((dist - start_pos)/v)
	for time in range(detect_time):
		rate(20)
		for i in range(2): p[i].pos += p_v[i]
		
	# detectors accept particles
	for i in range(2):
		if colors[i] != 2: light[i][colors[i]].color = light_color[colors[i]]

	light_text_visible(colors)
	sleep(t)

	# reset
	for i in range(2):
		switch[i][switch_id[i]].color = arrow_dark_color
		if colors[i] != 2: light[i][colors[i]].color = dark_color[colors[i]]
		light_text[i].visible = False
		switch_text[i].visible = False
	sleep(1)

source_detector(p)
switch_light()
#sleep(10)
introduce()
sleep(4)

content.text = "If switch A points to 1 under {'R'NG}, R will fire.\n\
If switch C points to 3 under {GG'R'}, R will fire.\n\
In this case, colors are same."
launch(p, light_id = ["R", "R"], switch_id = [0, 2], t = 4)
#content.text = "If switch A = 3, RN'G' -> G fires\nAnd switch B = 3, GG'R' -> R fires\n\
#-> opposite colors"
#launch(p, light_id = ["G", "R"], switch_id = [2, 2], t = 4)
content.text = "If switch A points to 2 under {R'N'G}, no light will fire.\n\
If switch C points to 3 under {GG'R'}, R will fire.\n\
This case is not considered."

launch(p, light_id = ["N", "R"], switch_id = [1, 2], t = 2)

print "\n-------- End! ---------"

seq1 = [0, 0, 1]  #R:0, G:1
seq2 = [0, 2, 1]  #N:2
same, diff, null = 0, 0, 0
prob = 0
content.height = 17
content.pos = (0, -14, 0)
scene.center = (0, -5, 10)
content.color = (0.7, 0.1, 0.1)

for time in range(0, 1001000):
	sw = random.sample(range(3), 2)

	sw1 = sw[0] # A machine switch
	sw2 = sw[1] # B machine switch

	if seq2[sw2] == 2:
		null += 1
		continue

	elif seq1[sw1] == seq2[sw2]: same += 1
	else: diff += 1

	if time-null != 0: prob = float(same)/(time-null)
	if time <= 10:
		content.text = "After " + str(time) + " times, \nProbability of different colors = " + "{:2.5f}".format(prob)\
		 + "\nTrue Prob is 1/4."
		sleep(0.7)
	elif time <= 100 and time % 5 == 0:
		content.text = "After " + str(time) + " times, \nProbability of different colors = " + "{:2.5f}".format(prob)\
		+ "\nTrue Prob is 1/4."
		sleep(0.3)
	elif time <= 10000 and time % 200 == 0:
		content.text = "After " + str(time) + " times, \nProbability of different colors = " + "{:2.5f}".format(prob)\
		+ "\nTrue Prob is 1/4."
		sleep(0.1)
	elif time % 20000 == 0:
		content.text = "After " + str(time) + " times, \nProbability of different colors = " + "{:2.5f}".format(prob)\
		+ "\nTrue Prob is 1/4."
		sleep(0.08)

sleep(10)





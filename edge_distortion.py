time_in_game = 0
game_state = True 
objects = [] 
height = 0 #высота игрового поля
width = 0 #ширина игрового поля
world = [[""]]
skin_of_world = '░'
frame = ['│','─','┌','┐','└','┘']	

class Entity ():

	def init (self, x, y, t, skin):
		self.xy = [x,y]
		self.t = t
		self.number = 0
		self.skin = skin
		upbating_obj ()

def init (w, h):
	""""""
	global height
	height = h
	global width
	width = w

#matrix
def creating_world():
	global world
	world[0][0] = skin_of_world
	world[0] = world[0] * width
	world = world * height

def clear ():
	global world
	world = [['']]
	creating_world ()

def print_objects ():
	global objects
	clear ()
	for i in range(len(objects)):
		xy = objects[i].xy
		point (xy, objects[i].skin)

def print_world ():
	print (frame[2] + frame[1] * width + frame[3])
	for i in range (len(world)):
		tmp = ''
		for j in world[i]:
			tmp = tmp + str(j)
		print (frame[0] + tmp + frame[0])
	print (frame[4] + frame[1] * width + frame[5])

#essence
def new_object (obj):
	global objects
	objects.append (obj)

def new_xy (xy, n):
	global objects
	objects[n-1].xy[0] = xy[0]
	objects[n-1].xy[1] = xy[1]

def kill_all ():
	global objects
	objects = []

def kill_obj (n):
	''''''
	global objects
	del objects[n-1]

def search_xy (xy):
	for obj in objects:
		if obj.xy == xy:
			return [True, obj.t, obj.number]
	return False

def line (xy1, xy2, obj):
	for xy in line_xy (xy1, xy2):
		new_object (obj (xy[0], xy[1]))

def square (xy1, xy2, obj):
	line (xy1, [xy2[0], xy1[1]], obj)
	line (xy1, [xy1[0], xy2[1]], obj)
	line ([xy2[0], xy1[1]], xy2, obj)
	line ([xy1[0], xy2[1]], xy2, obj)

def filled_square (xy1, xy2, obj):
	max_y = max([xy1[1], xy2[1]])
	min_y = min([xy1[1], xy2[1]])
	x = min([xy1[0], xy2[0]])
	while x != max([xy1[1], xy2[1]]):
		line ([x, min_y], [x, max_y], obj)
		x += 1

def upbating_obj ():
	global objects
	for i in range (len(objects)):
		objects[i].number = i

#point
def point(xy, skin):
	global world
	a = list(world[xy[1]])
	a[xy[0]] = skin
	world[xy[1]] = a

def kill_point (xy):
	point (xy, skin_of_world)

def line_xy (xy1, xy2):
	all_xy = []
	if xy1[0] == xy2[0]:
		x = xy1[0]
		tmp = [xy1[1], xy2[1]]
		for y in range (max(tmp)-min(tmp)+1):
			all_xy.append ([x, min(tmp)+y])
	elif xy1[1] == xy2[1]:
		y = xy1[1]
		tmp = [xy1[0], xy2[0]]
		for x in range (max(tmp)-min(tmp)+1):
			all_xy.append ([min(tmp)+x, y])
	else:
		print ("ERROR: заданны неверные координаты. |К сожалению движок умеет работать только с паралельными к границам экрана линиями.|")
	return all_xy

#touch
def checking_line (xy1, xy2, t):
	tmp = []
	for xy in line_xy (xy1, xy2):
		tmp2 = search_xy(xy)
		if t == tmp2[1]:
			tmp.append ([xy, search_xy(xy)[2]])
	return tmp

def checking_point (xy):
	for i in objects:
		if i.xy == xy:
			return [i.t, xy, i.number]
	return False

def checking_filled (xy1, xy2, t):
	tmp = []
	max_y = max([xy1[1], xy2[1]])
	min_y = min([xy1[1], xy2[1]])
	x = min([xy1[0], xy2[0]])
	while x != max([xy1[1], xy2[1]]):
		tmp.append (checking_line ([x, min_y], [x, max_y], t))
		x += 1
	return tmp

def checking_square (xy1, xy2, t):
	tmp = []
	tmp.append (checking_line (xy1, [xy2[0], xy1[1]], t))
	tmp.append (checking_line (xy1, [xy1[0], xy2[1]], t))
	tmp.append (checking_line ([xy2[0], xy1[1]], xy2, t))
	tmp.append (checking_line ([xy1[0], xy2[1]], xy2, t))
	return tmp

def checking_line_2(xy, n):
	x = xy[0]
	y = xy[1]
	if n == 0:
		while y != 0:
			y -= 1
			t = checking_point ([x,y])
			if t != -1:
				return t
	if n == 1:
		while x != width:
			x += 1
			t = checking_point ([x,y])
			if t != -1:
				return t
	if n == 2:
		while y != height:
			y += 1
			t = checking_point ([x,y])
			if t != -1:
				return t
	if n == 3:
		while x != 0:
			x -= 1
			t = checking_point ([x,y])
			if t != -1:
				return t
	return -1
	
def checking_touch (xy):
	tmp = [None, None, None, None]
	tmp[0] = (checking_point ([xy[0], xy[1]-1]))
	tmp[1] = (checking_point ([xy[0]+1, xy[1]]))
	tmp[2] = (checking_point ([xy[0], xy[1]+1]))
	tmp[3] = (checking_point ([xy[0]-1, xy[1]]))
	return tmp
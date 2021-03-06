from tkinter import *
from time import *
from random import *
from math import *
from tkinter import Tk

root = Tk()
root.title("Input")

w = 600
h = w
figure = [[0 for i in range(w)] for j in range(h)]
dots = [[0 for i in range(w)] for j in range(h)]
sequ = []

can = Canvas(root, width=w, height=h, bg='white')
can.pack()


class point():
	x = 0
	y = 0


class Vertex():
	x = 0
	y = 0
	visible = False


class polygon():
	def line(self, x, y, x1, y1):
		global can
		can.create_line(x, y, x1, y1)
		root.update()
		return

	mash = 50
	global w
	global h

	def get_rasm(self):
		global w, h
		for i in range(h // self.mash):
			self.line(0, i * self.mash, w, i * self.mash)
			self.line(i * self.mash, 0, i * self.mash, w)
		root.update()
		return

	def fill_cell(self, x, y):
		global w, h
		n1 = x // self.mash
		n2 = y // self.mash
		global can
		global figure
		figure[n1][n2] = 1
		can.create_rectangle(n1 * self.mash, n2 * self.mash, n1 * self.mash + self.mash, n2 * self.mash + self.mash,
		                     fill="#000000", outline="#1f1f1f")
	def fill_dot(self, x, y):
		global can
		global dots
		x = x // self.mash * self.mash
		y = y // self.mash * self.mash
		nx = x // self.mash
		ny = y // self.mash
		dots[nx][ny] = 1
		if len(sequ) != 0:
			if sequ [-1] != [x, y]:
				sequ.append([x, y])
		else:
			sequ.append([x, y])
		if len(sequ) > 1:
			can.create_line(sequ[-2][0], sequ[-2][1], sequ[-1][0], sequ[-1][1], fill="blue", width=3)
			can.create_oval(sequ[-2][0]-2, sequ[-2][1]-2, sequ[-2][0]+2, sequ[-2][1]+2, fill="red", outline="red")
		can.create_oval(x-2, y-2, x+2, y+2, fill="red", outline="red")


def upd_mouse(event):
	x = event.x
	y = event.y
	global mouse
	mouse.x = x
	mouse.y = y
	return


def getError(event):
	global root
	root.destroy()
	root_ = Tk()
	root_.title("Error!")
	l1 = Label(text='Error!', font='Arial 32')
	l1.pack()
	root_.mainloop()


def putFill():
	global mouse
	global poly
	#poly.fill_cell(mouse.x, mouse.y)
	poly.fill_dot(mouse.x, mouse.y)


def putFillOn(event):
	global filling
	filling = True


def putFillOff(event):
	global filling
	filling = False
	global main
	main = False



def fromDotsToString(a):
	ans = ''
	for i in range(1, len(a)):
		x = a[i - 1][0]
		y = a[i - 1][1]
		x1 = a[i][0]
		y1 = a[i][1]
		dir = max(abs(x - x1), abs(y - y1))
		if (dir == abs(x - x1)) and (x1 - x > 0):
			ans += 'x'
		elif (dir == abs(x - x1)) and (x1 - x < 0):
			ans += '-x'
		elif (dir == abs(y - y1)) and (y1 - y < 0):
			ans += 'y'
		elif (dir == abs(y - y1)) and (y1 - y > 0):
			ans += '-y'
	return ans

poly = polygon()
poly.mash = 30
poly.get_rasm()
mouse = point()
main = True
filling = False

root.bind('<Motion>', upd_mouse)
root.bind('<ButtonPress-1>', putFillOn)
root.bind('<ButtonRelease-1>', putFillOff)

while main:
	if filling:
		putFill()
	can.update()

dots.append(dots[0])
ans = fromDotsToString(sequ)
#print(ans)
root.destroy()

def fromStringToArray(s):
    q = []
    fl = True
    for i in range(len(s)):
        if fl:
            if s[i] == '-':
                fl = False
                q.append(s[i:i + 2:])
            else:
                q.append(s[i])
        else:
            fl = True
    #print(q)
    return q

def fromArrayToString(s):
    ans = ''
    for i in s:
        ans += i
    return ans

def negative(s):
	if s == 'x':
		return '-x'
	if s == '-x':
		return 'x'
	if s == 'y':
		return '-y'
	if s == '-y':
		return 'y'

def getPrime(s):
	# getting prime array from array s
	i = 0
	a = s.copy()
	while i < (len(s) - 1):
			if s[i] == negative(s[i + 1]):
				s = s[:i:] + s[i+2::]
				i = 0
			i += 1
	while (a != s):
		a = s.copy()
		while i < (len(s) - 1):
			if s[i] == negative(s[i + 1]):
				s = s[:i:] + s[i+2::]
				i = 0
			i += 1
	return s
	
ans = fromStringToArray(ans)
ans = getPrime(ans)
ans = fromArrayToString(ans)
print(ans)
class trihexagonal():
	global w
	global h
	root_tri = Tk()
	root_tri.title("Editing_In_Trihexagonal")
	
	Can = Canvas(root_tri, width = w, height = h, bg = 'white')
	Can.pack()
	
	def line(self, x, y, x1, y1):
		self.Can.create_line(x, y, x1, y1)
		self.root_tri.update()
		return

	def red_line(self, x, y, x1, y1):
		self.Can.create_line(x, y, x1, y1, width = 5, fill = "red")
		self.root_tri.update()
		return

	global poly

	stepLong = poly.mash
	mash = sqrt(3) / 2 * stepLong

	def get_rasm(self):
		global w, h
		for i in range(-(h // self.stepLong), h // self.stepLong * 2):
			if i % 2 == 0:
				self.line(0, i * self.mash, w, i * self.mash)
			if i % 2 == 0:
				self.line(i * self.stepLong, 0, i * self.stepLong + int(h / self.mash / 2 * self.stepLong), h)
			else:
				self.line(i * self.stepLong, 0, i * self.stepLong - int(h / self.mash / 2 * self.stepLong), h)
		self.root_tri.update()
		return

	def next_permutation(self, x, y, s):
		if (y % (self.mash * 2) != 0):
			if s == 'y':
				if x % (self.stepLong * 2) != 0:
					y -= self.mash
					x -= self.stepLong // 2
				else:
					y -= self.mash
					x += self.stepLong // 2
			elif s == '-y':
				if x % (self.stepLong * 2) != 0:
					y += self.mash
					x += self.stepLong // 2
				else:
					y += self.mash
					x -= self.stepLong // 2
			elif s == 'x':
				x += self.stepLong
			elif s == '-x':
				x -= self.stepLong
		else:
			if s == 'y':
				y -= self.mash
				x -= self.stepLong // 2
			elif s == '-y':
				y += self.mash
				x += self.stepLong // 2
			elif s == '-x':
				y += self.mash
				x -= self.stepLong // 2
			elif s == 'x':
				y -= self.mash
				x += self.stepLong // 2
		return [x, y]
	# x # int(sqrt(3) / 2 * x)
	def get_figure(self, word):
		word = fromStringToArray(word)
		x, y = 6 * self.stepLong, 6 * self.mash
		for i in word:
			a = self.next_permutation(x, y, i)
			self.red_line(x, y, a[0], a[1])
			sleep(0.1)
			x, y = a[0], a[1]
		self.root_tri.update()
		return


class square():
	global w
	global h
	root_sq = Tk()
	root_sq.title("Editing_In_Square")
	
	Can = Canvas(root_sq, width = w, height = h, bg = 'white')
	Can.pack()
	
	def line(self, x, y, x1, y1):
		self.Can.create_line(x, y, x1, y1)
		self.root_sq.update()
		return
	
	def red_line(self, x, y, x1, y1):
		self.Can.create_line(x, y, x1, y1, width = 5, fill = "red")
		self.root_sq.update()
		return

	global poly

	mash = poly.mash
	stepLong = mash

	def get_rasm(self):
		global w, h
		for i in range(h // self.mash):
			self.line(0, i * self.mash, w, i * self.mash)
			self.line(i * self.mash, 0, i * self.mash, w)
		self.root_sq.update()
		return

	def get_figure(self, word):
		word = fromStringToArray(word)
		x, y = self.mash * 6, self.mash * 6
		for i in word:
			if i == 'y':
				self.red_line(x, y, x, y - self.stepLong)
				x, y = x, y - self.stepLong
			elif i == '-y':
				self.red_line(x, y, x, y + self.stepLong)
				x, y = x, y + self.stepLong
			elif i == 'x':
				self.red_line(x, y, x + self.stepLong, y)
				x, y = x + self.stepLong, y
			elif i == '-x':
				self.red_line(x, y, x - self.stepLong, y)
				x, y = x - self.stepLong, y
		self.root_sq.update()
		return

sq = square()
trihex = trihexagonal()
sq.get_rasm()
trihex.get_rasm()
sq.get_figure(ans)
trihex.get_figure(ans)
while True:
	sq.root_sq.update()

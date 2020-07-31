from tkinter import *
from time import *
from tkinter import Tk

root = Tk()
root.title("Input")

w = 600
h = w

can = Canvas(root, width = w, height = h, bg = 'white')
can.pack()

class point():
	x = 0
	y = 0

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

	def fill(self, x, y):
		global w, h
		n1 = x // self.mash
		n2 = y // self.mash
		global can
		can.create_rectangle(n1 * self.mash, n2 * self.mash, n1 * self.mash + self.mash, n2 * self.mash + self.mash, fill = "#000000", outline = "#1f1f1f")

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
	l1 = Label(text = 'Error!', font = 'Arial 32')
	l1.pack()
	root_.mainloop()

def putFill():
	global mouse
	global poly
	poly.fill(mouse.x, mouse.y)

def putFillOn(event):
	global fill
	fill = True

def putFillOff(event):
	global fill
	fill = False
	global main
	main = False

poly = polygon()
poly.get_rasm()
mouse = point()
fill = False
main = True

root.bind('<Motion>', upd_mouse)
root.bind('<ButtonPress-1>', putFillOn)
root.bind('<ButtonRelease-1>', putFillOff)

while main:
	if fill:
		putFill()
	can.update()

root.mainloop()

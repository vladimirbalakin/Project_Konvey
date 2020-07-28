from tkinter import *
from time import *

root = Tk()
root.title("D is d really?")

w = 600
h = 600
onoff = True

can = Canvas(root, width = w, height = h, bg = 'white')
can.pack()

draw_f = False
last_x, last_y = w // 2, h // 2

class point():
    x = 300
    y = 300

def line(x, y, x1, y1):
    global can
    can.create_line(x, y, x1, y1)

mouse = point()

def upd_mouse(event):
    x, y = event.x, event.y
    global mouse
    mouse.x = x
    mouse.y = y

Non_Del = []

def non_del():
    global Non_Del
    global line
    for i in Non_Del:
        line(i[0], i[1], i[2], i[3])

def new_ndl(event):
    global Non_Del
    global last_x
    global last_y
    global mouse
    global draw_f
    if draw_f:        
        Non_Del.append([last_x, last_y, mouse.x, mouse.y])
        last_x, last_y = mouse.x, mouse.y

def on(event):
    global draw_f
    global last_x
    global last_y
    global mouse
    global onoff
    draw_f = not(draw_f)
    onoff = draw_f
    last_x, last_y = mouse.x, mouse.y
    
root.bind('<Motion>', upd_mouse)
root.bind('<Double-Button-1>', on)
root.bind('<Button-1>', new_ndl)


while onoff:
    if draw_f:
        line(last_x, last_y, mouse.x, mouse.y)
    can.update()
    can.delete("all")
    non_del()

s = ""

for i in Non_Del:
    q = max(abs(i[0] - i[2]), abs(i[1] - i[3]))
    if abs(q) == abs(i[0] - i[2]) and i[0] - i[2] < 0:
        s += 'x'
    elif abs(q) == abs(i[0] - i[2]) and i[0] - i[2] > 0:
        s += '-x'
    elif abs(q) == abs(i[1] - i[3]) and i[1] - i[3] > 0:
        s += 'y'
    elif abs(q) == abs(i[1] - i[3]) and i[1] - i[3] < 0:
        s += '-y'
    #print(q, s)

print(s)

root.mainloop()

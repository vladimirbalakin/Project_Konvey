import turtle
from tkinter import *
from time import *

root = Tk()
root.title("D is d really?")

w = 600
h = 600
onoff = True

can = Canvas(root, width=w, height=h, bg='white')
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
    draw_f = not (draw_f)
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
    # print(q, s)

print(s)


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
    print(q)
    return q


q = fromStringToArray(s)


def do_prime(q):
    coor = [[0, 0]]
    for i in q:
        if i == 'y':
            coor.append([coor[-1][0], coor[-1][1] - 100])
        elif i == '-y':
            coor.append([coor[-1][0], coor[-1][1] + 100])
        elif i == 'x':
            coor.append([coor[-1][0] + 100, coor[-1][1]])
        else:
            coor.append([coor[-1][0] - 100, coor[-1][1]])
    print(coor)
    if not(coor[0][0] == coor[-1][0] and coor[0][1] == coor[-1][1]):
        return ''
    n = len(coor)
    upr = []
    fl = True
    for i in range(1, n):
        if fl:
            for j in range(i + 1, n):
                if coor[i][0] == coor[j][0] and coor[i][1] == coor[j][1]:
                    upr.append([i, j])
                    fl = False
        else:
            if i == upr[-1][1]:
                fl = True
    print(upr)
    ans = []
    fl = True
    last = -1
    ssd = 0
    clac = False
    for i in range(n):
        if fl:
            ans.append([coor[i][0], coor[i][1]])
        else:
            if i == last:
                fl = True

        try:
            if upr[ssd][0] == i:
                fl = False
                last = upr[ssd][1]
                clac = True
            if clac:
                i += 1
                clac = False
        except:
            pass
    print(ans)
    anss = []
    for i in range(1, len(ans)):
        anss.append([ans[i - 1][0], ans[i - 1][1], ans[i][0], ans[i][1]])
    anss.append([ans[-1][0], ans[-1][1], ans[0][0], ans[0][1]])
    end = ''
    for i in anss:
        q = max(abs(i[0] - i[2]), abs(i[1] - i[3]))
        if abs(q) == abs(i[0] - i[2]) and i[0] - i[2] < 0:
            end += 'x'
        elif abs(q) == abs(i[0] - i[2]) and i[0] - i[2] > 0:
            end += '-x'
        elif abs(q) == abs(i[1] - i[3]) and i[1] - i[3] > 0:
            end += 'y'
        elif abs(q) == abs(i[1] - i[3]) and i[1] - i[3] < 0:
            end += '-y'
        # print(q, s)
    return end


q = do_prime(q)
print(q)
root.mainloop()
endArray = []
endArray = fromStringToArray(q)
from turtle import *
t = turtle.Turtle()
t.speed(0)
t.down()
t.hideturtle()
x = 0
y = 0
for i in endArray:
    if i == 'x':
        x += 100
    elif i == '-x':
        x -= 100
    elif i == 'y':
        y += 100
    else:
        y -= 100
    t.goto(x, y)
sleep(10)
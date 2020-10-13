import turtle
from time import *

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

def north(i):
    i %= 2
    if i == 0:
        turtle.setheading(120)
    else:
        turtle.setheading(120+30)
def east():
    turtle.setheading(0)
def south(i):
    i %= 2
    if i == 0:
        turtle.setheading(300)
    else:
        turtle.setheading(300+30)
def west():
    turtle.setheading(180)

a = input()
a = fromStringToArray(a)
j = 0
for i in a:
    if i == 'y':
        north(j)
    elif i == '-y':
        south(j)
    elif i == 'x':
        east()
    elif i == '-x':
        west()
    turtle.forward(10)
    j += 1
turtle.done()
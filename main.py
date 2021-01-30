import matplotlib.pyplot as plt
import networkx as nx
from tkinter import *


def zhopa(event):
    print(c.find_closest(event.x, event.y))
root = Tk()
x_number, y_number= 10,10
width, height = 100*x_number, 100*y_number
c = Canvas(width=width, height=height)
graph = [[0 for i in range(y_number)] for biba in range(x_number)]
x_pos, y_pos = 0,0
for x in range(x_number):
    for y in range(y_number):
        c.create_rectangle(x_pos, y_pos, x_pos+100, y_pos+100)
        x_pos += 50
    x_pos = 0
    y_pos += 50


root.bind('<Button-1>', zhopa)
c.pack()
root.mainloop()
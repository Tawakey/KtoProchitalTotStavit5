import matplotlib.pyplot as plt
import networkx as nx
from tkinter import *


def poisk(graph, dot_x, dot_y, visited, x_number, y_number):
    neighbours = [(-1,0), (1, 0), (0, 1), (0, -1)]

        



root = Tk()
x_number, y_number= 8,8
width, height = 100*x_number + 100, 100*y_number
c = Canvas(width=width, height=height)
graph = [[0 for i in range(y_number)] for biba in range(x_number)]
start = [False, None, None, None]
finish = [False, None, None, None]
filled = [0 for i in range(100)]
visited = []
path = []

def zhopa(event):
    global graph, x_number
    graph_x = (event.x//100)+1  
    graph_y = (event.y//100)
    tk_id = graph_x+(event.y//100)*x_number
    print(graph_x, graph_y)
    if not filled[tk_id]:
        c.itemconfig(tk_id, fill='red')
        filled[tk_id] = 1
        graph[graph_y][graph_x-1] = 1
    else:
        c.itemconfig(tk_id, fill = 'white')
        filled[tk_id] = 0
        graph[graph_y][graph_x-1] = 0
    [print(*i) for i in graph]
    print('\n')


def biba(event):
    global start, finish, graph, x_number
    graph_x = (event.x//100)+1
    graph_y = (event.y//100)
    tk_id = graph_x+(event.y//100)*x_number
    if not start[0]:
        c.itemconfig(tk_id, fill = 'green')
        start[0] = True
        start[-1] = tk_id
        graph[graph_y][graph_x-1] = 2
        start[1] = graph_y
        start[2] = graph_x
    else:
        if tk_id == start[-1]: 
            c.itemconfig(tk_id, fill = 'white')
            start[0] = False
            start[-1] = None
            graph[start[1]][start[2]-1] = 0
            start[1] = None
            start[2] = None
        else:
            if finish[-1] == tk_id:
                c.itemconfig(tk_id, fill = 'white')
                finish[0] = False
                finish[-1] = None
                graph[finish[1]][finish[2]-1] = 0
                finish[1] = None
                finish[2] = None
            else:
                if finish[0]:
                    c.itemconfig(finish[-1], fill = 'white')
                    c.itemconfig(tk_id, fill = 'gold')
                    graph[finish[1]][finish[2]-1] = 0
                    graph[graph_y][graph_x-1] = 3
                    finish[1] = graph_y
                    finish[2] = graph_x
                    finish[-1] = tk_id
                else:
                    c.itemconfig(tk_id, fill = 'gold')
                    graph[graph_y][graph_x-1] = 3
                    finish[1] = graph_y
                    finish[2] = graph_x
                    finish[0] = True
                    finish[-1] = tk_id
    print(finish[0])
    [print(*i) for i in graph]
    print('\n')
x_pos, y_pos = 0,0

for x in range(x_number):
    for y in range(y_number):
        c.create_rectangle(x_pos, y_pos, x_pos+100, y_pos+100)
        x_pos += 100
    x_pos = 0
    y_pos += 100
[c.itemconfig(id, fill = 'white') for id in range(100)]

root.bind('<Button-1>', zhopa)
root.bind('<Button-3>', biba)
c.pack()
root.mainloop()
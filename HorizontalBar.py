from Canvas import Canvas
import random

class HorizontalBar:
    def __init__(self, x, labels, values, title, label_max_size=5):
        self.x = x
        self.labels = labels
        self.values = values
        self.title = title
        self.y = len(self.labels)+3
        self.label_max_size = label_max_size
        self.canvas = Canvas(self.x+self.label_max_size+1, self.y)

    def insert(self, task):
        self.labels.append(task)
    def add_value(self, value):
        self.value=value
    def update(self):
        for j, c in enumerate(self.title):
            self.canvas.putPoint(j, 0, c)
        for j in range(self.x):
            self.canvas.putPoint(j+self.label_max_size+1, 2, str(j)+" ")
            if j in range(9):
                self.canvas.putPoint(j+self.label_max_size+1, 1, "|-")
            elif j > 9:
                self.canvas.putPoint(j+self.label_max_size+1, 1, "-|-") 
        for y, l in enumerate(self.labels):
            for x, c in enumerate(l):
                self.canvas.putPoint(self.label_max_size+1, y+3,"|")
                self.canvas.putPoint(x, y+3, c)
        for j, v in enumerate(self.values):
            for x in range(v[0]):
                self.canvas.putPoint(self.label_max_size+x+2, j+3, v[1])
    def show_diagram(self):
        self.canvas.drawCanvas()

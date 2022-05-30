from Canvas import Canvas
import random

class HorizontalBar:
    def __init__(self, x, tasks, values):
        self.x = x
        self.tasks = tasks
        self.values = values
        self.y = len(self.tasks)
        self.canvas = Canvas(self.x, self.y)
    def insert(self, task):
        self.tasks.append(task)
    def add_value(self, value):
        self.value=value
    def update(self):
        for i, e in enumerate(self.tasks):
            print("\033[0;0;0m")
            self.canvas.putPoint(len(e), i, "|")
            for j, c in enumerate(e):
                self.canvas.putPoint(j, i, c)
        for i, v in enumerate(self.values):
            for x in range(v[0]):
                self.canvas.putPoint(len(tasks[i])+1+x, i, v[1])
    def show_diagram(self):
        self.canvas.drawCanvas()

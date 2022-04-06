from tkinter import *
from random import randint
from time import sleep


class Potop:
    def __init__(self, c, r, cl, width, height):
        self.c = c
        self.cell = []
        self.r = r + 2
        self.cl = cl + 2
        self.width = width
        self.height = height
        self.count = 0
        s = randint(10, 50)
        for i in range(self.r):
            self.cell.append([])
            for j in range(self.cl):
                self.cell[i].append(0)

        self.cell[i][j] = 4
        self.cell[i][j] = 4
        # noev covcheg
        self.cell[s][s] = 1
        self.cell[s][s] = 1
        self.cell[s][s] = 1
        self.cell[s][s] = 1
        self.cell[s][s] = 1
        # my creativity while doing this
        self.cell[s][s] = 2
        self.cell[s][s] = 2
        self.cell[s][s] = 2
        self.cell[s][s] = 2
        # great flood
        self.cell[s][s] = 3
        self.cell[s][s] = 3
        self.cell[s][s] = 3
        self.cell[s][s] = 3
        self.cell[s][s] = 3
        # mythical creatures
        self.cell[s][s] = 5
        # observer

        self.paint()

    def animate(self):
        sc = []
        for i in range(self.r):
            sc.append([])
            for j in range(self.cl):
                sc[i].append(0)

        for i in range(1, self.r - 1):
            for j in range(1, self.cl - 1):
                n = self.cell[i-1][j-1]+self.cell[i-1][j]+self.cell[i-1][j+1]+self.cell[i][j-1]+self.cell[i-1][j+1]+self.cell[i+1][j-1]+self.cell[i+1][j] + self.cell[i+1][j+1]
                if n == 1:
                    sc[i][j] = 0
                elif n > 3:
                    sc[i][j] = 2
                    sc[25][25] = 4
                    sc[24][25] = 4
                elif n == 2:
                    sc[i][j] = 3
                elif n == 3:
                    sc[i][j] = 1
                    sc[45][5] = 5
                else:
                    sc[i][j] = self.cell[i][j]

        self.cell = sc

    def show(self):
        for i in range(self.r):
            for j in range(self.cl):
                print(self.cell[i][j], end="")
            print()

    def observer(self):
            color = "white"
            z = self.width // (self.r - 2)
            scl = self.height // (self.cl - 2)
            for i in range(1, self.r - 1):
                for j in range(1, self.cl - 1):
                    if (self.cell[i][j] == 5):
                        color = "white"
                    self.c.create_circle((i-1)*z, (j-1)*scl, (i)*z, (j)*scl)
            self.animate()
            self.c.after(100, self.paint)

    def paint(self):
        szr = self.width // (self.r - 2)
        scl = self.height // (self.cl - 2)
        for i in range(1, self.r - 1):
            for j in range(1, self.cl - 1):
                if (self.cell[i][j] == 1):
                    color = "pink"
                elif (self.cell[i][j] == 2):
                    color = "skyblue1"
                elif (self.cell[i][j] == 3):
                    color = "lightseagreen"
                elif (self.cell[i][j] == 4):
                    color = "peachpuff4"
                elif (self.cell[i][j] == 5):
                    color = "white"
                else:
                    color = "darkseagreen1"
                self.c.create_rectangle((i-1)*szr, (j-1)*scl, (i)*szr, (j)*scl, fill=color)
        sleep(0.4)
        self.animate()
        self.c.after(100, self.paint)

root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()

p = Potop(c, 50, 50, 800, 800)
p.show()

root.mainloop()

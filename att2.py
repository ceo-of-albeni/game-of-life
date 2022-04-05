from tkinter import *
# from time import sleep
from random import randint

 
class Potop:
    def __init__(self, c, r, cl, width, height):
        self.c = c
        self.cell = []
        self.r = r + 2
        self.cl = cl + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.r):
            self.cell.append([])
            for j in range(self.cl):
                self.cell[i].append(0)
       
        self.cell[i][j] = 4
        self.cell[i][j] = 4
        # noev covcheg
        self.cell[randint(10, 40)][randint(10, 40)] = 1
        self.cell[randint(10, 40)][randint(10, 40)] = 1
        self.cell[randint(10, 40)][randint(10, 40)] = 1
        self.cell[randint(10, 40)][randint(10, 40)] = 1
        self.cell[randint(10, 40)][randint(10, 40)] = 1
        # my creativity while doing this
        self.cell[randint(10, 40)][randint(10, 40)] = 2
        self.cell[randint(10, 40)][randint(10, 40)] = 2
        self.cell[randint(10, 40)][randint(10, 40)] = 2
        self.cell[randint(10, 40)][randint(10, 40)] = 2
        # great flood
        self.cell[randint(10, 40)][randint(10, 40)] = 3
        self.cell[randint(10, 40)][randint(10, 40)] = 3
        self.cell[randint(10, 40)][randint(10, 40)] = 3
        self.cell[randint(10, 40)][randint(10, 40)] = 3
        self.cell[randint(10, 40)][randint(10, 40)] = 3
        # mythical creatures
        

        self.draw()
   
    def step(self):
        sc = []
        for i in range(self.r):
            sc.append([])
            for j in range(self.cl):
                sc[i].append(0)

        for i in range(1, self.r - 1):
            for j in range(1, self.cl - 1):
                sosedi = self.cell[i - 1][j - 1] + self.cell[i - 1][j] + self.cell[i - 1][j + 1] + self.cell[i][j - 1] + self.cell[i - 1][j + 1] + self.cell[i + 1][j - 1] + self.cell[i + 1][j] + self.cell[i + 1][j + 1]
                if sosedi == 1:
                    sc[i][j] = 0
                elif sosedi > 3:
                    sc[i][j] = 2
                    sc[20][20] = 4
                    sc[19][20] = 4
                elif sosedi == 2:
                    sc[i][j] = 3
                elif sosedi == 3:
                    sc[i][j] = 1
                else:
                    sc[i][j] = self.cell[i][j]
       
        self.cell = sc
 
 
    def printing(self):
        for i in range(self.r):
            for j in range(self.cl):
                print(self.cell[i][j], end="")
            print()
 
    def draw(self):
        sizer = self.width // (self.r - 2)
        sizecl = self.height // (self.cl - 2)
        for i in range(1, self.r - 1):
            for j in range(1, self.cl - 1):
                if (self.cell[i][j] == 1):
                    color = "pink"
                elif (self.cell[i][j] == 2):
                    color = "skyblue1"
                elif (self.cell[i][j] == 3):
                    color = "lightseagreen"
                elif (self.cell[i][j] == 4):
                    color = "brown"
                else:
                    color = "darkseagreen1"
                self.c.create_rectangle((i-1) * sizer, (j-1) * sizecl, (i) * sizer, (j) * sizecl, fill=color)
        self.step()
        self.c.after(100, self.draw)
 

root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()
 
f = Potop(c, 40, 40, 800, 800)
f.printing()
 
 
root.mainloop()
# c.create_oval(p.x + 5,p.y + 5,p.x+p.size + 5,p.y+p.size + 5)
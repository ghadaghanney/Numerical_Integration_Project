from numpy import sin, cos, exp, log, sqrt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
matplotlib.use('TkAgg')
from tkinter import messagebox as msg


class RectangleG (object):
    def __init__(self, a, b, n, f, aa):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.aa = aa

    def integrate(self, f):
        x = self.x
        y = [f(xx) for xx in x]
        h = float(x[1] - x[0])
        s = sum(y[0: -1])
        return h * s

    def Graph(self, f, resolution=1001):
        xl = self.x
        yl = [f(x) for x in xl]
        xlist_fine = np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i + 1], xl[i+1], xl[i]]
            y_rect = [0, yl[i], yl[i], 0, 0]  
            self.aa.plot(x_rect, y_rect, 'r')
        yflist_fine = [f(x) for x in xlist_fine]
        self.aa.plot(xlist_fine, yflist_fine)
        self.aa.plot(xl, yl, "bo")
        


class Simpson(object):
    def __init__(self, a, b, n, f, aa): 
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1) 
        self.f = f
        self.n = n  # Nombre de subdivision
        self.c = aa
    

    def integrate(self, f):
        x = self.x  
        y = [f(xx) for xx in x] 
        h = float(x[1] - x[0])  
        n = len(x) - 1 
        if n % 2 == 1: 
            n -= 1 
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        return h * s / 3.0

    def Graph(self, f, resolution=1001):  
        xl = self.x  
        yl = [f(x) for x in xl] 
        xlist_fine = np.linspace(self.a, self.b, resolution)
       
        for i in range(self.n):  
            xx = np.linspace(xl[i], xl[i+1], resolution)
            
            m = (xl[i]+xl[i+1])/2  
            aa = xl[i]  
            bb = xl[i+1] 
            l0 = (xx-m)/(aa-m)*(xx-bb)/(aa-bb)
            l1 = (xx-aa)/(m-aa)*(xx-bb)/(m-bb)
            l2 = (xx-aa)/(bb-aa)*(xx-m)/(bb-m)
            P = f(aa)*l0 + f(m)*l1 + f(bb)*l2  
            self.c.plot(xx, P, 'b')  
            self.c.plot(m, f(m), "r*")
        yflist_fine = [f(x) for x in xlist_fine]  
        self.c.plot(xlist_fine, yflist_fine, 'g')
        self.c.plot(xl, yl, 'bo')  
        


class Milieu(object):  
    def __init__(self, a, b, n, f, aa):  
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.aa = aa

    def integrate(self, f):
        x = self.x  
        h = float(x[1] - x[0])
        s = 0
        for i in range(self.n):
            s = s+f((x[i]+x[i+1])*0.5)
        return h*s

    def Graph(self, f, resolution=1001):
        xl = self.x
        yl = [f(x) for x in xl]
        xlist_fine = np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            m = (xl[i]+xl[i+1])/2
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]]
            y_rect = [0, f(m), f(m), 0, 0]  
            self.aa.plot(x_rect, y_rect, "r")
            self.aa.plot(m, f(m), "b*")

        yflist_fine = [f(x) for x in xlist_fine]
        self.aa.plot(xlist_fine, yflist_fine, 'g')
       


class Trapezoidal(object):
    def __init__(self, a, b, n, f, aa):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.aa = aa

    def integrate(self, f):
        x = self.x
        y = [f(xx) for xx in x]
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0

    def Graph(self, f, resolution=1001):
        xl = self.x
        yl = [f(x) for x in xl]
        xlist_fine = np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]]
            y_rect = [0, yl[i], yl[i+1], 0, 0] 
            self.aa.plot(x_rect, y_rect, "m")
        yflist_fine = [f(x) for x in xlist_fine]
        self.aa.plot(xlist_fine, yflist_fine)
        self.aa.plot(xl, yl, "cs")  



class mclass:
    def __init__(self,  window):
        self.window = window
        self.fr1 = Frame(window, highlightbackground="#2F4F4F",highlightthickness=2, width=100, height=100, bd=5)
        self.fr2 = Frame(window, highlightbackground="#2F4F4F",highlightthickness=2, width=100, height=100, bd=5)

        #expression f 
        self.func_txt = StringVar()
        self.func_txt.set("L'expression de f :")
        self.label_func = Label(self.fr1, textvariable=self.func_txt, justify=RIGHT, height=4)
        self.label_func.grid(row=1, column=0)
        self.label_func.config(font=("Courier", 12))

        #box a
        self.a_txt = StringVar()
        self.a_txt.set("Borne a:")
        self.label_a = Label(self.fr1, textvariable=self.a_txt, font=("Arial", 10),justify=RIGHT, anchor="w", height=4)
        self.label_a.grid(sticky=E, row=2, column=0)
        self.label_a.config(font=("Courier", 12))
        self.boxa = Entry(self.fr1, width=10, borderwidth=3)
        self.boxa.grid(sticky=W, row=2, column=1)
        self.boxa.insert(0, '-4')

        #box b
        self.b_txt = StringVar()
        self.b_txt.set("Borne b :")
        self.label_b = Label(self.fr1, textvariable=self.b_txt, font=("Arial", 10),justify=RIGHT, anchor="w", height=4)
        self.label_b.grid(sticky=E, row=3, column=0)
        self.boxb = Entry(self.fr1, width=10, borderwidth=3)
        self.boxb.grid(sticky=W, row=3, column=1)
        self.label_b.config(font=("Courier", 12))

        self.box = Entry(self.fr1, borderwidth=3)
        self.box.grid(row=1, column=1)
        self.boxn = Entry(self.fr1, borderwidth=3, textvariable="3")
        self.boxn.grid(sticky=W, row=4, column=1)
        self.boxn.delete(0, END)
        self.boxn.insert(0, "8")

        #Nombre de N 
        self.n_txt = StringVar()
        self.n_txt.set("Nombre de N :")
        self.label_n = Label(self.fr1, textvariable=self.n_txt,justify=RIGHT, anchor="w", height=4)
        self.label_n.grid(sticky=E, row=4, column=0)
        self.label_n.config(font=("Courier", 12))
        
        #Choisir methode 
        self.c_txt = StringVar()
        self.c_txt.set("Choisir La méthode : ")
        self.label_in = Label(self.fr1, textvariable=self.c_txt, justify=RIGHT, anchor='w', height=4)
        self.label_in.grid(sticky=E, row=5, column=0)
        self.label_in.config(font=("Courier", 12))
        self.combo = Combobox(self.fr1)
        self.combo['values'] = (' Point Milieu',' Trapèze',' rectangle',' Simpson')
        self.combo.grid(sticky=W, row=5, column=1)
        self.combo.current(0)

        #plot
        self.button = Button(self.fr1, width=25, text="PLOT",bg="coral", fg="white", command=self.plot)
        self.button.grid(row=6, column=0, columnspan=3)
        self.fr1.grid(row=1, column=0, padx=10, pady=10, sticky="ns")
        self.fr2.grid(row=1, column=1, padx=10, pady=10)

        #Bouton quitter
        self.button = Button(self.fr1, width =25,text="QUITTER",bg="coral",fg="white", command=self.choice_box)
        self.button.grid(row=12,column=0,columnspan=3)
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)

     
        #figure
        self.fig = Figure(figsize=(4, 4))
        self.a = self.fig.add_subplot(111)
        self.a.set_title("GRAPHE DE f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.boxb.insert(0, "4")
        self.box.insert(0, 'sin(x)')

    def plot(self):
        def f(x): return eval(self.box.get())
        x = np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
        pp = f(x)
        self.a.cla()
        self.a.set_ylim([-3, 10])
        self.a.xaxis.set_ticks(np.arange(-3, 8, 1))
        self.a.yaxis.set_ticks(np.arange(-3, 8, 1))
        self.a.set_title("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.grid(True)
        self.a.plot(x, f(x), color='blue')
        dic = {' rectangle': RectangleG, ' Trapèze': Trapezoidal,' Point Milieu': Milieu, ' Simpson': Simpson}
        s = self.combo.get()
        R = dic[s](float(self.boxa.get()), float(self.boxb.get()), int(self.boxn.get()), f, self.a)
        R.Graph(f)
        self.fig.canvas.draw()

    def choice_box(self):
          answer = msg.askyesnocancel("Attention", "Voulez-vous quitter !!")
 
          if answer == True:
             self.window.quit()


if __name__=='__main__' :
    window= Tk()
    window.title("Intégration Numérique")
    start = mclass(window)
    
    # Gets the requested values of the height and widht.
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    print("Width",windowWidth,"Height",windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/4 - windowWidth/3)
    positionDown = int(window.winfo_screenheight()/4 - windowHeight/3)
 
    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))

    window.mainloop()   
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from numpy import sin ,cos,exp,log,sqrt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter.font as font
from tkinter import messagebox as msg
import tkinter as tk

class mclass:
    def __init__(self,  window):
        self.window = window
        self.fr1 = Frame(window,bg="white", highlightthickness=2, width=100, height=100, bd= 5)
        self.fr2 = Frame(window,bg="white", highlightthickness=2, width=100, height=100, bd= 5)

        

        self.func_txt=StringVar()
        self.func_txt.set("Expression of f :")
        self.label_func=Label(self.fr1, textvariable=self.func_txt,bg="white",justify=RIGHT, height=4, fg='blue')
        self.label_func.config(font=("Courier", 12))
        self.label_func.grid(row=1,column=0)
        
        
        

        self.a_txt=StringVar()
        self.a_txt.set("a:")
        self.label_a=Label(self.fr1, textvariable=self.a_txt,justify=RIGHT,bg="white", anchor="w", height=4, fg='blue')
        self.label_a.grid(sticky = E,row=2,column=0)
        self.label_a.config(font=("Courier", 12))
        self.boxa = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxa.grid(sticky = W,row=2,column=1)



        self.b_txt=StringVar()
        self.b_txt.set("b:")
        self.label_b=Label(self.fr1, textvariable=self.b_txt,justify=RIGHT,bg="white" ,anchor="w", height=4, fg='blue')
        self.label_b.grid(sticky = E,row=3,column=0)
        self.label_b.config(font=("Courier", 12))
        self.boxb = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxb.grid(sticky = W,row=3,column=1)
        self.box = Entry(self.fr1,borderwidth=3,bg="powder blue")
        self.box.grid(row=1,column=1)



        self.n_txt=StringVar()
        self.n_txt.set("Number of points :")
        self.label_n=Label(self.fr1, textvariable=self.n_txt,justify=RIGHT,bg="white" ,anchor="w", height=4, fg='blue')
        self.label_n.grid(sticky = E,row=4,column=0)
        self.label_n.config(font=("Courier", 12))
        self.boxn = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxn.grid(sticky = W,row=4,column=1)
        self.box = Entry(self.fr1,borderwidth=3,bg="powder blue")
        self.box.grid(row=1,column=1)
        



        self.button = Button (self.fr1, width =35,text="plot",bg="powder blue", command=self.plot)
        self.button.grid(row=5,column=0,columnspan=3)

        self.button = Button(self.fr1, width =35,text="Quite",bg="#acc085", command=self.choice_box)
        self.button.grid(row=6,column=0,columnspan=3)

    


        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)
        self.fig = Figure(figsize=(6,6))
        self.a = self.fig.add_subplot(111)
        self.a.set_title ("Graph f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.set_facecolor("white")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2 )
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def choice_box(self):
          answer = msg.askyesnocancel("Multi Choice Box Title", "Do You Want To Quite!")
 
          if answer == True:
             self.window.quit()  
             
    def plot (self):
        f= lambda x: eval(self.box.get())
        x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
        pp=f(x)
        self.a.cla()
        self.a.set_ylim([float(self.boxa.get()), float(self.boxb.get())])
        self.a.xaxis.set_ticks(np.arange(float(self.boxa.get()), float(self.boxb.get())+1, 1))
        self.a.yaxis.set_ticks(np.arange(float(self.boxa.get()), float(self.boxb.get())+1, 1))
        self.a.set_title ("Graph f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.grid(True)
        self.a.plot(x, f(x),color='blue')
        self.canvas.draw()





window= Tk()
window.title("Numerical Integration")
#window.iconbitmap("myicon.png")
#window.iconphoto(False, Tk.PhotoImage(file = 'myicon.png'))
#window.iconbitmap('icon.ico')


window.configure(background='#4D4D4D')  # give color for your window
window.resizable(False, False) # for preventing window resize
start= mclass(window)


window.mainloop()

from tkinter import *
import tkinter as tk



import sys
import os

w = tk.Tk()
w.title('NUMERICAL ANALYSIS')
#w.iconbitmap('my_icon.ico)
img = PhotoImage(file="hello.gif")
c = Canvas(w, bg ='black',width=600, height=600)
c.pack()
c.create_image(300, 300, image=img)

b3 = Button(w, text='QUITE',bg="magenta", fg="white",command = w.destroy)
b3.pack(padx=5, pady=5, side=RIGHT)

def run():
    os.system('python Runge_Project.py')

b2 = Button(w,text='RUNGE',bg="magenta", fg="white",command = run)
b2.pack(padx=5, pady=5, side=LEFT)

def run2():
    os.system('python 4methodes.py')

b1 = Button(w, text='NUMERICAL INTEGRATION',bg="magenta",fg="white", command = run2)
b1.pack(pady=5, side=LEFT)

w.resizable(width=False, height=False)




# Gets the requested values of the height and widht.
windowWidth = w.winfo_reqwidth()
windowHeight = w.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)


# Gets both half the screen width/height and window width/height
positionRight = int(w.winfo_screenwidth()/4 - windowWidth/3)
positionDown = int(w.winfo_screenheight()/4 - windowHeight/3)
 
# Positions the window in the center of the page.
w.geometry("+{}+{}".format(positionRight, positionDown))

w.mainloop()
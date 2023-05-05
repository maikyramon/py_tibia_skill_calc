from tkinter import *
from tkinter import messagebox
from math import *

vocation_constants = {
    '1': {'1600' : 3.0, '50': 1.1, '51': 1.1, '25': 1.4, '100': 1.1, '20': 1.1},
    '2': {'1600' : 1.4, '50': 1.2, '51': 1.2, '25': 1.1, '100': 1.1, '20': 1.1},
    '3': {'1600' : 1.1, '50': 2.0, '51': 1.5, '25': 2.0, '100': 1.5, '20': 1.1},
    '4': {'1600' : 1.1, '50': 1.8, '51': 1.5, '25': 1.8, '100': 1.5, '20': 1.1},
    '5': {'1600' : 4.0, '50': 2.0, '51': 1.5, '25': 2.0, '100': 1.5, '20': 1.1}
}

janela = Tk()

janela.title("calc skill tibia")

val_vocation = StringVar()
val_skill    = StringVar()

val_vocation.set(0)
val_skill.set(0)

vocations = [("knight",   1, 1),
   	         ("paladin",  2, 2),
    	     ("sorcerer", 3, 3),
             ("druid",    4, 4),
             ("none",     5, 5)]

skills = [("ml",        1600, 1),
   	      ("melee",     50,   2),
    	  ("distance",  25,   3),
          ("shielding", 100,  4),
          ("fishing",   20,   5),
          ("fisting",   51,   6),]


def calc_skill():
    global atual
    global desejada

    A = val_skill.get()
    b = val_vocation.get()
    skill_atual = int(atual.get())
    skill_desejada = int(desejada.get())
    b = float(vocation_constants[b][A])

    A = int(A)
    if A == 51: 
        A -= 1

    if A == 1600:
        c = 0
    else: 
        c = 10
    
    P = A * ((pow(b, skill_atual - c) - 1) / (b - 1))
    TP = A * ((pow(b, skill_desejada - c) - 1) / (b - 1))
    
    TP = TP - P

    sec = int(TP)

    hour = int(sec / 3600)
    sec  = sec % 3600
    min  = int(sec / 60)
    sec  = sec % 60
    
    messagebox.showinfo("Information",f'{hour} hours, {min} minutes, {sec} seconds, ou {int(TP)} golpes')


Label(janela, text="vocação: ").grid(column=0, row=0)
for vocation, val, column in vocations:
    Radiobutton(janela, text=vocation, variable=val_vocation, value=val).grid(column=column, row=0)


Label(janela, text="skill: ").grid(column=0, row=1)
for skill, val, column in skills:
    Radiobutton(janela, text=skill, variable=val_skill, value=val).grid(column=column, row=1)


Label(janela, text="skill atual: ").grid(column=0, row=2)
atual = Entry(janela, width=20, )
atual.grid(column=1, row=2)
#atual.focus_set()

Label(janela, text="skill desejada: ").grid(column=0, row=3)
desejada = Entry(janela, width=20)
desejada.grid(column=1, row=3)

Button(janela, text="calc", width=10, command=calc_skill).grid(column=1, row=4)


janela.mainloop()
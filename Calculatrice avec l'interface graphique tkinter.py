from tkinter import *
from math import*

#fenetre 
s=Tk()
s.title("Calculatrice")
entrer=Entry(s,width=14,borderwidth=9,bg="light blue",font=("Helvetica",26))
entrer.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#Les fonctions

    
def click(nombre):
    temp=entrer.get()
    entrer.delete(0,END)
    entrer.insert(0,str(temp)+str(nombre))

def factoriel() :
    global nombre1
    signe="!"
    nombre1=float(entrer.get())
    resultat=1
    while nombre1>=1:
        resultat = resultat * nombre1
        nombre1 = nombre1-1
    entrer.delete(0,END)
    entrer.insert(0,resultat)

def racine_carrée():
    global nombre1
    signe="!"
    nombre1=float(entrer.get())
    entrer.delete(0,END)
    entrer.insert(0,sqrt(nombre1))
    
def plus():
    global nombre1
    global signe
    signe="+"
    nombre1 = float (entrer.get())
    entrer.delete(0,END)
    
def moins():
    global nombre1
    global signe
    signe="-"
    nombre1 = float (entrer.get())
    entrer.delete(0,END)

def mult():
    global nombre1
    global signe
    signe="*"
    nombre1 = float (entrer.get())
    entrer.delete(0,END)
    
def div():
    global nombre1
    global signe
    signe="/"
    nombre1 = float (entrer.get())
    entrer.delete(0,END)

def modulo():
    global nombre1
    global signe
    signe='%'
    nombre1=float(entrer.get())
    entrer.delete(0,END)

def clear():
    entrer.delete(0,END)

def egal():
    global signe
    nombre2 = float(entrer.get())
    entrer.delete(0,END)

    #Test sur la condition du signe

    if signe == "+":
        entrer.insert(0,nombre1 + nombre2)
    elif signe == "-":
        entrer.insert(0,nombre1 - nombre2)
    elif signe == "*":
        entrer.insert(0,nombre1 * nombre2)
    elif signe == "/":
        if nombre2 == 0:
            entrer.insert(0,"Error")
        else:
            entrer.insert(0,nombre1 / nombre2)
    elif signe== "%":
        entrer.insert(0,nombre1%nombre2)
    elif signe == ' ':
        entrer.insert(0,nombre1)
    else:
        entrer.insert(0,"Signe introuvable")

#Les boutons
b7=Button(s,padx=6,bd=12,bg="white",text="7",width=2,font=("Helvetica",22,'bold'),command=lambda:click(7))
b8=Button(s,padx=6,bd=12,bg="white",text="8",width=2,font=("Helvetica",22,'bold'),command=lambda:click(8))
b9=Button(s,padx=6,bd=12,bg="white",text="9",width=2,font=("Helvetica",22,'bold'),command=lambda:click(9))
b_plus=Button(s,padx=6,bd=12,bg="white",text="+",width=2,font=("Helvetica",22,'bold'),command=plus)
b4=Button(s,padx=6,bd=12,bg="white",text="4",width=2,font=("Helvetica",22,'bold'),command=lambda:click(4))
b5=Button(s,padx=6,bd=12,bg="white",text="5",width=2,font=("Helvetica",22,'bold'),command=lambda:click(5))
b6=Button(s,padx=6,bd=12,bg="white",text="6",width=2,font=("Helvetica",22,'bold'),command=lambda:click(6))
b_moins=Button(s,padx=12,bd=8,bg="white",text="-",width=2,font=("Helvetica",22,'bold'),command=moins)
b1=Button(s,padx=6,bd=12,bg="white",text="1",width=2,font=("Helvetica",22,'bold'),command=lambda:click(1))
b2=Button(s,padx=6,bd=12,bg="white",text="2",width=2,font=("Helvetica",22,'bold'),command=lambda:click(2))
b3=Button(s,padx=6,bd=12,bg="white",text="3",width=2,font=("Helvetica",22,'bold'),command=lambda:click(3))
b_mult=Button(s,padx=6,bd=12,bg="white",text="*",width=2,font=("Helvetica",22,'bold'),command=mult)
b0=Button(s,padx=6,bd=12,bg="white",text="0",width=2,font=("Helvetica",22,'bold'),command=lambda:click(0))
b_virgule=Button(s,padx=6,bd=12,bg="white",text=".",width=2,font=("Helvetica",22,'bold'),command=lambda:click("."))
b_egal=Button(s,padx=6,bd=12,bg="white",text="=",width=6,font=("Helvetica",22,'bold'),command=egal)
b_div=Button(s,padx=6,bd=12,bg="white",text="/",width=2,font=("Helvetica",22,'bold'),command=div)
b_clear=Button(s,padx=6,bd=12,bg="white",text="DEL",width=2,font=("Helvetica",22,'bold'),command=clear)
bfacto=Button(s,padx=6,bd=12,bg="white",text="!",width=2,font=("Helvetica",22,'bold'),command=factoriel)
bmod=Button(s,padx=6,bd=12,bg="white",text="mod",width=2,font=("Helvetica",22,'bold'),command=modulo)
brac=Button(s,padx=6,bd=12,bg="white",text="sqrt",width=2,font=("Helvetica",22,'bold'),command=racine_carrée)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b_clear.grid(row=0,column=4)
b_plus.grid(row=2,column=3)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b_moins.grid(row=2,column=4)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b_mult.grid(row=1,column=3)
b0.grid(row=4,column=0)
b_virgule.grid(row=4,column=1)
b_egal.grid(row=4,column=3,columnspan=4)
b_div.grid(row=1,column=4)
bfacto.grid(row=4,column=2)
bmod.grid(row=3,column=3)
brac.grid(row=3,column=4)



#Programme principale
s.mainloop()

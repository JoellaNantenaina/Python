from tkinter import*
import numpy as np
from numpy.linalg import*

#fenetre
s=Tk()
s.title("Calcule matricielle")

#Fonction
def affichage():
    entrer_liste=entrer.get().split(",")
    ligne=nbLigne.get()
    colonne=nbCol.get()
    liste=[]
    for x in entrer_liste:
        liste.append(int(x))
    A=np.matrix(np.array(liste).reshape((int(ligne),int(colonne))))
    show_list=Label(frame,bg="light blue",font=("Arial",12,"italic"),text="Soit la matrice A :\n\n{}".format(str(A)))
    show_list.grid(row=0,column=1,sticky=(N,S,E,W),padx=5)

    show_det=Label(frame,bg="light blue",font=("Arial",12,"italic"),text="Son déterminant est :\n\n{}".format(str(det(A))))
    show_det.grid(row=1,column=1,sticky=(N,S,E,W),padx=5)

    show_rang=Label(frame,bg="light blue",font=("Arial",12,"italic"),text="Son rang est :\n\n{}".format(str(matrix_rank(A))))
    show_rang.grid(row=2,column=1,sticky=(N,S,E,W),padx=5)

    show_inv=Label(frame,bg="light blue",font=("Arial",12,"italic"),text="L'inverse de la matrice A :\n\n{}".format(str(inv(A))))
    show_inv.grid(row=3,column=1,sticky=(N,S,E,W),padx=5)

    show_val=Label(frame,bg="light blue",font=("Arial",12,"italic"),text="Ses valeurs propres sont :\n\n{}".format(str(eigvals(A))))
    show_val.grid(row=4,column=1,sticky=(N,S,E,W),padx=5)

    entrer.delete(0,END)
    nbLigne.delete(0,END)
    nbCol.delete(0,END)
#Frame,pou mieux organiser la fenetre    
    
conteneur = Frame(s,width=9)
conteneur.grid(row=10,column=0,sticky=(N,S,E,W))

#SOus frame
frame = LabelFrame(conteneur,borderwidth=5,bg="light blue",width=600,height=350,fg="Steel Blue",text='Résultat',font=("Helvetica",18,"bold"))
frame.grid(row=10,column=0,rowspan=8,columnspan=5,sticky=(N,S,E,W))

#Formulaire de saisie
msg=Label(conteneur,width=25,text="Entrer une liste de nombres :",fg="Steel Blue",font=("Helvetica",12,"bold"))
msg.grid(row=0,column=0,columnspan=2)

entrer=Entry(conteneur,width=28,font=("Helvetica",14,"bold"),fg="white",bg="gray",borderwidth=5)
entrer.grid(row=0,column=2,columnspan=2)

espace=Label(conteneur,width=2)
espace.grid(row=1,column=0,columnspan=5)

msg1=Label(conteneur,width=25,text="Nombre de ligne(s):",font=("Helvetica",12,"bold"))
msg1.grid(row=3,column=0,columnspan=2)

nbLigne=Spinbox(conteneur,width=5,from_=1, to=10,font=("Helvetica",14,"bold"),fg="white",bg="gray")
nbLigne.grid(row=3,column=2)

msg2=Label(conteneur,width=25,text="Nombre de colonne(s):",font=("Helvetica",12,"bold"))
msg2.grid(row=5,column=0,columnspan=2)

nbCol=Spinbox(conteneur,width=5,from_=1, to=10,font=("Helvetica",14,"bold"),fg="white",bg="gray")
nbCol.grid(row=5,column=2)

espace2=Label(conteneur,width=2)
espace2.grid(row=6,column=0,columnspan=5)

#Boutton submit
bouton=Button(conteneur,width=15,text="Submit",font=("Helvetica",16,"bold"),bg="light blue",fg="white",command=affichage)
bouton.grid(row=7,column=1,columnspan=4)

espace3=Label(conteneur,width=2)
espace3.grid(row=8,column=0,columnspan=5)


#Programme Principale
s.mainloop()

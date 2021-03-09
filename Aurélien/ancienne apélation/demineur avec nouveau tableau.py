from turtle import *
from random import *
import time


setup(800,800)

tt_g = Turtle()            #Turtle grille
tt_g.penup()
tt_g.speed("fastest")
list_case= []
ligne_list= []
collone_list= []


def grille():                           #définition de la grille de départ
    global bombe_case
    global nb_collone
    global nb_ligne
    nb_collone = int(textinput("Nombre de collone", "Veuillez saisir le nombre de collone désiré:")) 
    nb_ligne = int(textinput("Nombre de ligne", "Veuillez saisir le nombre de ligne désiré:"))
    #nb_collone = int(input("Veuillez saisir le nombre de collone désiré:"))     #Pour version Python 3.0
    #nb_ligne = int(input("Veuillez saisir le nombre de ligne désiré:"))         #   //
    tt_g.goto(-10*nb_collone,10*nb_ligne)             #Fait le contour du carré génerale et le colorie en gris
    tt_g.pendown()
    tt_g.fillcolor("gray")
    tt_g.begin_fill()
    for i in range(2):
        tt_g.forward((10*nb_collone)*2)         
        tt_g.right(90)
        tt_g.forward((10*nb_ligne)*2)
        tt_g.right(90)
    tt_g.end_fill()
    
    n=20
    for i in range(nb_ligne):                           #dessine chaque ligne
        tt_g.penup()
        tt_g.goto((-10*nb_collone),(10*nb_ligne)-n) 
        tt_g.pendown()
        tt_g.forward((10*nb_collone)*2)
        n= n+20 
    
    tt_g.penup()
    tt_g.goto(-10*nb_collone,10*nb_ligne)
    tt_g.pendown()
    tt_g.right(90)
    n=20
    for i in range(nb_collone):                           #dessine chaque collone
        tt_g.penup()
        tt_g.goto((-10*nb_collone)+n,(10*nb_ligne)) 
        tt_g.pendown()
        tt_g.forward((10*nb_ligne)*2)
        n= n+20 
    tt_g.left(90)
    tt_g.penup()
    
    bombe_case= []
    for i in range((nb_ligne*nb_collone)//5):        #def bombe sur des cases aléatoirement
        bombe_aléatoire= randint(0, nb_collone*nb_ligne)
        while bombe_aléatoire in bombe_case:   #évite de poser plusieurs bombe sur la même case
            bombe_aléatoire= randint(1, nb_collone*nb_ligne)
        bombe_case.append(bombe_aléatoire)
            
    bombe_case.sort()
    print("nb bombe=",len(bombe_case))
    print("bombe_cas=",bombe_case)



def revel_case():                   #colorie la case sans bombe en blanc
    tt_g.fillcolor("white")
    tt_g.goto((-10*nb_collone)+n,(10*nb_ligne)-c)
    tt_g.pendown()
    tt_g.begin_fill()
    for i in range(4):
        tt_g.forward(20)
        tt_g.right(90)
    tt_g.end_fill()
    tt_g.penup()






nombre_bombe_autour= []
def ecriture_nombre():                      #variable pour écrire le nombre de bombe autour de la case séléctionner

    if collone_list[i-1]+ligne_list[k-1] in bombe_case:
        nombre_bombe_autour.append(1)
    if collone_list[i]+ligne_list[k-1] in bombe_case:
        nombre_bombe_autour.append(1)
    if collone_list[i+1]+ligne_list[k-1] in bombe_case:
        nombre_bombe_autour.append(1)
    if collone_list[i-1]+ligne_list[k] in bombe_case:
        nombre_bombe_autour.append(1)
    if collone_list[i+1]+ligne_list[k] in bombe_case:
        nombre_bombe_autour.append(1)
    if collone_list[i-1]+ligne_list[k+1] in bombe_case:
        nombre_bombe_autour.append(1)
    if collone_list[i-1]+ligne_list[k+1] in bombe_case:
        nombre_bombe_autour.append(1)
    if collone_list[i+1]+ligne_list[k+1] in bombe_case:
        nombre_bombe_autour.append(1)


    nb_bombe_aut=nombre_bombe_autour.count(1)       #compte le nombre de bombe autour
    tt_g.goto((-10*nb_collone)+n+5,(10*nb_ligne)-c-23)
    tt_g.pendown()
    if nb_bombe_aut ==1:         #Si il y a au minimum une bombe écrire le nombre en couleurs sinon : case vide
        tt_g.color("blue")
        tt_g.write("1", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==2:
        tt_g.color("green")
        tt_g.write("2", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==3:
        tt_g.color("red")
        tt_g.write("3", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==4:
        tt_g.color("purple")
        tt_g.write("4", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==5:
        tt_g.color("brown")
        tt_g.write("5", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==6:
        tt_g.color("orange")
        tt_g.write("6", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==7:
        tt_g.color("pink")
        tt_g.write("7", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==8:
        tt_g.color("black")
        tt_g.write("8", font=("Arial", 15, "normal"))
    tt_g.color("black")
    nombre_bombe_autour[:]= []
    tt_g.penup()
    
    
'''
def position(x,y):                                           #entre la case cliquer des une liste
    global n
    global c
    global variable_temp
    n=0   # pour les cases en ligne
    a=0
    c=0   # pour faire pour faire les autres ligne de chaque colonne
    for k in range(25):
        for i in range(25):
            if -250+n<x<-230+n and 230+c<y<250+c and i+1+a not in list_case:
                list_case.append(i+1+a) #list_case est la liste qui nous dit les case déjà cliquer
                variable_temp= i+1+a
                if i+1+a in bombe_case:
                    print("perdu")
                else:
                    revel_case()
                    ecriture_nombre()
            n=n+20
        a=a+25
        c=c-20
        n=0
   # print(list_case)
   # print("x=",x,"y=",y)

'''

def tableau():               #création tableau
    n=0   
    for i in range(nb_collone+1):
        collone_list.append(n)
        n=n+1
    print(collone_list)
    n=0
    for i in range(nb_ligne+1):
        ligne_list.append(n)
        n=n+nb_collone
    print(ligne_list)

def position(x,y):                   #entre la case cliquer des une liste
    global i
    global k
    global n
    global c
    n=0  
    c=0 
    Etat= "Neutre"
    for k in range(nb_ligne):
        for i in range(nb_collone):
            if (-10*nb_collone)+n <x< (-10*nb_collone+20)+n and (10*nb_ligne-20)-c<y<(10*nb_ligne)-c and collone_list[i]+ligne_list[k] not in list_case:
                list_case.append(collone_list[i]+ligne_list[k])
                print(collone_list[i]+ligne_list[k])
                if collone_list[i]+ligne_list[k] in bombe_case:
                    print("perdu")
                    Etat="Perdu"
                else:
                    iv =i
                    kv= k
                    
                    revel_case()
                    ecriture_nombre()
            n=n+20
        c=c+20
        n=0
    list_case.sort()
    print(list_case)
    print("x=",x,"y=",y)


grille()
tableau()

onscreenclick(position)
#onclick(None)
mainloop()
    
    
    
    





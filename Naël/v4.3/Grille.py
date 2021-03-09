from turtle import *
from random import *
import Menu


tt_g = Turtle()            #Turtle grille
tt_g.hideturtle()
tt_g.penup()
tt_g.speed("fastest")



def grille():                           #définition de la grille de départ
    global bombe_case
    global oscMenu
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

    tt_g.goto(100,370)
    Menu.rectangleG()
    tt_g.forward(30)
    tt_g.right(90)
    tt_g.forward(42)
    tt_g.left(90)
    tt_g.write("PAUSE", font=("Arial", 20, "normal"))
    tt_g.goto(-100,370)
    Menu.rectangleG()
    tt_g.goto(-300,370)
    Menu.rectangleG()
    tt_g.forward(75)
    tt_g.right(90)
    tt_g.pendown()
    tt_g.forward(50)
    tt_g.penup()
    tt_g.left(90)
    tt_g.goto(-215,350)
    drapeau_case()
    


    bombe_case= []
    for i in range((nb_ligne*nb_collone)//5):        #def bombe sur des cases aléatoirement
        bombe_aléatoire= randint(0, nb_collone*nb_ligne-1)
        while bombe_aléatoire in bombe_case:   #évite de poser plusieurs bombe sur la même case
            bombe_aléatoire= randint(1, nb_collone*nb_ligne)
        bombe_case.append(bombe_aléatoire)

    bombe_case.sort()
    print("nb bombe=",len(bombe_case))
    print("bombe_case=",bombe_case)

    tableau()

def tableau():               #création tableau
    n=0
    for i in range(nb_collone+1):
        collone_list.append(n)
        n=n+1
    #print(collone_list)
    n=0
    for i in range(nb_ligne+1):
        ligne_list.append(n)
        n=n+nb_collone
    #/print(ligne_list)
    
def drapeau_case():
    tt_g.forward(10)
    tt_g.left(45)
    tt_g.pendown()
    tt_g.forward(20)
    tt_g.right(45+90)
    tt_g.forward(40)
    tt_g.left(90)
    tt_g.forward(20)
    tt_g.right(180)
    tt_g.forward(40)
    tt_g.backward(20)
    tt_g.right(90)
    tt_g.forward(25)
    tt_g.left(90)
    tt_g.forward(15)
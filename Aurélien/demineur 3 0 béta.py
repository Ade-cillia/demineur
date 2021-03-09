from turtle import *
from random import *
import time


setup(800,800)

tt_g = Turtle()            #Turtle grille
tt_g.penup()
tt_g.speed("fastest")
list_case= []



def grille():                           #définition de la grille de départ
    nb_collone = int(textinput("Nombre de collone", "Veuillez saisir le nombre de collone désiré:")) 
    nb_ligne = int(textinput("Nombre de ligne", "Veuillez saisir le nombre de ligne désiré:"))
    tt_g.goto(-10*nb_collone,10*nb_ligne)             #Fait le contour du carré génerale et le colorie en gris
    tt_g.pendown()
    tt_g.fillcolor("gray")
    tt_g.begin_fill()
    for i in range(4):
        tt_g.forward((10*nb_collone)*2)         
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
        tt_g.forward((10*nb_collone)*2)
        n= n+20 
    
    
    
    
    
    
    
grille()




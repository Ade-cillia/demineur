from turtle import *
from random import *
import time


setup(800,800)

tt_g = Turtle()            #Turtle grille
tt_g.penup()
tt_g.speed("fastest")
list_case= []

def grille():                           #définition de la grille de départ
    tt_g.goto(-250,250)
    tt_g.pendown()
    tt_g.fillcolor("gray")
    tt_g.begin_fill()
    for i in range(4):
        tt_g.forward(500)
        tt_g.right(90)
    tt_g.end_fill()
    n=0
    for i in range(26):
        tt_g.goto(-250,250-n)
        tt_g.pendown()
        tt_g.forward(500)
        n=n+20
        tt_g.penup()
    tt_g.left(90)
    n=0
    for i in range(26):
        tt_g.goto(250-n,-250)
        tt_g.pendown()
        tt_g.forward(500)
        n=n+20
        tt_g.penup()
    tt_g.right(90)

grille()

bombe_case= []
for i in range(200):        #def bombe
    bombe_aléatoire= randint(1, 625)
    if bombe_aléatoire not in bombe_case:
        bombe_case.append(bombe_aléatoire)
bombe_case.sort()
print(bombe_case)


def revel_case():                   #colorie la case sans bombe en blanc
    tt_g.fillcolor("white")
    tt_g.goto(-250+n,250+c)
    tt_g.pendown()
    tt_g.begin_fill()
    for i in range(4):
        tt_g.forward(20)
        tt_g.right(90)
    tt_g.end_fill()
    tt_g.penup()






nombre_bombe_autour= []
def ecriture_nombre():
    if variable_temp-26 in bombe_case:
        nombre_bombe_autour.append(1)
    if variable_temp-25 in bombe_case:
        nombre_bombe_autour.append(1)
    if variable_temp-24 in bombe_case:
        nombre_bombe_autour.append(1)
    if variable_temp-1 in bombe_case:
        nombre_bombe_autour.append(1)
    if variable_temp+1 in bombe_case:
        nombre_bombe_autour.append(1)
    if variable_temp+24 in bombe_case:
        nombre_bombe_autour.append(1)
    if variable_temp+25 in bombe_case:
        nombre_bombe_autour.append(1)
    if variable_temp+26 in bombe_case:
        nombre_bombe_autour.append(1)


    nb_bombe_aut=nombre_bombe_autour.count(1)
    tt_g.goto(-250+n+5,250+c-23)
    tt_g.pendown()
    if nb_bombe_aut >0:
        tt_g.write(nb_bombe_aut, font=("Arial", 15, "normal"))
    nombre_bombe_autour[:]= []
    tt_g.penup()





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
                list_case.append(i+1+a)
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
    print(list_case)
    print("x=",x,"y=",y)
















onscreenclick(position)
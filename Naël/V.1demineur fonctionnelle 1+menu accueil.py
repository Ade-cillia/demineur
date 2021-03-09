from turtle import *
from random import *
import time


setup(800,800)

tt_g = Turtle()            #Turtle grille
tt_g.hideturtle()
tt_g.penup()
tt_g.speed("fastest")
list_case= []
tt_m = Turtle()             #Turtle menu
tt_m.hideturtle()
tt_m.speed("fastest")


def menu():

    tt_m.penup()
    tt_m.goto(-150,350)
    tt_m.pendown()
    tt_m.write("DEMINEUR", font=("Arial", 30, "normal"))
    tt_m.penup()
   
    tt_m.goto(-130,250)
    rectangle()
    tt_m.forward(30)
    tt_m.right(90)
    tt_m.forward(42)
    tt_m.left(90)
    tt_m.write("JOUER", font=("Arial", 20, "normal"))
    
    tt_m.goto(-130, 150)
    rectangle()
    tt_m.forward(10)
    tt_m.right(90)
    tt_m.forward(42)
    tt_m.left(90)
    tt_m.write("TUTORIEL", font=("Arial", 20, "normal"))
    
    tt_m.goto(-130,50)
    rectangle()
    tt_m.forward(25)
    tt_m.right(90)
    tt_m.forward(42)
    tt_m.left(90)
    tt_m.write("OPTION", font=("Arial", 20, "normal"))
    
    tt_m.goto(-130,-50)
    rectangle()
    tt_m.forward(20)
    tt_m.right(90)
    tt_m.forward(42)
    tt_m.left(90)
    tt_m.write("SUCCES", font=("Arial", 20, "normal"))
    
    onscreenclick(click_menu)


def rectangle():
    hauteur = 150
    longueur = 50
    tt_m.pendown()
    tt_m.forward(hauteur)
    tt_m.right(90)
    tt_m.forward(longueur)
    tt_m.right(90)
    tt_m.forward(hauteur)
    tt_m.right(90)
    tt_m.forward(longueur)
    tt_m.right(90)
    tt_m.penup()


def click_menu(x,y):
    if -130<x<-20 and 200<y<250:
        tt_m.clear()
        grille()
        
        
    








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



bombe_case= []
for i in range(200):        #def bombe sur des cases aléatoirement
    bombe_aléatoire= randint(1, 625)
    if bombe_aléatoire not in bombe_case:   #évite de poser plusieurs bombe sur la même case
        bombe_case.append(bombe_aléatoire)
bombe_case.sort()
#print(bombe_case)
onscreenclick(position)


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
def ecriture_nombre():                      #variable pour écrire le nombre de bombe autour de la case séléctionner
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

    nb_bombe_aut=nombre_bombe_autour.count(1)       #compte le nombre de bombe autour
    tt_g.goto(-250+n+5,250+c-23)
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




menu()



#onscreenclick(position)
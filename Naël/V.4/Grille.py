from turtle import *
from random import *
from Menu import *
import time
from Test_click import *


setup(800,800)
title("demineur")

tt_g = Turtle()            #Turtle grille
tt_g.hideturtle()
tt_g.penup()
tt_g.speed("fastest")
list_case= []
ligne_list= []
collone_list= []
tt_m = Turtle()             ###NAËLV.1
#tt_m.st()
tt_m.hideturtle()           ###NAËL V.1
tt_m.speed("fastest")      ###NAËLV.1
#global oscMenu = 1
global nb_collone
global nb_ligne

'''
mixer.init()
mixer.music.load("music1.wav")
mixer.music.set_volume(0.05)
mixer.music.play(-1)

def music():
    global music
    global music_jouer
    music_jouer = None
    music= ["music_noragami.ogg"]
    music_suivant = choice(music)
    while music_suivant == music_jouer:
        music_suivant = choice(music)
    music_jouer = music_suivant
    mixer.music.load(music_suivant)
    mixer.music.set_volume(0.05)
    mixer.music.play()


#music()

'''

def rectangleG():                                                                ###Bouton inGame (RectangleGame)
    hauteur = 50
    longueur = 150
    tt_g.pendown()
    tt_g.forward(longueur)
    tt_g.right(90)
    tt_g.forward(hauteur)
    tt_g.right(90)
    tt_g.forward(longueur)
    tt_g.right(90)
    tt_g.forward(hauteur)
    tt_g.right(90)
    tt_g.penup()


    



    


def grille():                           #définition de la grille de départ
    global bombe_case
    global oscMenu
    global bombe_case
    global nb_collone
    global nb_ligne
    tt_m.clear()
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
    rectangleG()
    tt_g.forward(30)
    tt_g.right(90)
    tt_g.forward(42)
    tt_g.left(90)
    tt_g.write("PAUSE", font=("Arial", 20, "normal"))
    tt_g.goto(-100,370)
    rectangleG()
    tt_g.goto(-300,370)
    rectangleG()
    tt_g.forward(75)
    tt_g.right(90)
    tt_g.pendown()
    tt_g.forward(50)
    tt_g.penup()
    tt_g.left(90)


    bombe_case= []
    for i in range((nb_ligne*nb_collone)//10):        #def bombe sur des cases aléatoirement (le dernier chiffres et 1/(concentration de bombes)
        bombe_aléatoire= randint(0, nb_collone*nb_ligne-1)
        while bombe_aléatoire in bombe_case:   #évite de poser plusieurs bombe sur la même case
            bombe_aléatoire= randint(1, nb_collone*nb_ligne)
        bombe_case.append(bombe_aléatoire)
            
    bombe_case.sort()
    print("nb bombe=",len(bombe_case))
    print("bombe_case=",bombe_case)
    tableau()
    oscMenu = 0
    print(oscMenu)
    if oscMenu == 0:
        onscreenclick(position)



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


def revel_bombe():
    tt_g.color("red")
    tt_g.goto((-10*nb_collone)+n,(10*nb_ligne)-c)
    tt_g.pendown()
    for i in range(4):
        tt_g.forward(20)
        tt_g.right(90)
    tt_g.penup()
    tt_g.goto(-400,-400)
    #tt_g.write("☠", font=("Arial", 600, "normal"))
    tt_g.goto((-10*nb_collone)+n-2,(10*nb_ligne)-c-26+1/2)

    tt_g.write("✹", font=("Arial", 20, "normal"))
    tt_g.color("black")

nombre_bombe_autour= []



def ecriture_nombre():                      #variable pour écrire le nombre de bombe autour de la case séléctionner

    if collone_list[i]==0 and ligne_list[k]==0:                  #angle gauche
        if collone_list[i+1]+ligne_list[k] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
        print(collone_list[i])
        print(ligne_list[k])
        
    if collone_list[-2]>collone_list[i]>0 and ligne_list[k]==0:  #ligne du haut
        if collone_list[i-1]+ligne_list[k] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i-1]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
            
    if collone_list[i]==nb_collone and ligne_list[k]==0: #angle haut droit
        if collone_list[i-1]+ligne_list[k] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i-1]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
            
    if collone_list[i]==0 and ligne_list[-2]>ligne_list[k]>0:    #ligne gauche
        if collone_list[i]+ligne_list[k-1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k-1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
            
    if collone_list[i]==collone_list[-2] and ligne_list[-2]>ligne_list[k]>0: #ligne droite
        if collone_list[i-1]+ligne_list[k-1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i]+ligne_list[k-1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i-1]+ligne_list[k] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i-1]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
            
    if collone_list[i]==0 and ligne_list[k]==ligne_list[-2]: #angle bas gauche
        if collone_list[i]+ligne_list[k-1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k-1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k] in bombe_case:
            nombre_bombe_autour.append(1)
    
    if collone_list[-2]>collone_list[i]>0 and ligne_list[k]==ligne_list[-2]: #ligne bas
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
            
    if collone_list[i]==collone_list[-2] and ligne_list[k]==ligne_list[-2]: #angle bas droite
        if collone_list[i-1]+ligne_list[k-1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i]+ligne_list[k-1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i-1]+ligne_list[k] in bombe_case:
            nombre_bombe_autour.append(1)
            
    if collone_list[-2]>collone_list[i]>0  and  ligne_list[-2]>ligne_list[k]>0:   #case non contre un bord
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
        if collone_list[i]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)
        if collone_list[i+1]+ligne_list[k+1] in bombe_case:
            nombre_bombe_autour.append(1)

   
    '''                        #test:
    print(ligne_list[-2])
    print(collone_list[-2])
    print(collone_list[i])
    print(ligne_list[k])
    print(nombre_bombe_autour)
    '''
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
    







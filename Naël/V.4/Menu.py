from turtle import *
from random import *
import Grille
import time
from Test_click import*


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
global oscMenu
oscMenu = 1
global nb_collone
global nb_ligne



def menu():                                                  ###NAËLV.1
    global oscMenu
    
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
    
    



def rectangle():                                                                ###NAËLV.1
    hauteur = 50
    longueur = 150
    tt_m.pendown()
    tt_m.forward(longueur)
    tt_m.right(90)
    tt_m.forward(hauteur)
    tt_m.right(90)
    tt_m.forward(longueur)
    tt_m.right(90)
    tt_m.forward(hauteur)
    tt_m.right(90)
    tt_m.penup()
    


        


def page_succes():
    tt_m.penup()
    tt_m.goto(-150,350)
    tt_m.pendown()
    tt_m.write("SUCCES", font=("Arial", 30, "normal"))
    tt_m.penup()
from turtle import *
import Grille
import Test_click
import Revelation_case
import Timer

tt_m = Turtle()   #Turtle menu
#tt_m.st()
tt_m.hideturtle()
tt_m.speed("fastest")  


def menu():                                                  
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
    
    


def rectangle():                                                               
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

def rectangleG():                                                               
    hauteur = 50
    longueur = 150
    Grille.tt_g.pendown()
    Grille.tt_g.forward(longueur)
    Grille.tt_g.right(90)
    Grille.tt_g.forward(hauteur)
    Grille.tt_g.right(90)
    Grille.tt_g.forward(longueur)
    Grille.tt_g.right(90)
    Grille.tt_g.forward(hauteur)
    Grille.tt_g.right(90)
    Grille.tt_g.penup()


def click_menu(x,y):                                    
    global oscMenu
    
    if -130<x<20 and 200<y<250 and oscMenu == 1:
        oscMenu = 0
        tt_m.clear()
        Grille.grille()
        Timer.temps()
    if oscMenu == 0:
        onscreenclick(Test_click.position)
    if -130<x<20 and -100<y<-50 and oscMenu == 1:
        oscMenu = 0
        tt_m.clear()
        page_succes()
        
    


def page_succes():
    tt_m.penup()
    tt_m.goto(-150,350)
    tt_m.pendown()
    tt_m.write("SUCCES", font=("Arial", 30, "normal"))
    tt_m.penup()
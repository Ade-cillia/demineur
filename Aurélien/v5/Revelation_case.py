from turtle import *
import Grille
import Menu
import Test_click

tt_rev = Turtle()            #Turtle révélation
tt_rev.hideturtle()
tt_rev.penup()
tt_rev.speed("fastest")




def revel_case():                   #colorie la case sans bombe en blanc
    tt_rev.fillcolor("white")
    tt_rev.goto((-10*Grille.nb_collone)+Test_click.n,(10*Grille.nb_ligne)-Test_click.c)
    tt_rev.pendown()
    tt_rev.begin_fill()
    for i in range(4):
        tt_rev.forward(20)
        tt_rev.right(90)
    tt_rev.end_fill()
    tt_rev.penup()

def revel_bombe():
    tt_rev.color("red")
    tt_rev.goto((-10*Grille.nb_collone)+Test_click.n,(10*Grille.nb_ligne)-Test_click.c)
    tt_rev.pendown()
    for i in range(4):
        tt_rev.forward(20)
        tt_rev.right(90)
    tt_rev.penup()
    tt_rev.goto(-400,-400)
    #tt_g.write("☠", font=("Arial", 600, "normal"))
    tt_rev.goto((-10*Grille.nb_collone)+Test_click.n-2,(10*Grille.nb_ligne)-Test_click.c-26+1/2)

    tt_rev.write("✹", font=("Arial", 20, "normal"))
    tt_rev.color("black")

#bombe symobole: ✹ , 💣 ,
#🏴‍

def revel_toute_case_blanche():
    Test_click.temp_n=0
    Test_click.fonction_revel = 1
    while True:
        Test_click.ecriture_nombre()
        Test_click.temp_n = Test_click.temp_n + 1
    Test_click.fonction_revel = 0
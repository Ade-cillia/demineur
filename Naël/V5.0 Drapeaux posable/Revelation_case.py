from turtle import *
import Grille
import Menu
import Test_click
global n
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

def place_drapeau(x,y):  #dessiner le drapeau au centre de la case
    global i
    global k
    global n
    global c
    global Etat
    n=0
    c=0
    Etat= "Neutre"
    for k in range(Grille.nb_ligne):
        for i in range(Grille.nb_collone):
            if (-10*Grille.nb_collone)+n <x< (-10*Grille.nb_collone+20)+n and (10*Grille.nb_ligne-20)-c<y<(10*Grille.nb_ligne)-c and Grille.collone_list[i]+Grille.ligne_list[k] not in Grille.list_case and (Grille.collone_list[i]+Grille.ligne_list[k]) not in liste_drapeau and len(Grille.bombe_case)-len(liste_drapeau) > 0:   #identifie la case cliqué
                
                liste_drapeau.append(Grille.collone_list[i]+Grille.ligne_list[k])
                tt_rev.goto(((-10*Grille.nb_collone)+n)+10,((10*Grille.nb_ligne-20)-c)+10) #va au centre de cette case
                tt_rev.pendown()
                tt_rev.left(90)
                tt_rev.forward(8)
                tt_rev.left(45+90)
                tt_rev.fillcolor("red")
                tt_rev.begin_fill()
                tt_rev.forward(9)
                tt_rev.left(45+90)
                tt_rev.forward(6)
                tt_rev.end_fill()
                tt_rev.right(90)
                tt_rev.goto(((-10*Grille.nb_collone)+n)+10,((10*Grille.nb_ligne-20)-c)+10)
                tt_rev.forward(8)
                tt_rev.left(90)
                tt_rev.forward(6)
                tt_rev.backward(13)
                tt_rev.penup()
                
            
            
            elif ((-10*Grille.nb_collone)+n <x< (-10*Grille.nb_collone+20)+n and (10*Grille.nb_ligne-20)-c<y<(10*Grille.nb_ligne)-c and Grille.collone_list[i]+Grille.ligne_list[k] not in Grille.list_case and (Grille.collone_list[i]+Grille.ligne_list[k])) in liste_drapeau and len(Grille.bombe_case)-len(liste_drapeau) > 0:
                
                liste_drapeau.remove(Grille.collone_list[i]+Grille.ligne_list[k])
                tt_rev.goto(((-10*Grille.nb_collone)+n)+10,((10*Grille.nb_ligne-20)-c)+10)
                tt_rev.forward(10)
                tt_rev.fillcolor("gray")
                tt_rev.begin_fill()
                tt_rev.left(90)
                tt_rev.forward(9)
                tt_rev.left(90)
                tt_rev.forward(18)
                tt_rev.left(90)
                tt_rev.forward(18)
                tt_rev.left(90)
                tt_rev.forward(18)
                tt_rev.left(90)
                tt_rev.forward(18)
                tt_rev.end_fill()
                tt_rev.right(90)
            
            
           

            
            
            
            
            n=n+20
        c=c+20
        n=0
    #actualiser le nombre de drapeau
    #Grille.tt_g.showturtle()
    Grille.tt_g.fillcolor("white")
    Grille.tt_g.begin_fill()
    Grille.tt_g.goto(-300,370)
    Menu.demirectangleG()
    Grille.tt_g.end_fill()
    Grille.tt_g.right(90)
    Grille.tt_g.forward(40)
    Grille.tt_g.left(90)
    Grille.tt_g.forward(25)
    Grille.tt_g.write(len(Grille.bombe_case)-len(liste_drapeau), font=("Arial", 20, "normal"))

        

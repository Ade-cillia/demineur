from turtle import *
from random import *
from Menu import *
import time
from Grille import *

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




def click_menu(x,y):                                    ###NAËLV.1
    global oscMenu
    
    if -130<x<20 and 200<y<250 and oscMenu == 1: #click Jouer
        oscMenu = 0
        tt_m.clear()
        Grille.grille()
    if -130<x<20 and -100<y<-50 and oscMenu == 1: #click Succes
        oscMenu = 0
        tt_m.clear()
        page_succes()
        
        
        



def position(x,y,):                   #entre la case cliquer des une liste
    global i
    global k
    global n
    global c
    global Etat
    global nb_collone
    global nb_ligne
    n=0  
    c=0 
    Etat= "Neutre"
    for k in range(nb_ligne):
        for i in range(nb_collone):
            if (-10*nb_collone)+n <x< (-10*nb_collone+20)+n and (10*nb_ligne-20)-c<y<(10*nb_ligne)-c and collone_list[i]+ligne_list[k] not in list_case:
                list_case.append(collone_list[i]+ligne_list[k])
                #print(collone_list[i]+ligne_list[k])
                if collone_list[i]+ligne_list[k] in bombe_case:
                    print("perdu")
                    Etat="Perdu"
                    revel_case()
                    revel_bombe()
                else:
                    revel_case()
                    ecriture_nombre()
            n=n+20
        c=c+20
        n=0
    list_case.sort()
    #print(list_case)
    #print("x=",x,"y=",y)
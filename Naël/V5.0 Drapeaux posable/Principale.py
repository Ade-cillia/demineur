from turtle import *
import time
import Menu
import Music
import Grille
import Test_click
import Revelation_case

#---------------------GLOBAL--------------------------------

global list_case
global ligne_list
global collone_list
global nombre_bombe_autour
global oscMenu
#-----------------INITIALISATION----------------------------

setup(800,800)
title("demineur")


Grille.list_case= []
Grille.ligne_list= []
Grille.collone_list= []
Grille.bombe_case= []
Test_click.nombre_bombe_autour= []
Revelation_case.liste_drapeau=[]
Menu.oscMenu = 1





#--------------------PROGRAMME-------------------------------



Menu.menu()
if Menu.oscMenu == 1:
    onscreenclick(Menu.click_menu)





mainloop()
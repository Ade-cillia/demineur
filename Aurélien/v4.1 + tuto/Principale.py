from turtle import *
import time
import Menu
import Music
import Grille
import Test_click
import Revelation_case
import Tutoriel

#---------------------GLOBAL--------------------------------

global list_case
global ligne_list
global collone_list
global nombre_bombe_autour
global oscMenu
global start_tuto
#-----------------INITIALISATION----------------------------

setup(800,800)
title("demineur")


Grille.list_case= []
Grille.ligne_list= []
Grille.collone_list= []
Test_click.nombre_bombe_autour= []
Menu.oscMenu = 1






#--------------------PROGRAMME-------------------------------



Menu.menu()
if Menu.oscMenu == 1:
    onscreenclick(Menu.click_menu)




mainloop()
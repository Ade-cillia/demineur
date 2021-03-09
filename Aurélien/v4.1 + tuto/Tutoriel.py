from turtle import *
import Menu



tt_tuto = Turtle()   #Turtle tutoriel
#tt_m.st()
tt_tuto.hideturtle()
tt_tuto.speed("fastest")  
tt_tuto.penup()



def tuto():
    tt_tuto.clear()
    
    tt_tuto.goto(-150,350)
    tt_tuto.pendown()
    tt_tuto.write("Tutoriel", font=("Arial", 30, "normal"))
    tt_tuto.penup()
    
    tt_tuto.goto(-250,150)
    tt_tuto.pendown()
    tt_tuto.write("Le but du démineur est plus simple qu'il n'y parait.", font=("Arial", 15, "normal"))
    tt_tuto.penup()
    
    tt_tuto.goto(-250,120)
    tt_tuto.pendown()
    tt_tuto.write("Il suffit de révéler toutes les cases en faisant un clique gauche dessus,", font=("Arial", 15, "normal"))
    tt_tuto.penup()
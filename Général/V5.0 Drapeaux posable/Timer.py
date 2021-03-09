from turtle import *

tim_g = Turtle()#Turtle de calcul du temps
tim_g.ht()
tim_g.penup()
tim_g.color("red")
tim_g.speed("slowest")
tps_g = Turtle()#Turtle d'écriture du temps
tps_g.ht()
tps_g.color("red")
tps_g.speed("fastest")



global secondes
global minutes
minutes = 0
secondes = 0
b=303.3367037411527



def temps():
    tps_g.penup()
    tps_g.goto(-17,325)
    tps_g.pendown()
    global secondes
    global minutes
    while True:
        tim_g.forward(b)
        secondes=secondes+1
        if secondes == 60:
            secondes = 0
            minutes = minutes +1
        tps_g.clear()
        tps_g.write(str(minutes).zfill(2) + ":" + str(secondes).zfill(2) , False,"center", ("ComicSans",25,"normal"))
        tim_g.backward(b)
        secondes=secondes+1
        if secondes == 60:
            secondes = 0
            minutes = minutes +1
        tps_g.clear()
        tps_g.write(str(minutes).zfill(2) + ":" + str(secondes).zfill(2) , False,"center", ("ComicSans",25,"normal"))
        
        

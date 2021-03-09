from turtle import *
import Grille
import Menu
import Revelation_case

def position(x,y):                   #entre la case cliquer des une liste
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
            if (-10*Grille.nb_collone)+n <x< (-10*Grille.nb_collone+20)+n and (10*Grille.nb_ligne-20)-c<y<(10*Grille.nb_ligne)-c and Grille.collone_list[i]+Grille.ligne_list[k] not in Grille.list_case:
                Grille.list_case.append(Grille.collone_list[i]+Grille.ligne_list[k])
                #print(collone_list[i]+ligne_list[k])
                if Grille.collone_list[i]+Grille.ligne_list[k] in Grille.bombe_case:
                    print("perdu")
                    Etat="Perdu"
                    Revelation_case.revel_case()
                    Revelation_case.revel_bombe()
                else:
                    Revelation_case.revel_case()
                    ecriture_nombre()
            n=n+20
        c=c+20
        n=0
    Grille.list_case.sort()
    #print(list_case)
    #print("x=",x,"y=",y)





def ecriture_nombre():                      #variable pour écrire le nombre de bombe autour de la case séléctionner

    if Grille.collone_list[i]==0 and Grille.ligne_list[k]==0:                  #angle gauche
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)

    if Grille.collone_list[-2]>Grille.collone_list[i]>0 and Grille.ligne_list[k]==0:  #ligne du haut
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)

    if Grille.collone_list[i]==Grille.nb_collone and Grille.ligne_list[k]==0: #angle haut droit
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)

    if Grille.collone_list[i]==0 and Grille.ligne_list[-2]>Grille.ligne_list[k]>0:    #ligne gauche
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k-1] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)

    if Grille.collone_list[i]==Grille.collone_list[-2] and Grille.ligne_list[-2]>Grille.ligne_list[k]>0: #ligne droite
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i]+Grille.ligne_list[k+1] in Grille.bombe_case:
            nombre_bombe_autour.append(1)

    if Grille.collone_list[i]==0 and Grille.ligne_list[k]==Grille.ligne_list[-2]: #angle bas gauche
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)

    if Grille.collone_list[-2]>Grille.collone_list[i]>0 and Grille.ligne_list[k]==Grille.ligne_list[-2]: #ligne bas
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)

    if Grille.collone_list[i]==Grille.collone_list[-2] and Grille.ligne_list[k]==Grille.ligne_list[-2]: #angle bas droite
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)

    if Grille.collone_list[-2]>Grille.collone_list[i]>0  and  Grille.ligne_list[-2]>Grille.ligne_list[k]>0:   #case non contre un bord
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-1] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-1-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)
        if Grille.collone_list[i+1-temp_n]+Grille.ligne_list[k+1-temp_n] in Grille.bombe_case:
            nombre_bombe_autour.append(1)


    '''                        #test:
    print(Grille.ligne_list[-2])
    print(Grille.collone_list[-2])
    print(Grille.collone_list[i])
    print(Grille.ligne_list[k])
    print(nombre_bombe_autour)
    '''
    nb_bombe_aut=nombre_bombe_autour.count(1)       #compte le nombre de bombe autour
    Revelation_case.tt_rev.goto((-10*Grille.nb_collone)+n+5,(10*Grille.nb_ligne)-c-23)
    Revelation_case.tt_rev.pendown()
    if nb_bombe_aut ==1 and Test_click.fonction_revel==0:         #Si il y a au minimum une bombe écrire le nombre en couleurs sinon : case vide
        Revelation_case.tt_rev.color("blue")
        Revelation_case.tt_rev.write("1", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==2 and Test_click.fonction_revel==0:
        Revelation_case.tt_rev.color("green")
        Revelation_case.tt_rev.write("2", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==3 and Test_click.fonction_revel==0:
        Revelation_case.tt_rev.color("red")
        Revelation_case.tt_rev.write("3", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==4 and Test_click.fonction_revel==0:
        Revelation_case.tt_rev.color("purple")
        Revelation_case.tt_rev.write("4", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==5 and Test_click.fonction_revel==0:
        Revelation_case.tt_rev.color("brown")
        Revelation_case.tt_rev.write("5", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==6 and Test_click.fonction_revel==0:
        Revelation_case.tt_rev.color("orange")
        Revelation_case.tt_rev.write("6", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==7 and Test_click.fonction_revel==0:
        Revelation_case.tt_rev.color("pink")
        Revelation_case.tt_rev.write("7", font=("Arial", 15, "normal"))
    if nb_bombe_aut ==8 and Test_click.fonction_revel==0:
        Revelation_case.tt_rev.color("black")
        Revelation_case.tt_rev.write("8", font=("Arial", 15, "normal"))
        
    if nb_bombe_aut ==0:
        case_vérif.append(Grille.collone_list[i-temp_n]+Grille.ligne_list[k-temp_n])
        Revelation_case.revel_toute_case_blanche()
        
        
        
    Revelation_case.tt_rev.color("black")
    nombre_bombe_autour[:]= []
    Revelation_case.tt_rev.penup()




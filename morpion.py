def grille(listecases = []):
    print("\n",listecases[1],"|",listecases[2],"|",listecases[3], end=" ")
    print("\n", "-  ", "-  ", "-  ", end=" ")
    print("\n",listecases[4],"|",listecases[5], "|",listecases[6], end=" ")
    print("\n", "-  ", "-  ", "-  ", end=" ")
    print("\n",listecases[7], "|",listecases[8], "|",listecases[9], end=" ")


listecases = [0,1,2,3, 4,5,6, 7,8,9,10]
cj = 0

j1 = input("Nom du joueur 1 \n")
j2 = input("Nom du joueur 2 \n")


print("\n", "Indiquez quelle case remplacer en rentrant son chiffre. Une fois 3 cases alignées slectionnées, vous remportez la partie")



grille(listecases)

#Il y a 9 cases possibles donc on arrête quand il y a 9 cases jouées
while(cj < 9):

    c = 0
    #On vérifie quel joueur doit jouer
    if(cj%2):
        print("\n",j2, ", sélectionner la case à remplacer")
        case = int(input())
    else:
        print("\n",j1, ", sélectionner la case à remplacer")
        case = int(input())

    #On vérifie que la case est possible
    while(case != listecases[c]) or (case == 0) or (case == 10):
        
        #Si la case n'est pas possible, on demande de choisir une autre case et on recommence la vérification
        if(c > 9) or (case == 0) or (case == 10):
            case = int(input("Vous ne pouvez pas jouer sur cette case, choisissez une autre case \n"))
            c = 0

        c = c +1
    
    #On indique visuellement les cases remplies
    if(cj%2):
        listecases[case] = "O"
        v = "O"
        j=j2
    else:
        listecases[case] = "X"
        v ="X"
        j=j1
    
    #On incrémente le nombre de coups joués
    cj = cj + 1

    #On imprime le statut de la partie
    
    grille(listecases)

    #On vérifie qu'une ligne n'est pas remplis
    if(listecases[1] == v) and (listecases[2] == v) and (listecases[3] == v) :
        print("\n", j, "a gagné !")
        cj = 10
    if(listecases[4] == v) and (listecases[5] == v) and (listecases[6] == v) :
        print("\n", j, "a gagné !")
        cj = 10
    if(listecases[7] == v) and (listecases[8] == v) and (listecases[9] == v) :
        print("\n", j, "a gagné !")
        cj = 10
    if(listecases[1] == v) and (listecases[4] == v) and (listecases[7] == v) :
        print("\n", j, "a gagné !")
        cj = 10
    if(listecases[2] == v) and (listecases[5] == v) and (listecases[8] == v) :
        print("\n", j, "a gagné !")
        cj = 10
    if(listecases[3] == v) and (listecases[6] == v) and (listecases[9] == v) :
        print("\n", j, "a gagné !")
        cj = 10
    if(listecases[1] == v) and (listecases[5] == v) and (listecases[9] == v) :
        print("\n", j, "a gagné !")
        cj = 10
    if(listecases[3] == v) and (listecases[5] == v) and (listecases[7] == v) :
        print("\n", j, "a gagné !")
        cj = 10
    if(cj == 9) :
        print("\n C'est un match nul")
    

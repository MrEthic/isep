def createMatrice(matrice, n):
    for i in range(n):
        l = []
        for j in range(n):
            q = "Entré valeur ligne " + str(i + 1) + ", colone " + str(j + 1) + ":\t"
            v = float(input(q))
            l.append(v)
        matrice.append(l)
    
    


def affMatrice(matrice):
    prt = ""                        #Initialise un string "vide"
    for i in matrice:               #Pour chaque ligne i de la matrice
        for j in i:                 #Pour chaque valeur j de la ligne i
            prt += str(j) + "  "    #Ajoute la valeur j au string + un espace
        prt += "\n"                 #A la fin de chaque ligne on reviens a la ligne
    print(prt)                      #Imprime le sring de la matrice


matrice = []
createMatrice(matrice, 3)
affMatrice(matrice)
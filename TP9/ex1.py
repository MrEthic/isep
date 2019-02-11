def createMatrice(matrice, n):
    for i in range(n):
        l = []
        for j in range(n):
            q = "Entré valeur ligne " + str(i + 1) + ", colone " + str(j + 1) + ":\t"
            v = float(input(q))
            l.append(v)
        matrice.append(l)
    
    


def affMatrice(matrice):
    prt = ""
    for i in matrice:
        for j in i:
            prt += str(j) + "  "
        prt += "\n"
    print(prt)


matrice = []
createMatrice(matrice, 3)
affMatrice(matrice)
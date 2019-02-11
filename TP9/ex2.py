def createMatrice(matrice, ligne, colone):
    for i in range(ligne):
        l = []
        for j in range(colone):
            q = "Entré valeur ligne " + str(i + 1) + ", colone " + str(j + 1) + ":\t"
            v = float(input(q))
            l.append(v)
        matrice.append(l)    


def affMatrice(m):
    prt = ""
    for i in m:
        for j in i:
            prt += str(j) + "  "
        prt += "\n"
    print(prt)

matrice = []
createMatrice(matrice, 3, 4)
affMatrice(matrice)
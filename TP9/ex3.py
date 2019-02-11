def trianglePascal(h):
    triangle = [[1], [1,1]]
    for i in range(2, h):
        ligne = [1]
        for j in range(1, i):
            ligne.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        ligne.append(1)
        triangle.append(ligne)

    affichage = ""

    for l in triangle:
        for c in l:
            affichage += str(c) + "  "
        affichage += "\n"

    print(affichage)



trianglePascal(9)

PRODUITS = {
    0: {
        "name": "Brique de lait",
        "price": 2.5,
        "amount_sell": 0
    },
    1: {
        "name": "Barre de chocolat",
        "price": 1.5,
        "amount_sell": 0
    },
    2: {
        "name": "Bouteille d'eau",
        "price": 2.0,
        "amount_sell": 0
    }
}

class Magasin():
    def __init__(self, PRODUCT = PRODUITS):
        self.PRODUITS = PRODUCT
        self.chiffreAffaire = 0

    def printResult(self):
        result = "\nResultat de mon magasin :\n\nPar produits :\n" + 40 * "-" + "\n" + "Produit\t\t\tMontant\tRecette\n"
        for produit in self.PRODUITS.values():
            result += "#" + produit["name"] + "(" + str(produit["price"]) + ")" + "\t" + str(produit["amount_sell"]) + "\t" + str(produit["amount_sell"] * produit["price"]) + "\n"

        result += "\nChiffre d'affaire total : " + str(self.chiffreAffaire)
        print(result)


class Facture():
    def __init__(self, shop = Magasin()):
        self.shop = shop
        self.__products = []
        self.ticket = "------------TICKET------------\n"
        self.__total = 0

    def addProduct(self, product, amount = 1):

        if not product in self.shop.PRODUITS.keys():
            print("ERREUR : Code barre invalide\n------------------------------")
            return

        add = self.shop.PRODUITS[product]

        for i in range(amount):
            self.__products.append(add)
            self.shop.PRODUITS[product]["amount_sell"] += 1
        
        self.__total += amount * add["price"]

        ligne = "\r" + str(amount) + " x " + add["name"] + "(" + str(add["price"]) + ") = " + str(amount * add["price"]) + "€\n" + 30 * "-"
        self.ticket += ligne

        print(ligne)

    def finFacture(self):
        self.shop.chiffreAffaire += self.__total
        self.ticket += "\nTOTAL A PAYER : " + str(self.__total) + "€"
        print("\n", self.ticket, sep="")


monMagasin = Magasin(PRODUITS)

factureA = Facture(monMagasin)
factureA.addProduct(0, 2)
factureA.addProduct(1)
factureA.addProduct(4)
factureA.addProduct(2, 3)
factureA.finFacture()

monMagasin.printResult()


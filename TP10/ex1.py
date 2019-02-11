class Eleve():

    listeEleves = []

    def __init__(self, identifiant, name, firstName, classe, groupe):
        if not isinstance(identifiant, int) or identifiant < 1:
            print("L'identifiant saisi n'est pas valide (entier > 0)")
            raise Exception()
        for eleve in Eleve.listeEleves:
            if eleve.identifiant == identifiant:
                print("L'identifiant saisie existe déjà pour :", eleve.name, eleve.firstName)
                raise Exception()
        self.identifiant = identifiant
        self.name = name
        self.firstName = firstName
        self.classe = classe
        self.groupe = groupe

        Eleve.listeEleves.append(self)



e1 = Eleve(0.5, "Pierre", "Henri", "I1", "T2")
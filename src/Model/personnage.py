class Personnage:
    def __init__(self, nom: str, competence1: str,competence2: str):
        """
        Constructeur de la classe Personnage.
        Correspond à l'attribut : + nom: String
        """
        self.nom = nom
        self.competence1 = competence1
        self.competence2 = competence2

    def attaquer(self, cible):
        """
        Correspond à la méthode : + Attaquer
        """
        print(f"{self.nom} attaque {cible.nom} !")

    def competence_1(self):
        print(f"{self.nom} utilise {self.competence1} !")

    def competence_2(self):
        print(f"{self.nom} utilise {self.competence2} !")

    def defense(self):
        print(f"{self.nom} se protege.")

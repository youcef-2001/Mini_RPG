from abc import ABC, abstractmethod
class Personnage(ABC):
    def __init__(self, nom: str, competence1: str,competence2: str):
        self.nom = nom
        self.competence1 = competence1
        self.competence2 = competence2
    @abstractmethod
    def attaquer(self, opposant :'Personnage'):
        print(f"{self.nom} attaque {opposant.nom} !")

    @abstractmethod
    def competence_1(self):
        print(f"{self.nom} utilise {self.competence1} !")

    @abstractmethod
    def competence_2(self):
        print(f"{self.nom} utilise {self.competence2} !")

    @abstractmethod
    def defense(self):
        print(f"{self.nom} se protege.")

class Player(Personnage):
    def __init__(self, nom: str, classe: str, stats: int, offensif: int, defensif: int, capacite_armes: int, liste_inventaire: list[str] | None = None,inventaire: list[str] | None = None):
        super().__init__(nom)
        self.classe = classe
        self.stats = stats
        self.offensif = offensif
        self.defensif = defensif
        self.capacite_armes = capacite_armes
        self.liste_inventaire = []
        self.inventaire= []

    def attaquer(self, cible: Personnage):
        degats = self.offensif + (self.stats // 2)
        print(f"{self.nom} attaque {cible.nom} et fait {degats} degats")

    def se_defendre(self):
        print(f"{self.nom} se protege {self.defensif}")

    def utiliser_competence(self):
        pass

class Guerrier(Player):
    def __init__(self, nom: str):
        super().__init__(nom, classe="Guerrier", stats=150, offensif=20, defensif=15, capacite_armes=2)
        self.bonus = "Rage Berserk"

    def utiliser_competence1(self):
        print(f"{self.nom} lance Frappe Héroïque inflige {degats} a {cible.nom}")

    def utiliser_competence2(self):
        print(f"{self.nom} étourdi {cible.nom} !")

class Mage(Player):
    def __init__(self, nom: str):
        super().__init__(nom, classe="Mage", stats=100, offensif=30, defensif=5, capacite_armes=1)
        self.bonus = "Intelligence Arcane"

    def utiliser_competence1(self):
        print(f"{self.nom} lance Boule de Feu inflige {degats} a {cible.nom}")
    def utiliser_competence2(self):
        print(f"{self.nom} empoisonne {cible.nom}")

class Voleur(Player):
    def __init__(self, nom: str):
        super().__init__(nom, classe="Voleur", stats=110, offensif=25, defensif=8, capacite_armes=2)
        self.bonus = "Attaque Sournoise"

    def utiliser_competence1(self):
        print(f"{self.nom} devient invisible !")

    def utiliser_competence2(self):
        print(f"{self.nom} vole {cible.nom} !")

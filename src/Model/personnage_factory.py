from abc import ABC, abstractmethod
from typing import List

from Model.Objet import Objet
class Personnage(ABC):
    def __init__(self, nom: str, competence1: str,competence2: str, PV_max : int, current_PV : int):
        self.nom = nom
        self.competence1 = competence1
        self.competence2 = competence2
        self.PV_max = PV_max
        self.current_PV = current_PV
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
    def __init__(self, nom: str, offensif: int, defensif: int, capacite_armes: int,competence1 : str, competence2 : str,):
        super().__init__(nom)
        self.offensif = offensif
        self.defensif = defensif
        self.capacite_armes = capacite_armes
        self.inventaire : List[Objet] = []
        self.competence1 = competence1
        self.competence2 = competence2

    def attaquer(self, cible: Personnage):
        degats = self.offensif
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} attaque {cible.nom} et fait {degats} degats")

    def se_defendre(self):
        print(f"{self.nom} se protege {self.defensif}")

    def utiliser_competence(self):
        pass

class Guerrier(Player):
    def __init__(self, nom: str):
        super().__init__(nom,PV_max=150, offensif=20, defensif=15, capacite_armes=2,competence1 = "Frappe héroique", competence2="ground&pound")
        self.bonus = "Rage Berserk"

    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,2
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} lance Frappe Héroïque inflige {degats} a {cible.nom}")

    def utiliser_competence2(self, cible : Personnage):
        """
        mettre en place un status stun
        """
        print(f"{self.nom} étourdi {cible.nom} !")


class Mage(Player):
    def __init__(self, nom: str):
        super().__init__(nom, classe="Mage", PV_max=100, offensif=30, defensif=5, capacite_armes=1,competence1 = "Boule de feu", competence2="Poison")
        self.bonus = "Intelligence Arcane"

    def utiliser_competence1(self, cible : Personnage):
         degats = self.offensif*1,5
         cible.current_PV = cible.current_PV - degats
         print(f"{self.nom} lance Boule de Feu inflige {degats} a {cible.nom}")
    def utiliser_competence2(self, cible : Personnage):
        """"
        mettre en place un status empoisoner
        """
        print(f"{self.nom} empoisonne {cible.nom}")

class Voleur(Player):
    def __init__(self, nom: str):
        super().__init__(nom, classe="Voleur", PV_max=110, offensif=25, defensif=8, capacite_armes=2,competence1 = "Attaque fourbe", competence2="Vole inée")
        self.bonus = "Attaque Sournoise"

    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,5
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} donne deux coup de dague rapide")

    def utiliser_competence2(self, cible : Personnage):
        """"
        voler a ennemi mettre dans inventaire
        """
        print(f"{self.nom} vole {cible.nom} !")

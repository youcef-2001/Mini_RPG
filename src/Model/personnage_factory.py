from abc import ABC, abstractmethod
from typing import List
import random
from Model.Objet import Objet,Inventaire


class Personnage(ABC):
    def __init__(self, nom: str, competence1: str,competence2: str, PV_max : int, current_PV : int, status):
        self.nom = nom
        self.competence1 = competence1
        self.competence2 = competence2
        self.PV_max = PV_max
        self.current_PV = current_PV
        self.status = []
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

    @abstractmethod
    def debut_de_tour(self, status):
        if status is None: pass

        if status is not None: status.appliquer(self)
        """"
        si status pas = none appliquer effet du status
        """
    def ajouter_statut(self, statut):
        statut.appliquer(self)
        self.statuts.append(statut)

    def traiter_statuts(self):
        for statut in self.statuts[:]:
            statut.declencher(self)
            statut.reduire_duree()

            if  statut.is_expired():
                statut.a_expiration(self)
                self.statuts.remove(statut)

class Player(Personnage):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,armures: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status):
        super().__init__(nom, competence1, competence2 , PV_max , current_PV , status)
        self.offensif = offensif
        self.defensif = defensif
        self.armes = armes
        self.armures = armures
        self.inventaire = Inventaire()
        self.competence1 = competence1
        self.competence2 = competence2

    def attaquer(self, cible: Personnage):
        degats = self.offensif
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} attaque {cible.nom} et fait {degats} degats")

    def se_defendre(self):
        print(f"{self.nom} se protege {self.defensif}")

class Guerrier(Player):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, offensif=20, defensif=15, armes=None,armures=None, competence1 = "Frappe héroique", competence2="ground&pound",PV_max=150,current_PV=150,status= None)
        self.bonus = "Rage Berserk"

    def utiliser_attaque(self, cible : Player):
         degats = (self.offensif + self.armes) - (cible.armures + cible.defensif)
         cible.current_PV = cible.current_PV - degats
         print(f"{self.nom} donne un coup d'epée {degats} a {cible.nom}")

    def utiliser_defense(self, cible : Personnage):
         protection = self.defensif*1.5
         print(f"{self.nom} se met en garde")

    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,4
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} lance Frappe Héroïque inflige {degats} a {cible.nom}")

    def utiliser_competence2(self, cible : Personnage,status):
        if {cible.nom(status)} is None: status.appliquer({cible.nom})
        if {cible.nom(status)} is not None : pass
        print(f"{self.nom} étourdi {cible.nom} !")


class Mage(Player):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, classe="Mage",  offensif=30, defensif=5, armes=None,armures=None,competence1 = "Boule de feu", competence2="Poison",PV_max=100,current_PV=150,status= None)
        self.bonus = "Intelligence Arcane"

    def utiliser_attaque(self, cible : Player):
         degats = (self.offensif + self.armes) - (cible.armures + cible.defensif)
         cible.current_PV = cible.current_PV - (degats - {cible.defensif})
         print(f"{self.nom} donne un coup de baton {degats} a {cible.nom}")

    def utiliser_defense(self, cible : Personnage):
         protection = self.defensif*1.1
         print(f"{self.nom} se met en garde")

    def utiliser_competence1(self, cible : Personnage):
         degats = (self.offensif+self.armes)*1,5
         cible.current_PV = cible.current_PV - degats
         print(f"{self.nom} lance Boule de Feu inflige {degats} a {cible.nom}")

    def utiliser_competence2(self, cible : Personnage, status):
        if {cible.nom(status)} is None: status.appliquer({cible.nom})
        if {cible.nom(status)} is not None : pass
        print(f"{self.nom} empoisonne {cible.nom}")

class Voleur(Player):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, classe="Voleur",  offensif=25, defensif=8, armes=None,armures=None,competence1 = "Attaque fourbe", competence2="Vole inée",PV_max=110,current_PV=150,status= None)
        self.bonus = "Attaque Sournoise"

    def utiliser_attaque(self, cible : Player):
         degats = degats = (self.offensif + self.armes) - (cible.armures + cible.defensif)
         cible.current_PV = cible.current_PV - (degats - {cible.defensif})
         print(f"{self.nom} donne un coup de dague {degats} a {cible.nom}")

    def utiliser_defense(self, cible : Personnage):
         protection = self.defensif*1.1
         print(f"{self.nom} se met en garde")


    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,5
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} donne deux coup de dague rapide")

    def utiliser_competence2(self, cible : Personnage, inventaire):
        if {cible.nom(inventaire)} is None : 
            print(f"{cible.nom} a rien je lui passe une piece mskn")
            pass
        if {cible.nom(inventaire)} is not None :
             objet_vole = random.choice(cible.inventaire.objets)
             print(f"succès ! {self.nom} a volé {objet_vole.name} à {cible.nom} !")
        else :
             print(f"{self.nom} essaie de voler {objet_vole.name}, mais a plus de place")
        



class Enemy(Personnage):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,armures: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, competence1, competence2 , PV_max , current_PV , status)
        self.offensif = offensif
        self.defensif = defensif
        self.armes = armes
        self.armures = armures
        self.inventaire : List[Objet] = []
        self.competence1 = competence1
        self.competence2 = competence2

    def attaquer(self, cible: Personnage):
        degats = self.offensif
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} attaque {cible.nom} et fait {degats} degats")

    def se_defendre(self):
        print(f"{self.nom} se protege {self.defensif}")

class Loup_sauvage(Enemy):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, offensif=20, defensif=15, armes=None,armures=None,competence1 = "morsure", competence2="Double patte",PV_max=150,current_PV=150,status= None)
        self.bonus = "meute offensif"

    def utiliser_attaque(self, cible : Player):
         degats = (self.offensif + self.armes) - (cible.armures + cible.defensif)
         cible.current_PV = cible.current_PV - (degats - {cible.defensif})
         print(f"{self.nom} mors{degats} a {cible.nom}")

    def utiliser_defense(self, cible : Personnage):
         protection = self.defensif*1.2
         print(f"{self.nom} se met en garde")

    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,1
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} lance morsure {degats} a {cible.nom}")

    def utiliser_competence2(self, cible : Personnage,status):
        degats = self.offensif
        cible.current_PV = cible.current_PV - degats
        degats = self.offensif
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} Double attaque {cible.nom} !")


class Bandit(Enemy):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, offensif=20, defensif=15, armes=None,armures=None,competence1 = "Couteau usé", competence2="vole inée",PV_max=150,current_PV=150,status= None)
        self.bonus = "meute offensif"

    def utiliser_attaque(self, cible : Player):
         degats = (self.offensif + self.armes) - (cible.armures + cible.defensif)
         cible.current_PV = cible.current_PV - (degats - {cible.defensif})
         print(f"{self.nom} enleve {degats} a {cible.nom}")

    def utiliser_defense(self, cible : Personnage):
         protection = self.defensif*1.2
         print(f"{self.nom} se met en garde")

    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,1
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} couteau usé {degats} a {cible.nom}")

    def utiliser_competence2(self, cible : Personnage, inventaire):
        if {cible.nom(inventaire)} is None : 
            print(f"{cible.nom} a rien je lui passe une piece mskn")
            pass
        if {cible.nom(inventaire)} is not None :
             objet_vole = random.choice(cible.inventaire.objets)
             print(f"succès ! {self.nom} a volé {objet_vole.name} à {cible.nom} !")
        else :
             print(f"{self.nom} essaie de voler {objet_vole.name}, mais a plus de place")

class Squelette(Enemy):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, offensif=20, defensif=15, armes=None,armures=None,competence1 = " os ronger", competence2="maladie squeletique",PV_max=150,current_PV=150,status= None)
        self.bonus = "meute offensif"

    def utiliser_attaque(self, cible : Player):
         degats = (self.offensif + self.armes) - (cible.armures + cible.defensif)
         cible.current_PV = cible.current_PV - (degats - {cible.defensif})
         print(f"{self.nom} enleve {degats} a {cible.nom}")

    def utiliser_defense(self, cible : Personnage):
         protection = self.defensif*1.2
         print(f"{self.nom} se met en garde")

    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,1
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} couteau usé {degats} a {cible.nom}")

    def utiliser_competence2(self, cible : Personnage,status):
        if {cible.nom(status)} is None: status.appliquer({cible.nom})
        if {cible.nom(status)} is not None : pass
        print(f"{self.nom} empoisonne {cible.nom}")


class Champion_corrompu(Enemy):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, offensif=20, defensif=15, armes=None,armures=None,competence1 = " Coup de poing pieger", competence2="coup derriere le crane",PV_max=150,current_PV=150,status= None)
        self.bonus = "meute offensif"

    def utiliser_attaque(self, cible : Player):
         degats = (self.offensif + self.armes) - (cible.armures + cible.defensif)
         cible.current_PV = cible.current_PV - (degats - {cible.defensif})
         print(f"{self.nom} enleve {degats} a {cible.nom}")

    def utiliser_defense(self, cible : Personnage):
         protection = self.defensif*1.2
         print(f"{self.nom} se met en garde")

    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,1
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} coup du tricheur {degats} a {cible.nom}")

    def utiliser_competence2(self, cible : Personnage,status):
        if {cible.nom(status)} is None: status.appliquer({cible.nom})
        if {cible.nom(status)} is not None : pass
        print(f"{self.nom} un coup ilégal qui stun {cible.nom} !")


class Gardien_du_donjon(Enemy):
    def __init__(self, nom: str, offensif: int, defensif: int, armes: int,competence1: str,competence2: str, PV_max : int, current_PV : int, status, inventaire):
        super().__init__(nom, offensif=20, defensif=15, armes=None,armures=None,competence1 = " Coup de poing pieger", competence2="coup derriere le crane",PV_max=150,current_PV=150,status= None)
        self.bonus = "meute offensif"
        self.deuxieme_phase = False

    def utiliser_attaque(self, cible : Player):
         degats = (self.offensif + self.armes) - (cible.armures + cible.defensif)
         cible.current_PV = cible.current_PV - (degats - {cible.defensif})
         print(f"{self.nom} enleve {degats} a {cible.nom}")

    def utiliser_defense(self, cible : Personnage):
         protection = self.defensif*1.5
         print(f"{self.nom} se met en garde")

    def utiliser_competence1(self, cible : Personnage):
        degats = self.offensif*1,7
        cible.current_PV = cible.current_PV - degats
        print(f"{self.nom} coup du tricheur {degats} a {cible.nom}")

    def utiliser_competence2(self, cible : Personnage,status):
        degats = self.offensif*1,2
        if {cible.nom(status)} is None: status.appliquer({cible.nom})
        if {cible.nom(status)} is not None : pass
        print(f"{self.nom} un coup ilégal qui stun {cible.nom} !")

    def deuxieme_manche(self):
        if self.current_PV <= (self.PV_max / 2) and self.deuxieme_phase == False:
            self.offensif *= 2
            self.defensif *= 2
            self.current_PV += 20
            self.deuxieme_phase = True
            print(f"{self.nom} tu la zehef, ses stats sont doublées")

class EnemyFactory:
    @staticmethod
    def create_enemy(type_enemy: str) -> Enemy:
        type_enemy = type_enemy.lower()
        
        dummy_args = {
            "offensif": 0, 
            "defensif": 0, 
            "armes": 0, 
            "competence1": "", 
            "competence2": "", 
            "PV_max": 0, 
            "current_PV": 0, 
            "status": None, 
            "inventaire": None
        }

        if type_enemy == "loup":
            return Loup_sauvage(nom="Loup Sauvage", **dummy_args)
        
        elif type_enemy == "bandit":
            return Bandit(nom="Bandit", **dummy_args)
        
        elif type_enemy == "squelette":
            return Squelette(nom="Squelette", **dummy_args)
        
        elif type_enemy == "champion":
            return Champion_corrompu(nom="Champion Corrompu", **dummy_args)
        
        elif type_enemy == "gardien":
            return Gardien_du_donjon(nom="Gardien du Donjon", **dummy_args)
        
        else:
            raise ValueError(f"Type d'ennemi inconnu : {type_enemy}")
        
class PNJ(Personnage):
    def __init__(self, nom: str, competence1: str, competence2: str, PV_max: int, current_PV: int, status):
        super().__init__(nom, competence1, competence2, PV_max, current_PV, status)
    
    def interagir(self, joueur):
        print(f"{self.nom} viens te pénave")

    def attaquer(self, opposant: 'Personnage'):
        print(f"{self.nom} ne veut pas se battre !")

    def competence_1(self):
        pass

    def competence_2(self):
        pass

    def defense(self):
        print(f"{self.nom} arrete de m'attaquer gros hagar")

    def debut_de_tour(self, status):
        pass


class Marchand(PNJ):
    def __init__(self, nom="Marchand Itinérant"):
        super().__init__(nom, competence1="Négociation", competence2="Fuite", PV_max=50, current_PV=50, status=None)
        self.inventaire_a_vendre = ["Potion de soin", "Épée en fer", "Bouclier en bois"] 

    def interagir(self, joueur):
        print(f"--- {self.nom} ---")
        print("Sur Place ou pas a emporter chef?")
        for item in self.inventaire_a_vendre:
            print(f"- {item}")
    def defense(self):
        print(f"{self.nom} touche pas la bagnole")
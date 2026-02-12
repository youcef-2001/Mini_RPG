from abc import ABC, abstractmethod
import random

class Enemy(ABC):

    def __init__(self, nom, lvl, offensif, defensif, gold, experience, zone, competence1,competence2,item=None):
        self.nom = nom
        self.lvl = lvl
        self.max_hp = lvl * 10
        self.current_hp = self.max_hp
        self.offensif = offensif
        self.defensif = defensif
        self.gold = gold
        self.experience = experience
        self.zone = zone
        self.item = item
        self.passif = ""
        self.competence1 = competence1
        self.competence2 = competence2

class Loup(Enemy):
    def __init__(self):
        super().__init__("Loup Sauvage", lvl=1, offensif=8, defensif=2, 
                         gold=5, experience=10, zone="Foret", item="Fourrure")
        self.passif = "Attaque Rapide"

    def perform_action(self, player):
        print(f"Le {self.nom} vous attaque")

class Bandit(Enemy):
    def __init__(self):
        super().__init__("Bandit des Ombres", lvl=2, offensif=10, defensif=3, 
                         gold=15, experience=20, zone="Foret", item="Dague rouillée")
        self.passif = "Voleur"

    def perform_action(self, player):
        action = random.choice(["attaque", "vol"])
        if action == "vol":
            print(f"Le {self.nom} tente de vous voler")
        else:
            print(f"Le {self.nom} vous attaque")

class Squelette(Enemy):
    def __init__(self):
        super().__init__("Squelette", lvl=3, offensif=12, defensif=8, 
                         gold=10, experience=25, zone="Donjon", item="Ossement")
        self.passif = "Résistance Physique"

    def perform_action(self, player):
        print(f"Le {self.nom} vous attaque")
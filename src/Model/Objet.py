
class Objet:
    def __init__(self, name):
        self.name = name


class Key(Objet):
    def __init__(self, name):
        super().__init__(name)

class consommable(Objet): 
    def __init__(self, name):
        self.name = name


    def consommer(self, personnage, enemy):
        raise NotImplementedError


class Potion(consommable):
    def __init__(self):
        super().__init__("Potion")
    
    def consommer(self, personnage, enemy):
        personnage.current_PV = personnage.current_PV + int(personnage.PV_max * 0.2)
        
        if personnage.current_PV > personnage.PV_max:
            personnage.current_PV = personnage.PV_max

        print(f"{personnage.nom} recupere {personnage.PV_max * 0.2}")
    
class Bombe(consommable):
    def __init__(self):
        super().__init__("Bombe")

    def consommer(self, personnage, enemy):
        degats = 30
        enemy.current_PV -= degats
        print(f"{enemy.nom} subit {degats} degats !")

class Antidote(consommable):
    def __init__(self):
        super().__init__("Antidote")

    def consommer(self, personnage, enemy):
        avant = len(personnage.statuts)
        personnage.statuts = [s for s in personnage.statuts if s.nom != "Poison"]
        apres = len(personnage.statuts)

        if avant != apres:
            print(f"{personnage.nom} est soigné du poison !")
        else:
            print("Aucun poison à retirer.")



    
class Equipement(Objet):
    def __init__(self, name: str, classe: str, degat_sup: int, gold: int, type_: str):
        super().__init__(name)
        self.classe = classe
        self.degat_sup = degat_sup
        self.gold = gold
        self.type = type_   

    def appliquer_bonus(self, personnage):
        if self.type == "Arme":
            personnage.offensif += self.degat_sup
        elif self.type == "Armure":
            personnage.defensif += self.degat_sup

class VoleurEquipement(Equipement):
    def __init__(self, name, degat_sup, gold, type_="Arme"):
        super().__init__(name, "Voleur", degat_sup, gold, type_)


class Dague(VoleurEquipement):
    def __init__(self):
        super().__init__(
            name="Dague",
            degat_sup=6,
            gold=2
        )

class MageEquipement(Equipement):
    def __init__(self, name, degat_sup, gold, type_="Arme"):
        super().__init__(name, "Mage", degat_sup, gold, type_)

class Orbe(MageEquipement):
    def __init__(self):
        super().__init__(
            name="Orbe",
            degat_sup=8,
            gold=2
        )


class GuerrierEquipement(Equipement):
    def __init__(self, name, degat_sup, gold, type_="Arme"):
        super().__init__(name, "Guerrier", degat_sup, gold, type_)

class SabreLourd(GuerrierEquipement):
    def __init__(self):
        super().__init__(
            name="SabreLourd",
            degat_sup=10,
            gold=5
        )

class CommuneEquipement(Equipement):
    def __init__(self, name, degat_sup, gold, type_="Armure"):
        super().__init__(name, "Commune", degat_sup, gold, type_)

class CostumeEnCuir(CommuneEquipement):
    def __init__(self):
        super().__init__(
            name="CostumeEnCuir",
            degat_sup=3,
            gold=4,
        )

class ObjetsFactory:

    @staticmethod
    def creer_objet(type_objet: str):

        objets = {
            "Dag": Dague,
            "Orbe": Orbe,
            "SabreLourd": SabreLourd,
            "CostumeEnCuir": CostumeEnCuir,
            "Potion": Potion,
            "Bombe": Bombe,
            "Antidote": Antidote
        }

        if type_objet in objets:
            return objets[type_objet]()
        else:
            raise ValueError("Objet inconnu")

class Inventaire:

    def __init__(self, limite_slots: int = 10):
        self.objets: list[Objet] = []
        self.limite_slots = limite_slots

    def ajouter_objet(self, objet: Objet) -> bool:

        if len(self.objets) >= self.limite_slots:
            print("Inventaire plein !")
            return False

        self.objets.append(objet)
        print(f"{objet.name} ajouté à l'inventaire.")
        return True

    def retirer_objet(self, objet: Objet) -> bool:
 
        if objet in self.objets:
            self.objets.remove(objet)
            print(f"{objet.name} retiré de l'inventaire.")
            return True

        print("Objet introuvable.")
        return False

    def afficher(self):
        if not self.objets:
            print("Inventaire vide.")
            return

        print("=== Inventaire ===")
        for i, obj in enumerate(self.objets, 1):
            print(f"{i}. {obj.name}")

      

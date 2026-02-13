
class Objet:
    def __init__(self, name):
        self.name = name


class key(Objet):
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setName(self, value):
        self.name = value


class consommable(Objet): 
    def __init__(self, name):
        self.name = name


    def consommer(self, personnage, enemy):
        raise NotImplementedError


class Potion(consommable):
    def __init__(self):
        super().__init__("Potion")
    
    def consommer(self, personnage, enemy):
        personnage.current_PV = personnage.current_PV + personnage.PV_max * 0.2
        
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
        personnage.statuts = [s for s in personnage.statuts if s.nom != "Poison"]
        print(f"{personnage.nom} est soigné du poison !")


    
class Equipement(Objet):
    def __init__(self, name, classe, stats, poids, type_, passif):
        super().__init__(name)
        self.classe = classe        
        self.stats = stats          
        self.poids = poids
        self.type = type_           
        self.passif = passif 

    def appliquer_bonus(self, personnage):
        if self.type == "Arme":
            personnage.offensif += self.stats
        elif self.type == "Armure":
            personnage.defensif += self.stats

class VoleurEquipement(Equipement):
    def __init__(self, nom, poids, effet=None, bonus=None):
        super().__init__(nom, "Voleur", poids, passif=effet)
        self.effet = effet
        self.bonus = bonus

class Dag(VoleurEquipement):
    def __init__(self, nom, poids, effet=None, bonus=None):
        super().__init__("Dag", poids, effet, bonus)

class MageEquipement(Equipement):
    def __init__(self, nom, stats, poids, type_, effet=None, bonus=None):
        super().__init__(nom, "Mage", stats, poids, type_, passif=effet)
        self.effet = effet
        self.bonus = bonus

class GuerrierEquipement(Equipement):
    def __init__(self, nom, stats, poids, type_, effet=None, bonus=None):
        super().__init__(nom, "Guerrier", stats, poids, type_, passif=effet)
        self.effet = effet
        self.bonus = bonus

class CommuneEquipement(Equipement):
    def __init__(self, nom, stats, poids, type_, effet=None, bonus=None):
        super().__init__(nom, "Commune", stats, poids, type_, passif=effet)
        self.effet = effet
        self.bonus = bonus


class ObjetsFactory:

    @staticmethod
    def creer_objet(type_objet: str):
        objets = {
            "Potion": lambda: Potion(),
            "Bombe": lambda: Bombe(),
            "Antidote": lambda: Antidote(),
            "EpeeGuerrier": lambda: GuerrierEquipement()
        }

      


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
    
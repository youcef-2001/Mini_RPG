from typing import override


class Event:
    def __init__(self) :
        self.finished= False
        

    def lancer(self) : 
        print("executer l'event")

class Walking(Event):
    @override
    def lancer(self):
        print("je marche")
        self.finished = True

class Marchand(Event):
    def __init__(self) :
        super().__init__()
        self.marchand= PNJFactory.getmarchand()


    @override
    def lancer(self):
        print(f"Tu as rencontrer un Marchand{self.marchand}")
        print(f"le marchand possede {self.marchand.inventaire}")
        choice= input(f"quel objet voulez vous achetez")
        match choice :
            case "quit": print("vous quittez le marchand")
            case _: print("retry please")

        self.finished = True

class Combat(Event):
    @override
    def lancer(self):
        print(" en combat ")
        self.finished = True

class Coffre(Event):
    @override
    def lancer(self):
        print("je viens de trouver un coffre")
        self.finished = True

class Dialogue(Event):
    @override
    def lancer(self):
        print("je dialogue pour avancer dans la quete")
        self.finished = True


    
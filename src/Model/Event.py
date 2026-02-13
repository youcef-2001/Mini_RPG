from typing import override


class Event:
    def __init__(self) -> None:
        pass

    def lancer(self) : 
        print("executer l'event")

class Walking(Event):
    @override
    def lancer(self):
        print("je marche")

class Marchand(Event):
    @override
    def lancer(self):
        print("je TE VEND DES TRUCS")

class Combat(Event):
    @override
    def lancer(self):
        print(" en combat ")

class Coffre(Event):
    @override
    def lancer(self):
        print("je viens de trouver un coffre")

class Dialogue(Event):
    @override
    def lancer(self):
        print("je jedialogue pour avancer dans la quete")
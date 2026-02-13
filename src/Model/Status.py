from abc import ABC, abstractmethod

class Status(ABC):

    def __init__(self, nom: str, duree: int):
        self.nom = nom
        self.duree = duree

    def appliquer(self, cible):
        print(f"{cible.nom} est affecté par {self.nom} pour {self.duree} tours.")

    def reduire_duree(self, valeur: int = 1):
        self.duree -= valeur

    def is_expired(self) -> bool:
        return self.duree <= 0

    @abstractmethod
    def declencher(self, cible):
        pass

    def a_expiration(self, cible):
        """
        Appelé quand le statut expire.
        """
        print(f"{self.nom} sur {cible.nom} a expiré.")


class Poison(Status):

    def __init__(self, degats_par_tour: int = 5, duree: int = 3):
        super().__init__("Poison", duree)
        self.degats_par_tour = degats_par_tour

    def declencher(self, cible):
        cible.current_PV -= self.degats_par_tour
        print(f"{cible.nom} subit {self.degats_par_tour} degats de poison !")


class Bouclier(Status):

    def __init__(self, absorption: int = 20, duree: int = 2):
        super().__init__("Bouclier", duree)
        self.absorption_restante = absorption

    def declencher(self, cible):
        pass

    def absorber_degats(self, degats: int) -> int:
        if self.absorption_restante <= 0:
            return degats

        absorption = min(degats, self.absorption_restante)
        self.absorption_restante -= absorption
        print(f"Le bouclier absorbe {absorption} degats !")

        return degats - absorption

    def is_expired(self):
        return self.duree <= 0 or self.absorption_restante <= 0
    
    def a_expiration(self, cible):
        print("Le bouclier disparaît.")

    

class Etourdissement(Status):

    def __init__(self):
        super().__init__("Etourdissement", 1)

    def declencher(self, cible):
        print(f"{cible.nom} est étourdi et ne peut pas agir !")


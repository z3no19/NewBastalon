from abc import ABC
from src.Loot import Loot

class Nemico():
    def __init__(self, Vita: int, Attacco: int, Agilita: int):

        self.Vita = Vita
        self.Attacco = Attacco
        self.Agilita = Agilita

    def LifeCheck(self):
        if self.Vita <= 0:
            print("Nemico Morto")
            Loot.DropMonete()

    def Movimento(self, Agilita):
        pass

    def DroppaLoot(self):
        Loot.DropMonete

    def __str__(self):
        return f"Le statistiche del nemico sono: Vita{self.Vita} - Attacco {self.Attacco} - Agilità {self.Agilita}"
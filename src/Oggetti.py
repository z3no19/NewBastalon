from abc import ABC
from .Loot import Loot
from .Armi import Arma
from .Inventario import Inventario

class Oggetti():
    def __init__(self, Vita: int):

        self.Vita = Vita

    def RiceviDanno(self, Vita,DannoGiocatore):
        Vita
        self.Vita -= DannoGiocatore
        pass

    def LifeCheck(self):
        if self.Vita <= 0:
            print("Oggetto Distrutto")
            self.DroppaLoot()

    def DroppaLoot(self):
        Loot.DropMonete()
        Loot.DropArma()
        pass

    def __str__(self):
        return f"Sono un oggetto e ho vita {self.Vita}"
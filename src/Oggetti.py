from abc import ABC
from Loot import Loot

class Oggetti():
    def __init__(self, Vita: int):

        self.Vita = Vita

    def RiceviDanno(self, Vita,DannoGiocatore):
        Vita
        self.Vita -= DannoGiocatore
        pass

    def DroppaLoot(self):
        Loot.DropMonete
        Loot.DropArma
        pass

    def __str__(self):
        return f"Sono un oggetto e ho vita {self.Vita}"
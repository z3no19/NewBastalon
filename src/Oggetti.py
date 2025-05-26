from abc import ABC

class Oggetti():
    def __init__(self, Vita: int):

        self.Vita = Vita

    def RiceviDanno(self, Vita, DannoNemico, DannoGiocatore):
        pass

    def DroppaLoot(self):
        pass

    def __str__(self):
        return f"Sono un oggetto e ho vita {self.Vita}"
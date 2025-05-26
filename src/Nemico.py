from abc import ABC

class Nemico():
    def __init__(self, Vita: int, Forza: int, Agilita: int):

        self.Vita = Vita
        self.Forza = Forza
        self.Agilita = Agilita

    def Movimento(self, Agilita):
        pass
    
    def Attacco(self, Forza):
        DannoNemico = Forza * 2
        return DannoNemico

    def RiceviDanno(self, Vita, DannoGiocatore):
        pass

    def DroppaLoot(self):
        pass

    def __str__(self):
        return f"Le statistiche del nemico sono: Vita{self.Vita} - Forza {self.Forza} - Agilità {self.Agilita}"
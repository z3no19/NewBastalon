from abc import ABC

class Personaggio():
    def __init__(self, Vita: int, Forza: int, Agilita: int):

        self.Vita = Vita
        self.Forza = Forza
        self.Agilita = Agilita

    def GetStat(self, Vita, Forza, Agilita):
        pass

    def Movimento(self, Agilita):
        Velocita = Agilita * 0.1
        return Velocita
    
    def Attacco(self, Forza, Arma):
        Attacco = (Forza * Arma)/2
        return Attacco
    

    def RiceviDanno(self, Vita, DannoNemico):
        Damage = Vita - DannoNemico
        return Damage

    def __str__(self):
        return f"Le statistiche del personaggio sono: Vita {self.Vita} - Forza {self.Forza} - Agilità {self.Agilita}"
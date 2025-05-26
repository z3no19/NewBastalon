from abc import ABC

class Cura():
    def __init__(self, Utilizzi: int, NumeroCure: int, CuraEffettiva: int):

        self.Utilizzi = Utilizzi
        self.NumeroCure = NumeroCure
        self.CuraEffettiva = CuraEffettiva

    def GetStat(self, Utilizzi: int, NumeroCure: int, CuraEffettiva: int):
        pass

    def Healing(self, Vita, CuraEffettiva):
        Heal = Vita + CuraEffettiva
        return Heal

    def ScalaUtilizzi(self, Utilizzi):
        Utilizzi-1
        return Utilizzi

    def __str__(self):
        return f"Posso curarmi {self.Utilizzi} volte per {self.CuraEffettiva} punti vita"
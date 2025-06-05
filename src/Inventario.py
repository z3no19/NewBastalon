from abc import ABC
from src.Armi import Arma

class Inventario():
    def __init__(self, Arma1, Arma2, ArmaHolder):

        self.Arma1 = Arma1
        self.Arma2 = Arma2
        self.ArmaHolder = ArmaHolder

    def GetStat(self, Arma1, Arma2):
        pass

    def GetArmaClass (self,Registro,valore):
        ArmaScelta = Registro[valore]
        return ArmaScelta

    def CambioArma(self):
        print("Quale arma vuoi sostituire? X/C")
        user_input = input()
        if user_input == "X":
            self.Arma1 = self.ArmaHolder
            print("arma1 cambiata")
        elif user_input == "C":
            self.Arma2 = self.ArmaHolder
            print("arma2 cambiata")      

    def __str__(self):
        return f"Le mie armi sono {self.Arma1} e {self.Arma2}"
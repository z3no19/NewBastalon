from abc import ABC

class Inventario():
    def __init__(self, Arma1, Arma2, ArmaHolder):

        self.Arma1 = Arma1
        self.Arma2 = Arma2
        self.ArmaHolder = ArmaHolder
   


    def GetStat(self, Arma1, Arma2):
        pass

    def GetArmaHolder(self, ArmaHolder, ArmaID):
        ArmaHolder= ArmaID
        return ArmaHolder

    def CambioArma(self, Arma1, Arma2, ArmaHolder):
        print("Quale arma vuoi sostituire? X/C")
        user_input = input()
        if user_input == "C":
            Arma1 = ArmaHolder
        elif user_input == "X":
            Arma2 = ArmaHolder
            return Arma1, Arma2

    def __str__(self):
        return f"Le mie armi sono {self.Arma1} e {self.Arma2}"
from abc import ABC
import random

class Loot():
    def __init__(self,Arma, Monete):

        self.Arma = Arma
        self.Monete = Monete



    def DropArma(self, ArmaID):
       random_number = random.randint(3, 6)
       ArmaID = random_number
       return ArmaID

    def CambioArma(self, Arma1, Arma2, ArmaHolder):
        pass

    def __str__(self):
        return f"Le mie armi sono {self.Arma1} e {self.Arma2}"
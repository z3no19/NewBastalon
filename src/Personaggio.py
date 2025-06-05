from abc import ABC
from src.Armi import Arma
from src.Inventario import Inventario
from src.Nemico import Nemico
import random

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
    
    def Attacco(self, DannoArma: int, Nemico: Nemico):
        Attacco = (self.Forza * DannoArma)/2
        Nemico.Vita -= Attacco
        print("Vita nemico")
        print(Nemico.Vita)
        Nemico.LifeCheck()

    def RiceviDanno(self, Nemico: Nemico):
        self.Vita -= Nemico.Attacco
        Personaggio.LifeCheck(self)
        print("Vita Giocatore")
        print(self.Vita)

    def Schivata(self,Nemico: Nemico):
        valore = random.randint(0, 100)
        if valore >50:
            print("sculato")
        else:
            self.RiceviDanno(Nemico)

    def Combattimento(self, Arma1: Arma,Arma2: Arma, Nemico: Nemico):
        print("Vuoi attaccare o schivare? Attacca'X' Schiva 'C'")
        user_input = input()
        if user_input == "X":
            print("Con Quale arma vuoi attaccare? Arma 1 'X' o Arma 2 'C'?")
            user_input = input()
            if user_input == "X":
                self.Attacco(Arma1.DannoArma,Nemico)
                self.RiceviDanno(Nemico)
            elif user_input == "C":
                self.Attacco(Arma2.DannoArma,Nemico)
                self.RiceviDanno(Nemico)

        elif user_input == "C":
            self.Schivata(Nemico)
      
    def LifeCheck(self):
        if self.Vita <= 0:
            print("Sei Morto")
            quit()

    def __str__(self):
        return f"Le statistiche del personaggio sono: Vita {self.Vita} - Forza {self.Forza} - Agilità {self.Agilita}"
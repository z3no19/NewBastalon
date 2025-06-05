from abc import ABC
import random

class Loot():
    def __init__(self,Arma, Monete):

        self.Arma = Arma
        self.Monete = Monete



    def DropArma():
        return random.randint(2, 5)
    
    def DropMonete():
        Monete = random.randint(0, 500)
        print("Nemico ha droppato",Monete,"monete")
 
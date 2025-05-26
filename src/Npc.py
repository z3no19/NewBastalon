from abc import ABC

class Npc():
    def __init__(self, ProgressioneStoria: int):

        self.ProgressioneStoria = ProgressioneStoria

    def Interazione(self):
        pass


    def SceltaDialogo(self,ProgressioneStoria):
        pass

    def __str__(self):
        return f"Sono un Npc e posso parlarti del topic {self.ProgressioneStoria}"
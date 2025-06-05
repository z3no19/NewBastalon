from abc import ABC

class Npc():
    def __init__(self, ProgressioneStoria: int):

        self.ProgressioneStoria = ProgressioneStoria

    def Interazione(self):
        print("Vuoi parlare con l'NPC? X per parlare / C per ignorare")
        user_input = input("Scelta: ").upper()
        if user_input == "X":
            return f"Sono un NPC e posso parlarti del topic {self.ProgressioneStoria}"
        elif user_input == "C":
            return "Allora vai a cagare."
        else:
            return "Input non valido. Scegli 'X' o 'C'."


    def SceltaDialogo(self,ProgressioneStoria):
        pass

    def __str__(self):
        return f"Sono un Npc e posso parlarti del topic {self.ProgressioneStoria}"
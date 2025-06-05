from src.Personaggio import Personaggio
from src.Cura import Cura
from src.Armi import Arma
from src.Inventario import Inventario
from src.Nemico import Nemico
from src.Npc import Npc
from src.Oggetti import Oggetti
from src.Loot import Loot

Arma1 = Arma("spada", 60)
Arma2 = Arma("spadone", 60)
Arma3 = Arma("spadino", 60)
Arma4 = Arma("spadetta", 60)
Arma5 = Arma("spadonza", 60)
Arma6 = Arma("spadapim", 60)

ArmaHolder = Arma("---", 0)

Registro = [Arma1, Arma2, Arma3, Arma4, Arma5, Arma6]

Personaggione = Personaggio(100, 2, 10)
Inventarione = Inventario(Arma1,Arma2,ArmaHolder)
Cura = Cura(7,7,20)
Nemico1 = Nemico(100,10,4)
Npc = Npc(1)
Oggetti = Oggetti(1)

#print(Personaggio)
#print(Inventario)
#print(Cura)
#print(Nemico)
#print(Npc)
#print(Oggetti)



while Nemico1.Vita > 0:
    Personaggione.Combattimento(Inventarione.Arma1,Inventarione.Arma2, Nemico1)


print(Inventarione)
print("Hai trovato un'arma nuova!")
Inventarione.ArmaHolder = Inventarione.GetArmaClass(Registro, Loot.DropArma())
Inventarione.CambioArma()
print(Inventarione)


# DannoEffettivo = Personaggio.Attacco(Personaggio.Forza,Arma1.DannoArma)
# print(DannoEffettivo)

# Velocita = Personaggio.Movimento(Personaggio.Agilita)
# #print(Velocita)

# Heal = Cura.Healing(Personaggio.Vita,Cura.CuraEffettiva)
# #print(Heal)

# Personaggio.Vita = Personaggio.RiceviDanno(Personaggio.Vita, Nemico.Attacco(Nemico.Forza))
# #print(Personaggio.Vita)
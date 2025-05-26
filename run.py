from src.Personaggio import Personaggio
from src.Cura import Cura
from src.Inventario import Inventario
from src.Nemico import Nemico
from src.Npc import Npc
from src.Oggetti import Oggetti
from src.Armi import Arma


Arma1 = Arma("spada", 60, 1)
Arma2 = Arma("spadone", 60, 2)
Arma3 = Arma("spadino", 60, 3)
Arma4 = Arma("spadetta", 60, 4)
Arma5 = Arma("spadonza", 60, 5)
Arma6 = Arma("spadapim", 60, 6)

Personaggio = Personaggio(100, 10, 10)
Inventario = Inventario(Arma1,Arma2,0)
Cura = Cura(7,7,20)
Nemico = Nemico(10,10,4)
Npc = Npc(1)
Oggetti = Oggetti(1)




#print(Personaggio)
#print(Inventario)
#print(Cura)
#print(Nemico)
#print(Npc)
#print(Oggetti)

DannoEffettivo = Personaggio.Attacco(Personaggio.Forza,Arma1.DannoArma)
print(DannoEffettivo)

Velocita = Personaggio.Movimento(Personaggio.Agilita)
#print(Velocita)

Heal = Cura.Healing(Personaggio.Vita,Cura.CuraEffettiva)
#print(Heal)

Personaggio.Vita = Personaggio.RiceviDanno(Personaggio.Vita, Nemico.Attacco(Nemico.Forza))
#print(Personaggio.Vita)
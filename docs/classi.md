# CLASSI UTILIZATE

## Qui verranno descritte e classi che interagiranno tra di loro nel corso del gioco


#### PERSONAGGIO

1. Attributi

- Vita (int)
- Forza (int)
- Agilità (int)

2. Funzioni

- GetStat
- Movimento (Agi)
- Attacco (For,Arma)
- Cura
- RiceviDanno


#### NEMICO

1. Attributi

- Vita (int)
- Forza (int)
- Agilità (int)

2. Funzioni

- Movimento (Agi)
- Attacco (For)
- RiceviDanno
- DroppaLoot

#### OGGETTI

1. Attributi

- Vita (int)

2. Funzioni

- RiceviDanno
- DroppaLoot

#### CURA

1. Attributi

- Utilizzi (int)
- NumeroCure (int)
- %_Cura (int)

2. Funzioni

- ScalaUtilizzi
- Potenzia N.Cure
- Potenzia%Cura

#### NPC

1. Attributi

- ProgressioneStoria (int)

2. Funzioni

- Interazione
- SceltaDialogo (Prog. Storia)


#### INVENTARIO

1. Attributi

- Arma1
- Arma2


2. Funzioni

- GetStats
- CambioArma

#### DANNI 

1. Attributi

    - dannoInflitto: int
    - dannoSubito: int

#### ARMI

1. Attributi

    - dannoInflitto: int
    

#### LOOT 

1. Attributi
        - nome: string
        - descrizione: string


#### STATISTICHE GLOBALI  

1. Attributi

    - vita: int
    - Cura: int
    - monete: int

2. Funzione

    - ProgressioneStoria()
    - ModificaStat()
### DIAGRAMMA DI CLASSE
```mermaid
classDiagram 
 class Personaggio {
        - vita: int
        - forza: int
        - agilità: int

        - GetStat()
        - Movimento (Agi)
        - Attacco (For, Arma)
        - Cura()
        - RiceviDanno()
    }

class Inventario {
    - Arma1
    - Arma2
    - GetStats()
    - CambioArma()

}

class Nemico {
    - vita: int
    - forza: int
    - agilità: int
    - Movimento(Agi)
    - Attaccco(For)
    - RiceviDanno()
    - DroppaLoot()
}

class Oggetti {
    - vita: int
    - RiceviDanno()
    - DroppaLoot()
}

class Cura {
    - Utilizzi: int
    - NumeroCure: int
    - %_Cura: int
    - ScalaUtilizzi()
    - Potenzia N.Cure()
    - Potenzia%Cura()

}

class Npc {
    - ProgressioneStoria: int
    - Interazione()
    - SceltaDialogo()
}

class Danni {
    - dannoInflitto: int
    - dannoSubito: int

}
  
class Armi {
        - dannoInflitto: int
    }

class Loot {
        - nome: string
        - descrizione: string
    }

class StatisticheGlobali{
    - vita: int
    - Cura: int
    - monete: int
    - ProgressioneStoria()
    - ModificaStat()

}

Personaggio --|> Inventario :ha
Inventario --|> Armi :contiene
Armi --|> Loot
Loot --|> Inventario : è contenuto
Loot --|> StatisticheGlobali : modifica
Loot <|--|> Nemico : è droppato
Nemico <|--|> Danni
Danni <|--|> Personaggio
Danni <|--|> StatisticheGlobali
Danni --|> Oggetti
StatisticheGlobali --|> Npc : contiene stato
Personaggio --|> Npc : interagisce
Personaggio --|> Cura
Cura --|> StatisticheGlobali
```
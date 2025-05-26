# Requisiti

#### FR1: Controlli e movimento

#### FR2: Interazione con gli NPC

#### FR3: Statistiche e progressione

#### FR4: Inventario ed equipaggiamento

#### FR5: Gestione delle mappe

#### FR6: Gestione delle missioni

#### FR7: User Interface e User Experience

#### FR8: Stato del gioco

#### FR9: Narrativa ed eventi scriptati



### FR1: Controlli e movimento
1. Il sistema deve visualizzare il mondo di gioco da una prospettiva 2D.
2. Il sistema deve permettere al giocatore di controllare il proprio personaggio usando dei dispositivi di input (tastitera o joypad).
3. Il sistema deve permettere al personaggio del giocatore di muoversi in maniera libera all'interno dell'area di gioco.
4. Il sistema deve gestire le collisioni, e le conseguenti interazioni, con l'ambiente circostante e gli NPC.
5. Il sistema deve permettere al personaggio di transitare tra diverse zone della mappa.
6. Il sistema deve essere reattivo alle azioni del personaggio per garantire un'esperienza dinamica.

### FR2: Interazione con gli NPC
1. Il sistema deve popolare il mondo con degli NPC.
2. Il sistema deve permettere ai giocatori di interagire con gli NPC.
3. Il sistema, nel caso l'interazione preveda un dialogo, deve mostrarne il testo in una parte dedicata della UI.
4. Alcuni NPC potranno mostrare schemi di movimento di base (come camminare lungo percorsi predefiniti).
5. Alcuni NPC interagiranno con i giocatori combattendoli.

### FR3: Statistiche e progressione
1. Il sistema avrà Agilità, Forza e Vita come statistiche base.
2. Il sistema dovrà gestire il tipo di ricompense e l'esperienza da assegnare ai giocatori.
3. Il sistema dovrà assegnare le ricompense ai giocatori dopo aver ucciso un nemico.
4. Il sistema dovrà dare dei buff permanenti, relativi all'aspetto platforming del gioco, dopo la sconfitta di un boss.
5. Il sistema dovrà permettere l'apprendimento di nuove abilità da parte dei giocatori, come parte delle ricompense.
6. Il sistema dovrà gestire l'aumento di livello delle abilità.

### FR4: Inventario ed equipaggiamento
1. Il sistema dovrà fornire un inventario che il giocatore userà per conservare gli oggetti raccolti.
2. Il sistema dovrà mostrare l'inventario tramite una schermata dedicata dell'UI.
3. Il sistema dovrà permettere al giocatore di usare oggetti consumabili dall'inventario (sia dentro che fuori dal combattimento).
4. Il sistema dovrà permettere al giocatore di visualizzare le descrizioni e le proprietà degli oggetti.
5. Il sistema dovrà definire slot di equipaggiamento per i personaggi giocanti (es., Arma, Scudo, Testa, Corpo, Accessorio).
6. Il sistema dovrà permettere al giocatore di equipaggiare e rimuovere oggetti negli slot appropriati tramite l'interfaccia utente.
7. Il sistema dovrà modificare le statistiche del personaggio e potenzialmente conferire abilità in base agli oggetti equipaggiati.
8. Il sistema dovrà far rispettare eventuali restrizioni del personaggio sull'equipaggiamento (ad esempio, armi specifiche per classe).

### FR5: Gestione delle mappe
1. Il sistema dovrà essere in grado di generare mappe randomizzate.
2. Il sistema dovrà essere in grado di inserire NPC adeguati per le mappe che genererà.
3. Il sistema dovrà generare la mappa del giorno, ovvero una mappa uguale per tutti che durerà per tutta la giornata.
4. Il sistema dovrà gestire una classifica delle performance nella mappa del giorno basata sul tempo impiegato.
5. Il sistema, nel generare gli NPC, deve generare un boss ogni 5 livelli.

### FR6: Gestione delle missioni
1. Il sistema dovrà essere in grado di generare missioni accessibili interagendo con l'ambiente e/o gli NPC.
2. Il sistema dovrà fornire una schermata per il Registro Missioni, tracciando le missioni attive e completate, e mostrandone obiettivi e descrizioni.
3. Il sistema dovrà tracciare i progressi del giocatore verso gli obiettivi della missione.
4. Il sistema dovrà aggiornare automaticamente lo stato della missione al completamento degli obiettivi.
5. Il sistema dovrà permettere al giocatore di consegnare le missioni completate all’NPC pertinente o, se necessario, completarle in maniera automatica.
6. Il sistema dovrà distribuire le ricompense al completamento della missione.

### FR7: User Interface e User Experience
1. Il sistema dovrà fornire un menu principale all'avvio del gioco.
2. Il sistema dovrà fornire un menu di gioco accessibile durante l'esplorazione.
3. Il sistema dovrà mostrare informazioni essenziali del personaggio sullo schermo durante l'esplorazione (ad esempio, barre per i punti vita e mana semplificate per il capogruppo).
4. Il sistema dovrà mostrare informazioni dettagliate sui personaggi e sui nemici durante il combattimento.
5. Il sistema dovrà fornire un chiaro feedback visivo per azioni, cambiamenti di stato, interazioni ed eventi di combattimento.

### FR8: Stato del gioco
1. Il sistema dovrà permettere al giocatore di salvare i dettagli del progresso nel gioco.
2. Il sistema dovrà permettere il salvataggio ovunque al di fuori di combattimenti o cutscene.
3. Il sistema dovrà permettere al giocatore di caricare uno stato di gioco precedentemente salvato.
4. Il sistema dovrà gestire le impostazioni audio, video, e dei controlli di gioco.

### FR9: Narrativa ed eventi scriptati
1. Il sistema dovrà essere in grado di attivare determinate linee di dialogo o dare accesso a maggiori informazioni su determinati luoghi e/o oggetti in base al progresso del giocatore o in determinate circostanze.
2. Il sistema dovrà mostrare informazioni narrative tramite dialoghi, descrizioni di oggetti, testi delle missioni o libri sulla lore del mondo di gioco.
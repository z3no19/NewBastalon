# CASI D'USO

1. GESTIONE DI UN COMBATTIMENTO

ATTORE: Giocatore

OBBIETTIVO: abbattere i nemici presenti nel livello per ottenere armi e EXP

INNESCO: al trigger di un comando dato dal giocatore il suo personaggio avrà un animazione di attacco che andrà a collidere con la hitbox del nemico

PRECONDIZIONI: il giocatore affronta il livello; I nemici sono visibili sulla mappa.

FLUSSO DI BASE

1. personaggio nemico a schermo
2. interazione tra il personaggio e il nemico a schermo
3. collissione tra l'animazione del personaggio e quella del nemico
4. se il colpo del personaggio va a segno mostrare animazione di danno del nemico di conseguenza diminuire la percentuale di vita
5. se il colpo del nemico va a segno mostrare l'animazione di danno subito e ridurre la percentuale di vita del personaggio e di conseguenza diminuire la percentuale di vita mostrata a schermo
6. se la percentuale di vita del nemico raggiunge lo 0 mostrare a schermo animazione di morte del nemico e conseguentemente eliminare il nemico dalla mappa di gioco
7. alla morte del nemico vengo droppate in modo casuale armi e/o punti exp
8. se eliminati tutti i nemici nella mappa avanzare al prossimo stage e scegliere spendendo punti exp un potenziamento alle statistiche di base 

FLUSSI ALTERNATIVI

1. se la percentuale di vita del personaggio raggiunge 0 mostrare animazione di morte del personaggio
2. alla morte del personaggio riportare il personaggio al hub principale e concludere la run
3. se il giocatore esce dal gioco a metà livello salvare lo stato evella partita , una volta rientrato ricaricare il salvataggio da inizio livello 

2. GESTIONE DELLA PROGRESSIONE


ATTORE: giocatore

OBBIETTIVO: progressione nella storia

INNESCO: completamento del livello con boss

PRECONDIZIONI: aver superato i livelli precedenti; battere il boss.

FLUSSO DI BASE

1. battere il boss quindi superare livello
2. il sistema aggiorna lo stato di progressione della storia
3. interazione tramite la pressione di pulsante apposito con npc nel hub principale
4. il sistema inizializza il dialogo
5. dialogo reso visibile a schermo
6. conclusione dialogo tramite pulsante predefinito
7. sistema aggiorna lo stato della storia a quello attuale

FLUSSI ALTERNATIVI

1. interazione con l'npc senza avanzamento della storia comporta una ripetizione dei punti dal 4 al 6

3. GESTIONE ARSENALE

ATTORE: giocatore

OBBIETTIVO: accumulare armi 

INNESCO: uccisione dei nemici

PRECONDIZIONI: aver iniziato la run e lasciato l'hub principale

FLUSSO DI BASE

1. il personaggio ottiene 2 armi iniziali potenziabili in modo permanente tramite la progressione di gioco
2. armi droppate dai nemici raccoglibili
3. scambiare le armi in possesso con quelle ottenute dai nemici
4. il giocatore sceglie l'arma da scambiare
5. massimo 2 armi trasportabili e utilizzabili per volta
6. agggiornate le statistiche e i moveset del personaggio

FLUSSI ALTERNATIVI

1. il giocatore cerca di equipaggiare più armi di quelle consentite
2. le armi droppate dai nemici vengono perse alla morte
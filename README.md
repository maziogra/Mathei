## Mathei 2.0

### di Oubih Khadija, Shahid Shameer e Gravellu Mattia

Uno strumento molto usato dagli studenti è Photomath, ma spesso non fornisce tutte le informazioni necessarie per svolgere uno studio di funzione completo. Mathei nasce per risolvere questo problema, permette di analizzare una funzione matematica e tracciarne il grafico, tutto questo in modo chiaro e immediato.

Questo progetto verrà presentato al "Politekne Mattei 2026"


Known issues:
- intersections non funziona con le gonio, c'è bisogno di un periodo a cui fare riferimento (findNearestPeriod)
- findSolution è troppo impreciso, da valutare la rimozione e la sostituzione con un metodo che risolva ad esempio ln(x) + x = 0 (solo 2 addendi)
- findNearestPeriod dovrebbe solo trovare il pediodo di riferimento, la funzione attualmente non dà problemi, tuttavia andrebbe divisa in due, delegando la ricerca dei punti critici

"""
    Dato che per questo non possiamo perdere tempo a lezione, se volete fare un bell'esercizio su cicli, liste e condizionali,
    vi propongo un esercizio classico: TicTacToe o gioco del Tris. 
    Normalmente il campo di gioco è una lista di liste con valori vuoti. Registrarli al suo interno, diventa necessario(se vogliamo
    che il tutto resti "semplice") per il lavoro di verifica che andrà fatto ad ogni inserimento
"""


square = [["","",""],["","",""],["","",""]]
 
# con il seguente ciclo for, joinando il contenuto di ogni riga tramite | e sostituendo eventuali caratteri vuoti
# (solo in fase di PRINT!!! Square non viene modificato da questo ciclo!!!), otterremo la griglia.  

for row in square:

    print("|".join([" " if not cell else cell for cell in row]))

# questa una piccola facility. ogni volta che chiamerete square_visualize(), otterrete la griglia aggiornata.
# Si basa sul ciclo for scritto precedentemente. Si limita ad inserire le stringhe(questa volta realmente modificate,
# ma non conservate in nessuna variabile poichè restituite dalla funzione) in un'unica stringa joinata con \n.
# Per utilizzarla durante l'esecuzione del programma, non dimenticate di fare il run sulla cella.
   
def square_visualize(square):

    print("\n".join(["|".join([" " if not cell else cell for cell in row]) for row in square]))

#per comprendere cosa fa questa funzione, sotto trovate tutto.

#Questo è ciò che avviene in "\n".join(["|".join([" " if not cell else cell for cell in row]) for row in square])

sample1 = [
            ["", "X", ""], ["O", "", "O"], ["", "", ""]
        ]

# questo ciclo itera lungo le liste in sample1. Al suo interno, ogni volta che incrementa, viene dichiarata una lista vuota.
# è quella che conterrà i caratteri trovati all'interno della griglia. 

for row in sample1:

    print("row",row)
    new_row = []

    # a questo punto bisogna verificare il contenuto di ogni "cella". Si inizia dunque un ciclo for annidato che iteri lungo 
    # row. Ad ogni cella, se il contenuto è "" , verrà sostituito con uno spazio(permette alla tabella di essere formattata
    # rispettando gli spazi), altrimenti con il carattere trovato(X,O). I print statement inseriti sono solo a scopo indicativo
    # e servono solo come conferma visiva di ciò che sta avvenendo.
        
    for index, cell in enumerate(row):

        print(f"contenuto cella {index}:|{cell}|")    
        if not cell:

            new_row.append(" ")
        else:
            
            new_row.append(cell)    

# che meraviglia enumerate()!!!!!! E' semplicissima, praticissima e vi aiuta a controllare l'indexing.

sample2 = [[1,2,3], [4,5,6], [7,8,9]]

for row in enumerate(sample2):

    print("row:",row)

print("enumerate da un'indice ad ogni elemento su cui itera e lo inserisce in una tupla dove è contenuto l'elemento analizzato")

# si può pensare di separare i due valori contenuti nella tupla di "enumerate" ed iterare nel modo seguente

for index,row in enumerate(sample2):

    print(index, row)

# separando i due valori, fare controlli condizionali verrà molto più semplice, e renderà l'indexing meno macchinoso 

""" 
    il gioco verrà eseguito da terminale(pensare di implementare un'interfaccia grafica sarebbe assai prematuro)
    e l'inserimento avverrà da tastiera tramite input.
    1|2|3               ad ogni tasto corrisponderà una cella. 
    4|5|6               al tasto 1 corrisponderà la cella [0][0]
    7|8|9               al tasto 2 corrisponderà la cella [0][1]
                        etc etc
    Ma come unire inserimento numero e posizione nel quadrato???
    Ci sono vari modi per affrontare il problema ma in questo caso possono venirci in aiuto i dizionari:
"""
positions = {
                "1" : [0,0],
                "2" : [0,1],
                "3" : [0,2],
                "4" : [1,0],
                "5" : [1,1],
                "6" : [1,2],
                "7" : [2,0],
                "8" : [2,1],
                "9" : [2,2]
            }


sample3 = [["","",""], ["","",""], ["","",""]]
square_visualize(sample3)
sample_choice = input("choose an empty cell and press enter: ")

# per andare ad inserire il segnaposto nella griglia, basterà risalire alla posizione tramite il dizionario positions. 
# per questa implementazione ho deciso di mantenere il formato di inserimento come stringa e di non utilizzare chiavi 
# del dizionario come "int". In teoria non è la scelta migliore, ma volevo evitare al codice di farmi eseguire una 
# operazione di conversione(entrambi gli approcci comunque, a seconda dei contesti, hanno vantaggi e svantaggi).
# come per la funzione enumerate(), posso distribuire i valori di una lista più grande in variabi effettuando
# l'operazione di "unpacking"(che non è semplice come sembra).

# la lista correlata al valore inserito dall'utente, contiene due valori che possono "spacchettati" nelle coordinate
# X, Y

x, y = positions[sample_choice]

# avendo utilizzato il formato stringa come formato per l'inserimento(al fine di rendere l'implementazione
# quanto più semplice possibile), basterà sommare la stringa vuota contenuta nella cella selezionata 
# alla stringa segnaposto.

sample3[x][y] += "X"

square_visualize(sample3)

# ma come gestire l'inserimento dei segnaposto e la loro turnazione???
# WHILE è la risposta.

# creando una variabile turno, incrementandola e confrontandola con l'operatore modulo (%) saremo
# in grado di verificare se il turno è un turno pari o un turno dispari e così, assumendo che 
# giocatore X sia il primo, otterremo un'alternanza di X e O 

turno_sample = 0

while turno_sample < 9:

    player = ""
    
    if turno_sample % 2 == 0:
        
        player = "X"
    else:
        player = "0"
    
    print(f"turno {turno_sample}, player {player}")         
        
    turno_sample += 1

    
"""

    scopriremo più avanti che :

    player = ""
    
    if turno_sample % 2 == 0:
        
        player = "X"
    else:
        player = "0"   



    può semplicemente scriversi:

    player = "X" if turno_sample % 2 == 0 else "0"

"""

"""
    Ci siamo quasi. Inserendo tutti i concetti affrontati fin'ora nella funzione while avremo un turno che parte da zero
    ed incrementa sino a 8, un campo imput che acquisirà la posizione tramite dizionario ed andrà ad inserire il segnaposto.
    Qua sotto, un esempio su tre turni. Inserite solo numeri differenti tra loro, ancora il codice non è in grado di fare 
    verifiche sugli inserimenti.
"""

turno = 0
sample4 = [["","",""], ["","",""], ["","",""]] 

while turno < 3:

    player = "X" if turno % 2 == 0 else "O"
    choice = input("choose an empty cell and press enter : ")
    x, y = positions[choice]
    sample4[x][y] = player
    square_visualize(sample4)
    turno += 1

        

    

#print(square_visualize())  




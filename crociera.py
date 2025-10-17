
import operator
from passeggero import Passeggero
from cabina import Cabina
from cabina_deluxe import CabinaDeluxe
from cabina_animali import CabinaAnimali

class Crociera: # inizializza la classe crociera
    def __init__(self, nome):
        self._nome = nome # inizializza l'attributo privato nome con il nome precedente
        self.passeggeri = [] # inizializza la lista dei passeggeri come lista vuota
        self.cabine = [] # inizializza la lista delle cabine come lista vuota
        """Inizializza gli attributi e le strutture dati"""
        # TODO

    @ property # metodo getter per ottenere il nome della crociera
    def nome(self):
        return self._nome

    @nome.setter # metodo setter per impostare in maniera controllata il nuovo nome della crociera
    def nome(self, valore):
        if valore != "":
            self._nome = valore


    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        try:
            from csv import reader
            with open(file_path, "r", encoding="utf-8") as infile: # apre il file
                csv_reader = reader(infile) # trasforma la riga in una lista
                for row in csv_reader: # itera su ogni riga
                    if len(row) == 3: # se la lista presenta 3 elementi: crea passeggero
                        codice_passeggero = row[0]
                        nome = row[1]
                        cognome = row[2]
                        passeggero = Passeggero (codice_passeggero, nome, cognome) # crea l'oggetto passeggero usando i valori letti nel file
                        self.passeggeri.append(passeggero) # aggiunge l'oggetto alla lista dei passeggeri
                    elif len(row) == 4: # se la lista presenta 4 elementi: crea cabina standard
                        codice_cabina = row[0]
                        num_letti = int(row[1])
                        ponte = int(row[2])
                        prezzo = int(row[3])
                        cabina = Cabina(codice_cabina,num_letti,ponte,prezzo) # crea l'oggetto cabina usando i valori letti nel file
                        self.cabine.append(cabina) # aggiunge l'oggetto alla lista delle cabine
                    else:
                        codice_cabina = row[0] # se la lista presenta più di 4 elementi: controlla il tipo di cabina
                        num_letti = int(row[1])
                        ponte = int(row[2])
                        prezzo = int(row[3])
                        extra = row[4] # valore in aggiunta alla cabina standard
                        try:
                            num_animali= int(extra) # controlla se è un numero intero e gli assegna il valore num_animali
                            cabina = CabinaAnimali(codice_cabina, num_letti, ponte, prezzo, num_animali) # crea l'oggetto
                        except ValueError: # se non può essere convertito ad un intero
                            tipologia = extra # valore della cabina deluxe
                            cabina = CabinaDeluxe(codice_cabina,num_letti,ponte,prezzo,tipologia) # crea l'oggetto
                        self.cabine.append(cabina) # aggiunge le cabine "speciali" alla lista delle cabine

        except FileNotFoundError:
            print("File non trovato ")


        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        trovato = False # controlla che il codice della cabina selezionata sia presente nella lista delle cabine
        for cabina in self.cabine: # controlla per ogni oggetto della lista
            if cabina.codice_cabina == codice_cabina: # confronta i codici usando la funzione __eq__() definita nella classe Cabina
                trovato = True
                break # una volta trovata l'uguaglianza esce dal ciclo
        if not trovato:
            raise Exception("Il codice della cabina selezionata non esiste")
        if not cabina.disponibile: # controlla che la cabina sia disponibile
            raise Exception("la cabina selezionata non è attualmente disponibile")
        presente = False # controlla che il codice del passeggero esista nella lista dei passeggeri
        for passeggero in self.passeggeri: # per ogni oggetto della lista
            if passeggero.codice_passeggero == codice_passeggero:
                presente = True
                break
        if not presente: # se non è presente il codice del passeggero nella lista scatena l'eccezione
            raise Exception("Il codice del passeggero selezionato non esiste")
        if passeggero.cabina not in ("", None): # se non è stata assegnata nessuna cabina al passeggero,scatena l'eccezione
            raise Exception ("Il passeggero selezionato ha già una cabina associata")

        passeggero.associa_cabina(codice_cabina) # associa il codice della cabina al passeggero
        cabina.occupa_cabina() # segnala che la cabina non è più disponibile con la funzione definita nella classe Cabina

        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        cabine_ordinate  = sorted((self.cabine),key = operator.attrgetter("prezzo")) # usa la funzione sorted, ma ci sono altri metodi
        return cabine_ordinate
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        elenco_passeggeri = []
        for passeggero in self.passeggeri:
            nome = passeggero.nome
            if passeggero.cabina != "":
                cabina = passeggero.cabina
                elenco_passeggeri.append((nome, cabina)) # aggiunge alla lista le tuple nome passeggero - cabina
            else:
                elenco_passeggeri.append((nome, "Nessuna")) # se il passeggero non ha nessuna cabina stampa nessuna
        print(elenco_passeggeri)

        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO



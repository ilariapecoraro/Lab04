from cabina import Cabina


class CabinaDeluxe(Cabina):
    def __init__(self, codice_cabina, num_letti, ponte, prezzo, tipologia): # inizializza la classe CabinaDeluxe
        super().__init__(codice_cabina, num_letti, ponte, prezzo) # richiama i metodi della classe Cabina
        self.tipologia = tipologia
        self.prezzo = self.prezzo * 1.20  # modifica il prezzo base letto nel file

    def __str__(self):
        if self.disponibile:  # controlla se disponibile
            return f"{self.codice_cabina}: {self.tipologia} | {self.num_letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo} - Disponibile "
        else:
            return f"{self.codice_cabina}: {self.tipologia} | {self.num_letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo} - Non disponibile "

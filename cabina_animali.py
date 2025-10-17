from cabina import Cabina


class CabinaAnimali(Cabina):

    def __init__(self, codice_cabina, num_letti, ponte, prezzo, num_animali): # inizializza la classe CabinaAnimali
        super().__init__(codice_cabina, num_letti, ponte, prezzo) # richiama i metodi della classe genitore
        self.num_animali = num_animali
        self.prezzo = self.prezzo + 1 + (0.10 * self.num_animali) # modifica il prezzo base letto nel file

    
    def __str__(self):
        if self.disponibile:
            return f"{self.codice_cabina}: Animali | {self.num_letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo} - Max animali: {self.num_animali} - Disponibile "
        else:
            return f"{self.codice_cabina}: Animali | {self.num_letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo} - Max animali: {self.num_animali} - Non disponibile "


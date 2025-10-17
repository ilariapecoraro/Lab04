class Cabina:
    def __init__(self,codice_cabina, num_letti, ponte, prezzo): # inizializa la classe Cabina
        self.codice_cabina = codice_cabina
        self.num_letti = num_letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.disponibile = True  # inizializza la cabina come disponibilE

    
    def __str__(self):
        if self.disponibile:
            return f"{self.codice_cabina} | {self.num_letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo} - Disponibile "
        else:
            return f"{self.codice_cabina} | {self.num_letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo} - Non disponibile "

    def __eq__(self, other): # metodo per confrontare due oggetti
        return self.codice_cabina == other.codice_cabina


    def occupa_cabina(self): # rende la cabina non più disponibile
        self.disponibile = False







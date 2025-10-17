class Passeggero:
    def __init__(self,codice_passeggero,nome,cognome): # inizializza la classe Passeggero
        self.codice_passeggero = codice_passeggero
        self.nome = nome
        self.cognome = cognome
        self.cabina = "" # la inizializza con una stringa vuota

    def __str__(self):
        return f"{self.codice_passeggero}, {self.nome}, {self.cognome}"

    def associa_cabina(self,id_cabina): # metodo per associare una cabina al passeggero
        self.cabina = id_cabina

    def __eq__(self, other): # metodo per confrontare due oggetti e stabilire in base a quali attributi sono uguali
        return self.codice_passeggero == other.codice_passeggero



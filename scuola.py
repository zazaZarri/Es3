from studente import Studente

class Scuola:
    def __init__(self, nome):
        self.nome = nome
        self.studenti = []

    def aggiungi_studente(self, studente):
        self.studenti.append(studente)

    def conta_studenti(self):
        return len(self.studenti)

    def cerca_per_cognome(self, cognome):
        risultati = []
        for s in self.studenti:
            if cognome.lower() in s.cognome.lower():
                risultati.append(s)
        return risultati

    def cerca_per_eta(self, eta):
        risultati = []
        for s in self.studenti:
            if s.eta == eta:
                risultati.append(s)
        return risultati
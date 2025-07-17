import time

class Cronometro:
    def __init__(self):
        self.inizio = None
        self.fine = None
        self.attivo = False

    def start(self):
        if not self.attivo:
            self.inizio = time.time()
            self.attivo = True
            print("Cronometro avviato.")
        else:
            print("Il cronometro è già in funzione.")

    def stop(self):
        if self.attivo:
            self.fine = time.time()
            self.attivo = False
            tempo_trascorso = self.fine - self.inizio
            print(f"Cronometro fermato. Tempo trascorso: {tempo_trascorso:.2f} secondi.")
        else:
            print("Il cronometro non è avviato.")

    def reset(self):
        self.inizio = None
        self.fine = None
        self.attivo = False
        print("Cronometro resettato.")
# bank.py – Stand nach Sicherung 4.B
class Kunde:
    def __init__(self, kundennummer, name, vorname, geburtsdatum):
        self.kundennummer = kundennummer
        self.name = name
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum


class Konto:
    def __init__(self, kontonummer, pin):
        self.kontonummer = kontonummer
        self.pin = pin
        self.kontostand = 0.0
        self.dispo = 500.0

# prototyp.py – erster Prototyp der Kontoverwaltung der WarnowBank
# Ausgabe vor Etappe 2.A. Die Schülerinnen und Schüler benutzen den Code nur,
# sie müssen ihn noch nicht verstehen. Die Abweichungen von der Anforderung
# (Version 2) sind beabsichtigt und werden in 2.4 und 4.1 untersucht.

class Kunde:
    def __init__(self, kundennummer, name, vorname, geburtsdatum):
        self.kundennummer = kundennummer
        self.name = name
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum


class Konto:
    def __init__(self, kontonummer, pin, kontostand, inhaber):
        self.kontonummer = kontonummer
        self.pin = pin
        self.kontostand = kontostand
        self.dispo = 500.0
        self.inhaber = inhaber

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

    def abheben(self, betrag):
        self.kontostand = self.kontostand - betrag

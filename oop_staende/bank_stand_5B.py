# bank.py – Stand nach Sicherung 5.B
class Kunde:
    def __init__(self, kundennummer, name, vorname, geburtsdatum):
        self.kundennummer = kundennummer
        self.name = name
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum

    def get_kundennummer(self):
        return self.kundennummer

    def get_name(self):
        return self.name

    def get_vorname(self):
        return self.vorname

    def get_geburtsdatum(self):
        return self.geburtsdatum

    def set_name(self, neuer_name):
        self.name = neuer_name

    def daten_drucken(self):
        print("Kundennummer:", self.kundennummer)
        print("Name:", self.vorname, self.name)
        print("Geboren am:", self.geburtsdatum)


class Konto:
    def __init__(self, kontonummer, pin):
        self.kontonummer = kontonummer
        self.pin = pin
        self.kontostand = 0.0
        self.dispo = 500.0

    def get_kontonummer(self):
        return self.kontonummer

    def get_kontostand(self):
        return self.kontostand

    def pin_pruefen(self, eingabe):
        return eingabe == self.pin

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

    def abheben(self, betrag):
        if self.kontostand - betrag >= -self.dispo:
            self.kontostand = self.kontostand - betrag
        else:
            print("Abhebung abgelehnt: Der Dispo reicht nicht aus.")

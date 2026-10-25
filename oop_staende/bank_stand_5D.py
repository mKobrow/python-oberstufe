# bank.py – Stand nach Abschluss von Baustein 5
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
        self.buchungen = []

    def get_kontonummer(self):
        return self.kontonummer

    def get_kontostand(self):
        return self.kontostand

    def pin_pruefen(self, eingabe):
        return eingabe == self.pin

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand = self.kontostand + betrag
            self.buchungen.append(betrag)
        else:
            print("Einzahlung abgelehnt: Der Betrag muss positiv sein.")

    def abheben(self, betrag):
        if betrag <= 0:
            print("Abhebung abgelehnt: Der Betrag muss positiv sein.")
        elif self.kontostand - betrag >= -self.dispo:
            self.kontostand = self.kontostand - betrag
            self.buchungen.append(-betrag)
        else:
            print("Abhebung abgelehnt: Der Dispo reicht nicht aus.")

    def ueberweisen(self, betrag, zielkonto):
        if betrag <= 0:
            print("Überweisung abgelehnt: Der Betrag muss positiv sein.")
        elif self.kontostand - betrag >= -self.dispo:
            self.kontostand = self.kontostand - betrag
            self.buchungen.append(-betrag)
            zielkonto.einzahlen(betrag)
        else:
            print("Überweisung abgelehnt: Der Dispo reicht nicht aus.")

    def auszug_drucken(self):
        print("Kontoauszug für Konto", self.kontonummer)
        for buchung in self.buchungen:
            print(buchung, "€")
        print("Kontostand:", self.kontostand, "€")


# Testablauf aus Aufgabe 2.3
kunde1 = Kunde(4711, "Lehmann", "Jan", "14.05.1988")
konto1 = Konto(987654321, "1234")
konto2 = Konto(65193275, "0815")
konto1.einzahlen(2020)
konto2.einzahlen(340)
konto1.abheben(50)
konto1.ueberweisen(120, konto2)
konto1.abheben(2400)
konto1.auszug_drucken()

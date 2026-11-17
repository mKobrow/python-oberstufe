# bank.py – Stand nach Abschluss von Baustein 5 (Datenkapselung)
class Kunde:
    def __init__(self, kundennummer, name, vorname, geburtsdatum):
        self.__kundennummer = kundennummer
        self.__name = name
        self.__vorname = vorname
        self.__geburtsdatum = geburtsdatum

    def get_kundennummer(self):
        return self.__kundennummer

    def get_name(self):
        return self.__name

    def get_vorname(self):
        return self.__vorname

    def get_geburtsdatum(self):
        return self.__geburtsdatum

    def set_name(self, neuer_name):
        if neuer_name != "":
            self.__name = neuer_name
        else:
            print("Der Name darf nicht leer sein.")

    def daten_drucken(self):
        print("Kundennummer:", self.__kundennummer)
        print("Name:", self.__vorname, self.__name)
        print("Geboren am:", self.__geburtsdatum)


class Konto:
    def __init__(self, kontonummer, pin):
        self.__kontonummer = kontonummer
        self.__pin = pin
        self.__kontostand = 0.0
        self.__dispo = 500.0
        self.__buchungen = []

    def get_kontonummer(self):
        return self.__kontonummer

    def get_kontostand(self):
        return self.__kontostand

    def set_pin(self, neue_pin):
        if len(neue_pin) == 4 and neue_pin.isdigit():
            self.__pin = neue_pin
        else:
            print("PIN abgelehnt: Die PIN muss aus genau vier Ziffern bestehen.")

    def pin_pruefen(self, eingabe):
        return eingabe == self.__pin

    def einzahlen(self, betrag):
        if betrag > 0:
            self.__kontostand = self.__kontostand + betrag
            self.__buchungen.append(betrag)
        else:
            print("Einzahlung abgelehnt: Der Betrag muss positiv sein.")

    def abheben(self, betrag):
        if betrag <= 0:
            print("Abhebung abgelehnt: Der Betrag muss positiv sein.")
        elif self.__kontostand - betrag >= -self.__dispo:
            self.__kontostand = self.__kontostand - betrag
            self.__buchungen.append(-betrag)
        else:
            print("Abhebung abgelehnt: Der Dispo reicht nicht aus.")

    def ueberweisen(self, betrag, zielkonto):
        if betrag <= 0:
            print("Überweisung abgelehnt: Der Betrag muss positiv sein.")
        elif self.__kontostand - betrag >= -self.__dispo:
            self.__kontostand = self.__kontostand - betrag
            self.__buchungen.append(-betrag)
            zielkonto.einzahlen(betrag)
        else:
            print("Überweisung abgelehnt: Der Dispo reicht nicht aus.")

    def auszug_drucken(self):
        print("Kontoauszug für Konto", self.__kontonummer)
        for buchung in self.__buchungen:
            print(buchung, "€")
        print("Kontostand:", self.__kontostand, "€")


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

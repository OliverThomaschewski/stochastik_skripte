from utils import combinatorics

"""
PERMUTATION OHNE WIEDERHOLUNG
    Anordnung von n Objekten, die alle unterscheidbar sind

    Beispiel: Kombinationsmöglichkeiten von CDs im Regal

    n!

    type = "p"

VARIATION OHNE WIEDERHOLUNG
    k aus n Objekten unter Beachtung der Reihenfolge. Jedes Objekt darf nur einmal ausgewählt werden (ohne zurücklegen).
    Beispiel: 10(n) Teilnehmer bei einem Wettrennen, wieviele Möglichkeiten der Top3(k) gibt es?

    n!
    -----
    (n-k)!

    type = "vo"

    Achtung: 

VARIATION MIT WIEDERHOLUNG
    k aus n Objekten unter der Beachtung der Reihenfolge. Objekte können auch mehrfach vorkommen (mit zurücklegen).

    Beispiel:   Passwörter mit 3(k) Stellen und den Zahlen 0-1 (n = 10)
                10 Lieder in einer Playlist mit 4 Plätzen, Lied darf mehrfach vorkommen

    n^k

    type = "vm"

KOMBINATION OHNE WIEDERHOLUNG
    k aus n Objekten ohne Beachtung der Reihenfolge. Jedes Objekt darf nur einmal ausgewählt werden (ohne zurücklegen).
    Beispiel:    Urne mit 5(n) verschiedenfarbigen Kugeln, es werden 3(k) Kugeln gezogen.
                 3 verschiedene Kugeln aus 40 verschiedenen Eissorten (Weil 3 Kugeln unterschiedlich angeordent werden können werden diese "zusätzlichen" Kombinationen rausgerechnet)

    ( n )       Klammer geht um n und k
      k  
    type = "ko"


KOMBINATION MIT WIEDERHOLUNG
    k aus n Objekten ohne Beachtung der Reihenfolge. Objekte dürfen mehrfach vorkommen (mit zurücklegen)
    Beispiel:   Urne mit 5(n) verschieden Kugeln, es werden 3(k) Kugeln ohne der Beachtung der Reihenfolge mit zurücklegen gezogen
               
    
    (n+k-1)
    -------
       k

    type = "km"


"""
#Gesamtmenge
n = 6

#Objekte die gezogen werden
k = 2
type = "km"

combinatorics(n,k,type)
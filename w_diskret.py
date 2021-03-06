from utils import diskret

"""
Bernoulli - Experiment
    - Experiment, bei dem Ereignis A mit Wahrscheinlich p eintritt oder nicht
    - A tritt ein = Erfolg, A tritt nicht ein = Misserfolg
    - p = P(A) Erfolgswahrscheinlichkeit, q = 1-p Misserfolg

Bernoulli -Verteilung
    Mit Welcher Wahrscheinlichkeit tritt ein Erfolg bei einem Versuch ein?

    den Wert 0 ( Misserfolg) annimmt, heißt Bernoulli-verteilt: 
    X ~ Ber(p)

    type = "ber"


    p = Erfolgswahrscheinlichkeit


Bernoulli - Kette
    Wird ein Bernoulli-Experiment n mal ausgeführt, spricht man von einer Bernoulli Kette

Geometrische Verteilung
    Wartezeit bis zum ersten Erfolg
    X ~ geom(p)

    type = "geom"

    n: Anzahl Versuche
    k: Nicht nötig, da nur bis zum ersten Erfolgreichen Versuch gerechnet wird
    p: Erfolgswahrscheinlichkeit eines Versuchs


Binomialverteilung
    Mit welcher Wahrscheinlichkeit treten k Erfolge in n Versuchen ein.
    X ~ Bin(n,p)

    n: Anzahl Versuche
    k: Anzahl Erfolge
    p: Erfolgswahrscheinlichkeit eines Versuchs

    type = "bin"

    Bei "weniger als 3 versuchen" muss eine 2 eingegeben werden
    

Poissonverteilung
    Anzahl der Vorkommnisse in einem (Zeit) Intervall
    X ~ Po(lambda)

    type = "po"

    lam: Auftrittsrate (lambda)
    k: Anzahl der Ankünfte




Method:

    P(X = 3): pmf
    P(X <= 3):cdf Achtung: kleiner GLEICH
    P(X > 3): sf

    

"""

type = "po"
method = "pmf"
n = 5
k = 7
p = 0.7
lam = 7


diskret(n,k,p,lam,type,method)




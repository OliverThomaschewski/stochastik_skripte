from scipy.stats import uniform

from utils import stetig

"""
Berechnungen mit stetigen Zufallsvariablen

Wichtig: Die Wahrscheinlichkeit, dass X genau einen Wert annimmt, ist immer 0


Gleichverteilung

    type : "gv"
    a = minimaler Wert
    b = maximaler Wert
    c = gesuchter Wert

    

Exponentialverteilung
    Beschreibt die Zeit zwischen zwei Ereignissen.
    Wahrscheinlichkeit bis zur ersten Ankunft?

    type = "exp"
    c = gesuchter Wert
    lam = Ankunftsrate

    Lambda gegeben

Normalverteilung
    N(erwart, std)
    erwart = Erwartungswert
    std = Standardabweichung
    c = Gesuchter Wert


METHOD
P(X <= 3) = cdf
P(X > 3) = sf
x(quantil) = ppf Für Normalverteilung?
"""

type = "exp"
method = "cdf"

a = 5
b = 300
c = 1
std = 7.17
erwart = 180.3
lam = 0.5



stetig(c,a,b, erwart, std,lam, method,type)
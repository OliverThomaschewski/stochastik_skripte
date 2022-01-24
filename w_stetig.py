from scipy.stats import uniform

from utils import stetig

"""
Berechnungen mit stetigen Zufallsvariablen

Wichtig: Die Wahrscheinlichkeit, dass X genau einen Wert annimmt, ist immer 0


Gleichverteilung

a = minimaler Wert
b = maximaler Wert
c = gesuchter Wert

type : "gv"

Exponentialverteilung
Beschreibt die Zeit zwischen zwei Ereignissen.

lam = Ankunftsrate

type = "exp"
c = gesuchter Wert

Lambda gegeben

Normalverteilung

Standardnormalverteilung




METHOD
P(X <= 3) = cdf
P(X > 3) = sf
"""

type = "exp"
method = "sf"

a = 5
b = 300
c = 12
lam = 18



stetig(c,a,b,lam, method,type)
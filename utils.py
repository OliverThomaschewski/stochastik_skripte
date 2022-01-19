import numpy as np
from scipy import stats, special
from matplotlib import pyplot as plt

import math

"""
This class contains Methods for statistical evaluations
"""


def show_basics(values):
    """
        Prints basic statistical values
        :param values: List with numbers
    """
    print("")
    print(f"WERT \t\t\tMETHODE \t\t\tERGEBNIS")
    print("________________________________________________________________________________________________________")
    print(f"Max \t\t\tmax(values) \t\t\t{max(values)}")
    print(f"Min \t\t\tmin(values) \t\t\t{min(values)}")
    print(f"Modalwert \t\tstats.mode() \t\t\t{stats.mode(values)}")
    print(f"Arithmetische Mittel \tnp.mean() \t\t\t{np.mean(values)}")
    print(f"Median \t\t\tnp.median() \t\t\t{np.median(values)}")
    print(f"90% Quantil \t\tnp.quantile(list, 0.9) \t\t{np.quantile(values, 0.9)}")
    print(f"75% Quartil \t\tnp.quantile(list, 0.75) \t{np.quantile(values, 0.75)}")
    print(f"50% Quartil \t\tnp.quantile(list, 0.5) \t\t{np.quantile(values, 0.5)}")
    print(f"25% Quartil \t\tnp.quantile(list, 0.25) \t{np.quantile(values, 0.25)}")
    print(f"10% Quantil \t\tnp.quantile(list, 0.1) \t\t{np.quantile(values, 0.1)}")
    print(f"Varianz \t\tnp.var(list) \t\t\t{np.var(values)}")
    print(f"Standardabweichung \tnp.std(list) \t\t\t{np.std(values)}")
    print(f"Interquartilsabstand \tstats.iqr() \t\t\t{stats.iqr(values)}")
    print(f"Spannweite \t\tmax(values) - min(values) \t{max(values) - min(values)}")

def combinatorics(n, k, type):

    if type == "p":
        print(f"Permutation ohne Wiederholung: n! {math.factorial(n)}")
    elif type == "vo":
        print(f"Variation ohne Wiederholung: n!/(((n-k)!) {math.factorial(n)/math.factorial(n-k)}")
    elif type == "vm":
        print(f"Variation mit Wiederholung n^k {math.pow(n,k)}")
    elif type == "ko":
        print(f"Kombination ohne Wiederholung special.binom(n,k) {special.binom(n, k)}")
    elif type == "km":
        print(f"Kombination mit Wiederholung special.binom(n+k-1,k) {special.binom(n+k-1, k)}")

def korr_scatter(a,b):
    """
        Rechnet Korrelationskoeffizient und zeichnet scatterplot
        :param a: liste 1
        :param b: liste 2
    """
    print(f"Korrelationskoeffizient np.corrcoef(a,b) {np.corrcoef(a,b)[0][1]}")
    plt.scatter(a,b)
    plt.show()

    
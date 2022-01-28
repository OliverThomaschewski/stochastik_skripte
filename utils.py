from xml.sax.handler import property_interning_dict
import numpy as np
import pandas as pd
from scipy import stats, special
from matplotlib import pyplot as plt
from scipy.stats import geom
from scipy.stats import bernoulli
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import uniform, expon, norm

import math

"""
This class contains Methods for statistical evaluations
"""


def show_basics(values):
    """
        Prints basic statistical values
        :param values: List with numbers
        :returns: None
    """
    print("")
    print(f"WERT \t\t\tMETHODE \t\t\t\t\tERGEBNIS")
    print("________________________________________________________________________________________________________")
    print(f"Max \t\t\tmax(values) \t\t\t\t\t{max(values)}")
    print(f"Min \t\t\tmin(values) \t\t\t\t\t{min(values)}")
    print(f"Modalwert \t\tstats.mode() \t\t\t\t\t{stats.mode(values)}")
    print(f"Arithmetische Mittel \tnp.mean() \t\t\t\t\t{np.mean(values)}")
    print(f"Median \t\t\tnp.median() \t\t\t\t\t{np.median(values)}")
    x90 = np.quantile(values, 0.9, interpolation ="higher" )
    x75 = np.quantile(values, 0.75, interpolation ="higher" )
    x50 = np.quantile(values, 0.5, interpolation ="higher" )
    x25 = np.quantile(values, 0.25, interpolation ="higher" )
    x10 = np.quantile(values, 0.1, interpolation ="higher" )
    print(f"90% Quantil \t\tnp.quantile(list, 0.9, interpolation =higher) \t{x90}")
    print(f"75% Quartil \t\tnp.quantile(list, 0.75, interpolation =higher) \t{x75}")
    print(f"50% Quartil \t\tnp.quantile(list, 0.5, interpolation =higher) \t{x50}")
    print(f"25% Quartil \t\tnp.quantile(list, 0.25, interpolation =higher) \t{x25}")
    print(f"10% Quantil \t\tnp.quantile(list, 0.1, interpolation =higher) \t{x10}")
    print(f"Varianz \t\tnp.var(list) \t\t\t\t\t{np.var(values)}")
    print(f"Standardabweichung \tnp.std(list, ddof = 1) \t\t\t\t{np.std(values, ddof = 1)}")
    print(f"Interquartilsabstand \tstats.iqr() \t\t\t\t\t{stats.iqr(values)}")
    print(f"Spannweite \t\tmax(values) - min(values) \t\t\t{max(values) - min(values)}")

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

def haeufigkeit(data):
    """
    Berechnet und zeichnet absolute und relative Häufigkeiten
    :param data: Liste mit Werten
    """

    df = pd.DataFrame(data).value_counts().rename_axis("Wert").reset_index(name = "Absolute Häufigkeit")

    df["Relative Häufigkeit"] = df["Absolute Häufigkeit"]/len(data)
    df = df.sort_values(by= "Wert")
    df["Werte für Verteilungsfunktion"] = df["Relative Häufigkeit"].cumsum()
    print("")
    print(df.to_string(index = False))


    plot1 = plt.figure(1)
    plt.title("Absolute Häufigkeiten")
    plt.xlabel("Werte")
    plt.ylabel("Häufigkeit")
    plt.bar(df["Wert"], df["Absolute Häufigkeit"])

    plot2 = plt.figure(2)
    plt.title("Empirische Verteilungsfunktion")
    plt.xlabel("Werte")
    plt.ylabel("Kumulierte Häufigkeit")
    plt.hist(data, df.shape[0]-1, cumulative=True, histtype="step", density=True,)


    plt.show()


def diskret(n, k, p, lam, type, method):

    print("\nBeschreibung \tFormel \t\t\tErgebnis")
    print("----------------------------------------------------------")

    if type == "geom":
        print("Geometrisch")
        if method == "pmf":
            print(f"P(X = {n}) \tgeom.pmf{n,p} \t{geom.pmf(n,p)}")
        elif method == "cdf":
            print(f"P(X <= {n}) \tgeom.cdf{n,p} \t{geom.cdf(n,p)}")
        elif method == "sf":
            print(f"P(X > {n}) \tgeom.sf{n,p} \t{geom.sf(n,p)}")
        
        print(f"Erwartungswert \t1/p \t\t\t{1/p} ")
       
        print(f"Varianz \tgeom.var({p}): \t\t{geom.var(p)}")


    if type == "bin":
        print("Binomial")
        if method == "pmf":
            print(f"P(X = {k}) \tbinom.pmf{k,n,p} \t{binom.pmf(k,n,p)}")
        elif method == "cdf":
            print(f"P(X <= {k}) \tbinom.cdf{k,n,p} \t{binom.cdf(k,n,p)}")
        elif method == "sf":
            print(f"P(X > {k}) \tbinom.sf{k,n,p} \t{binom.sf(k,n,p)}")
        
        print(f"Erwartungswert \tn*p \t\t\t{n*p} ")
       
        print(f"Varianz \tbinom.var({n,p}): \t{binom.var(n,p)}")


    if type == "po":
        print("Poisson")
        if method == "pmf":
            print(f"P(X = {k}) \tpoisson.pmf{k,lam} \t{poisson.pmf(k,lam)}")
        elif method == "cdf":
            print(f"P(X <= {k}) \tpoisson.cdf{k,lam} \t{poisson.cdf(k,lam)}")
        elif method == "sf":
            print(f"P(X > {k}) \tpoisson.sf{k,lam} \t{poisson.sf(k,lam)}")
        
        print(f"Erwartungswert \tlambda \t\t\t{lam} ")
       
        print(f"Varianz \tlambda \t\t\t{lam}")

        
def stetig(c,a,b,erwart, std, lam, method, type):
    print("\nBeschreibung \t\tFormel \t\t\tErgebnis")
    print("--------------------------------------------------------------------")

    if type == "gv":
        print("Gleichverteilung")
        if method == "cdf":
            print(f"P(X <= {c}) \t\tuniform.cdf{c,a,b} \t{uniform.cdf(c,a,b)}") #a,b,c / c,b,a | b,c,a n|a,c,b | b,a,c
        elif method == "sf":
            print(f"P(X > {c}) \t\tuniform.sf{c,a,b} \t{uniform.sf(c,a,b)}")
        
        print(f"Erwartungswert \t(a+b)/2 \t\t\t{(a+b)/2} ")
       
        print(f"Varianz \t((b-a)**2)/12 \t\t\t{((b-a)**2)/12}")

    if type == "exp":
        print("Exponentialverteilung")
        if method == "cdf":
            print(f"P(X < {c}) \t\texpon.cdf{c, lam} \t{expon.cdf(c,scale = 1/lam)}")
        elif method == "sf":
            print(f"P(X > {c}) \t\texpon.sf{c, lam} \t{expon.sf(c,scale = 1/lam)}")
        
        print(f"Erwartungswert \t1/lambda \t\t\t{1/lam} ")
       
        print(f"Varianz \t1/lambda**2 \t\t\t{1/lam**2}")

    if type == "norm":
        print("Normalverteilung")
        if method == "cdf":
            print(f"P(X < {c}) \t\tnorm.cdf{erwart, c, std} \t{norm.cdf(c, erwart,std)}")
        elif method == "sf":
            print(f"P(X > {c}) \t\tnorm.sf{erwart, c, std} \t{norm.sf(c, erwart,std)}")
        elif method == "ppf":
            print(f"x{c}) \t\tnorm.ppf{erwart, c, std} \t{norm.ppf(c, erwart,std)}")
        
        print(f"Erwartungswert \t1/lambda \t\t\t{1/lam} ")
       
        print(f"Varianz \t1/lambda**2 \t\t\t{1/lam**2}")






def laplace(test, tupel):
    
    print(len(list(filter(test, tupel))) / len(tupel))

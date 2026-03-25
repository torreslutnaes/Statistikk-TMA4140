import numpy as np
import matplotlib.pyplot as plt

#Oppgave 3C
r = 1000
n = 42
m = 35
frekvens = 12

alpha = 2*n/(2*n + m)
beta = 2*m/(2*n + m)

def poisson(frekvens, x):
    return (frekvens**x)/(x.np.factorial)*np.exp(-frekvens)

X = poisson(frekvens, r)
Y = poisson(frekvens=frekvens/2, x = r)


histogram_4 = plt.hist(bins=25, )



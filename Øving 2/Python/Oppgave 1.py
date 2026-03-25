# Importer nødvendige biblioteker, denne cellen må kjøres før annen kode.
import numpy as np
import matplotlib.pyplot as plt

# UTLVERT KODE (ingenting her skal endres)
# punktsannsynlighet
x = np.arange(6)
f_x = np.array([0.05, 0.10, 0.25, 0.40, 0.15, 0.05])

# kumulativ fordelingsfunksjon
F_x = [np.sum(f_x[:i]) for i in range(1, 7)]

def simX(n):
    # verdimengde
    x = np.arange(6)

    # for lagring av realisasjoner
    x_sim = np.zeros(n)

    for i in range(n):  # vi simulerer hver og en x for seg
        u = np.random.uniform()  # en realisasjon fra U(0,1)

        if u < F_x[0]:  # laveste verdi
            x_sim[i] = x[0]

        elif u <= F_x[1]:
            x_sim[i] = x[1]

        elif u <= F_x[2]:
            x_sim[i] = x[2]

        elif u <= F_x[3]:
            x_sim[i] = x[3]

        elif u <= F_x[4]:
            x_sim[i] = x[4]

        elif u > F_x[4]:
            x_sim[i] = x[5]

    return x_sim

n = 1000

u = 2

simulerte_X = simX(n)

P_X_le_2 = np.mean(simulerte_X <= 2)

E_X = np.sum (x * f_x)

Var = np.sum(x**2) - E_X**2

SD = np.sqrt(Var)



print("Approksimert sannsylighet: " , P_X_le_2)
print("Approksimert forventningsverdi er: ", E_X)
print("Approksimert standardavvik: ", SD)
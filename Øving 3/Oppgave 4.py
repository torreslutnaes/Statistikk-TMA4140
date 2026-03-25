#Oppgave 4

import numpy as np
import matplotlib.pyplot as plt


def y(n, m, s, a, b):
    x = np.random.normal(m,s,n)
    return a*x +b

def tetthet_y(x, m, s, a, b):
    mu_Y = a*m + b
    sigma_Y = abs(a)*s
    return (1/(sigma_Y*np.sqrt(2*np.pi))) * \
           np.exp(-((x-mu_Y)**2)/(2*sigma_Y**2))


generateY = y(100000, 1, 2, 2, 0.5)
generate_tetthetY = y(100000, 1, 2, 2, 0.5)

plt.hist(generateY, density=True, bins=100)
plt.plot(generate_tetthetY)
plt.show()




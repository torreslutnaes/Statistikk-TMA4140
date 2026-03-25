# Oppgave 2A

# Du trenger ikke endre noe i denne koden!

import numpy as np
# from scipy.stats import norm
import matplotlib.pyplot as plt

# Initialisering av parameterverdier
n = 25
alpha = 0.5
beta = 0.25
sigma = 0.25

# Simulering av data etter modell
# x_1, x_2, ..., x_n i intervallet [-5,5]
x = np.array([
    -3.842, -3.784, -3.745, -3.708, -3.37, -3.288, -2.312,
    -1.595, -1.106, -0.352, -0.171, 1.166, 2.196, 2.538,
    3.309, 3.876, 4.2, 4.261, 4.337, 4.352, 4.359
])

# Genererer tilhørende verdier for y_1, y_2, ..., y_n
y = alpha + beta * x + np.random.normal(loc=0, scale=sigma, size=len(x))

# Visualiserer resultatet i et plott
plt.plot(x, y, 'bo')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Du trenger ikke endre noe i denne koden!

def estimerELR(x, y):
    # Beregner gjennomsnitt
    xStrek = np.mean(x)
    yStrek = np.mean(y)
    
    # Estimater for parametere
    betaHat = np.sum((x - xStrek) * y) / np.sum((x - xStrek)**2)
    alphaHat = yStrek - betaHat * xStrek
    
    # Estimat for varians
    S2 = np.sum((y - (alphaHat + betaHat * x))**2) / (len(x) - 2)
    
    # Returnerer resultatet i en liste
    return [alphaHat, betaHat, S2]


paramHat = estimerELR(x, y)

print('alphaHat:', paramHat[0])
print('betaHat:', paramHat[1])
print('S2:', paramHat[2])


alphaHat = paramHat[0]
betaHat = paramHat [1]

residualer = y - (alphaHat + betaHat * x)

plt.plot(x, residualer, 'bo')
plt.axhline(0)
plt.xlabel('x')
plt.ylabel('Residualer')
plt.title('Residualplot')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Sett hvilke x-verdier du vil plotte for
x = np.linspace(0, 5, 100)

# Sett verdien for parameteren alpha
alpha = 1

# Beregn kumulativ fordelingsfunksjon
def F_X(x, alpha):
    return 1 - np.exp(-x**2 / alpha)

# Plot F(x)
plt.plot(x, F_X(x, alpha), color="red")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("Kumulativ fordelingsfunksjon F(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Sett hvilke x-verdier du vil plotte for
x = np.linspace(0, 5, 100)

# T-verdier for f_z
z = np.linspace(0,5,100)

# Sett verdien for parameteren alpha
alpha = 1

# Beregn kumulativ fordelingsfunksjon
def f_x(x, alpha):
    return (2*x/alpha)*np.exp((-x**2)/alpha)

def f_z(z, alpha):
    return (4*z/alpha) * np.exp(-z**2/alpha) * (1 - np.exp(-z**2/alpha))

# Plot f(x)
plt.plot(x, f_x(x, alpha), color="red")
plt.plot(z, f_z(z, alpha), color="blue")
plt.xlabel("x, z")
plt.ylabel("f(x), f(z)")
plt.title("Sannsynlighetstetthet for f(x) og f(z)")
plt.show()

#Oppgave 5A
#Kommentar: Min VS Code håndterer ikke scipy

import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2.5, 0.5, 3.3, 2.6, -0.7, -4.6, 3.3, 0.8, 1.9, -0.5, 1.2, 3.8])
y = np.array([4.1, 7.2, 5.0, 7.9, 5.8, 4.9, 5.0, 5.9, 6.9, 4.8, 6.7, 3.2])

def plot_normal(data, title):
    mu = np.mean(data)
    sigma = np.std(data, ddof=1)

    plt.hist(data, bins=6, density=True)

    xs = np.linspace(min(data)-1, max(data)+1, 200)
    normal = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((xs-mu)/sigma)**2)

    plt.plot(xs, normal)
    plt.title(title)
    plt.show()

plot_normal(x, "Histogram X")
plt.scatter(x, y) # Brukte dette for å se sammenhengen mellom X og Y
plt.show()
plot_normal(y, "Histogram Y")





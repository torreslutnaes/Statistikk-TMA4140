#Oppgave 1B
import numpy as np
import matplotlib.pyplot as plt

mu_x, sigma_x = 150, 5
mu_y, sigma_y = 200, 7
mu_theta, sigma_theta = 0.9, 0.05

n = 10000
X = np.random.normal(loc=mu_x, scale=sigma_x, size=n)
Y = np.random.normal(loc=mu_y, scale=sigma_y, size=n)
theta = np.random.normal(loc=mu_theta, scale=sigma_theta, size=n)
A = 0.5*X*Y*np.sin(theta)

mu_a = A.mean().round(2)
sigma_a = A.std().round(2)

print(mu_a)
print(sigma_a)

#Output på forventning = 11735.72 - fikk 11749 da jeg regnet for hånd  
#Output på standardavvik = 739.43 - 4 forskjellig fra svaret i oppgave a

#Undersøke om A er normalfordelt

def tetthet(mu, sigma, x):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp((-(x-mu)**2)/(2*sigma**2))

x_vals = np.linspace(min(A), max(A), 500)
histogram_A = plt.hist(A, bins=40, density=True)
plt.plot(x_vals, tetthet(mu_a, sigma_a, x_vals))
plt.show()

#Det ser ut som at A er tilnærmet normalfordelt, da sannsynlighetstettheten stemmer veldig bra med histogrammet




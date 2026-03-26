import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([
    24.7, 24.8, 27.3, 28.4, 28.4, 29.0, 30.3, 32.7, 35.6, 38.5,
    38.8, 39.3, 39.4, 42.9, 45.8, 46.9, 48.2, 51.5, 51.5, 53.4,
    56.0, 56.5, 57.3, 57.6, 59.2, 59.8
])

y = np.array([
    484, 427, 413, 517, 549, 648, 587, 704, 979, 914,
    1070, 1020, 1210, 989, 1160, 1400, 1760, 1710, 2010, 1880,
    1980, 1820, 2020, 1980, 2310, 1940 
])

n = len(x) + 1

#Utregning av gjennomsnitt for x og y
x_snitt = np.mean(x).round(3)
y_snitt = np.mean(y).round(3)

print(x_snitt)
print(y_snitt)

def beta_hat(x, y): 

    x_snitt = np.mean(x)
    y_snitt = np.mean(y)
    
    teller = 0
    nevner = 0
    
    for i in range(len(x)):
        teller += (x[i] - x_snitt) * (y[i] - y_snitt)
        nevner += (x[i] - x_snitt)**2
    
    return teller / nevner


def alpha_hat(x, y):
    x_snitt = np.mean(x)
    y_snitt = np.mean(y)
    return y_snitt - beta_hat(x, y) * x_snitt

def sigma2_hat(x, y):
    n = len(x)
    a_hat = alpha_hat(x, y)
    b_hat = beta_hat(x, y)
    
    sum_var = 0
    for i in range(n):
        sum_var += (y[i] - a_hat - b_hat * x[i])**2
    
    return sum_var / n

x_lin = np.linspace(min(x), max(x), 100)
y_lin = alpha_hat(x,y) + beta_hat(x,y) * x_lin

residualer = y - (alpha_hat(x,y) + beta_hat(x,y) * x)
    
# Spredningsplott
plt.scatter(x, y)
plt.plot(x_lin, y_lin, color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Spredningsplott")
plt.show()

# Residualplott mot x
plt.scatter(x, residualer)
plt.axhline(0)
plt.xlabel("x")
plt.ylabel("Residualer")
plt.title("Residualplott")
plt.show()
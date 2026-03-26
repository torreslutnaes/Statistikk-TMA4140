import numpy as np

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

# Estimatorer
def beta_hat(x, y):
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    return np.sum((x - x_bar)*(y - y_bar)) / np.sum((x - x_bar)**2)

def alpha_hat(x, y):
    return np.mean(y) - beta_hat(x, y)*np.mean(x)

# Beregninger
n = len(x)
a_hat = alpha_hat(x, y)
b_hat = beta_hat(x, y)

# Residualer
y_hat = a_hat + b_hat * x
residualer = y - y_hat

# Varians (med n-2!)
sigma2_hat = np.sum(residualer**2) / (n - 2)

# Standardfeil til alpha
x_bar = np.mean(x)
Sxx = np.sum((x - x_bar)**2)

SE_alpha = np.sqrt(sigma2_hat * (1/n + x_bar**2 / Sxx))

# Testobservator
T = a_hat / SE_alpha

print("alpha_hat =", a_hat)
print("SE_alpha =", SE_alpha)
print("T =", T)
#Oppgave 3B

import matplotlib.pyplot as plt
import numpy as np

data = np.array([7.98,10.82,15.88,17.00,24.22,12.20,8.17,16.53,7.46,
 14.31,34.55,19.46,20.21,13.58,10.98,4.42,24.92,30.29,
 23.45,23.36])

r_hat = np.mean(data)
print(r_hat) #Output = 16.9895


plt.hist(data, bins=8, density= True)
plt.title("Histogram")
plt.show()

plt.boxplot(data)
plt.title("Boxplot")
plt.show()

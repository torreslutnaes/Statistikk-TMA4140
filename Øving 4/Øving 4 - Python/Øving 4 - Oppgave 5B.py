#Oppgave 5B - brukt for å finne gjennomsnitt og utvalgsstandardavvik (S)

import numpy as np

x = np.array([-2.5, 0.5, 3.3, 2.6, -0.7, -4.6, 3.3, 0.8, 1.9, -0.5, 1.2, 3.8])


def s(data):
    mean = np.mean(data)
    print(mean.round(3))
    return np.sqrt((1/(len(data)-1)) * np.sum((data - mean)**2))

print(s(x).round(3))


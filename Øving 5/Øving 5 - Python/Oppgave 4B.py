#Oppgave 4B

import numpy as np
from random import sample
import matplotlib.pyplot as plt

def testStatistic(x, nTrad):
    meanTrad = np.mean(x[0:(nTrad)])
    meanNew = np.mean(x[(nTrad):])
    return meanNew - meanTrad

x = [0.189,0.743,0.605,0.044,0.091,0.045,0.532,0.642,
 0.397,0.583,0.355,0.054,0.155,0.066,0.099]

statisticObserved = testStatistic(x,8)
print('Observert verdi: ',statisticObserved.round(4)) #Output: -0.1172

M = 10000

simulated = []

for i in range(M):
    xPermuted = sample(x, len(x))
    statisticSimulated = testStatistic(xPermuted, 8)
    simulated.append(statisticSimulated)

p_value = np.mean([s <= statisticObserved for s in simulated])  

print('Simulert verdi: ', statisticSimulated.round(4)) #Output: 0.1726
print("p-value: ", p_value) #Output: 0.1905

plt.hist(simulated, bins=50)
plt.axvline(statisticObserved, color='red')
plt.show()




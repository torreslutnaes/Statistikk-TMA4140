import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
f_x = np.array([0.05, 0.10, 0.25, 0.40, 0.15, 0.05])

plt.figure(figsize=(7, 4))
plt.bar(x, f_x)
plt.xticks(x)
plt.ylim(0, 0.45)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Stolpediagram for f(x)")

plt.tight_layout()
plt.show(block=True)

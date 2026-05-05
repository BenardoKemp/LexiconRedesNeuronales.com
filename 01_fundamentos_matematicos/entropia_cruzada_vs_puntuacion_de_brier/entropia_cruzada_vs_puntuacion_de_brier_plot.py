import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0.01, 1, 200)

# Entropía cruzada (y=1)
cross_entropy = -np.log(p)

# Brier Score (y=1)
brier = (p - 1) ** 2

plt.plot(p, cross_entropy, label="Entropía cruzada")
plt.plot(p, brier, label="Brier Score")

plt.xlabel("Probabilidad predicha (clase correcta)")
plt.ylabel("Pérdida")
plt.title("Entropía cruzada vs Brier Score")

plt.legend()
plt.grid(True)
plt.show()
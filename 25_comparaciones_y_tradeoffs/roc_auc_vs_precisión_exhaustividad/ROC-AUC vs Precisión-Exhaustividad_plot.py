import numpy as np
import matplotlib.pyplot as plt

# Datos simulados
recall = np.linspace(0, 1, 100)
precision = 1 - 0.7 * recall**1.5

fpr = np.linspace(0, 1, 100)
tpr = 1 - (1 - fpr)**2

# Crear figura
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Curva ROC
ax[0].plot(fpr, tpr)
ax[0].plot([0, 1], [0, 1], linestyle="--")
ax[0].set_title("Curva ROC")
ax[0].set_xlabel("Tasa de falsos positivos")
ax[0].set_ylabel("Tasa de verdaderos positivos")

# Curva Precisión-Exhaustividad
ax[1].plot(recall, precision)
ax[1].set_title("Curva Precisión-Exhaustividad")
ax[1].set_xlabel("Exhaustividad")
ax[1].set_ylabel("Precisión")

plt.tight_layout()
plt.show()
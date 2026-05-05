import numpy as np
import matplotlib.pyplot as plt

# Entropía cruzada binaria cuando la clase verdadera es 1:
# CE = -log(p)
# p = probabilidad predicha para la clase correcta

def entropia_cruzada(p):
    p = np.clip(p, 1e-10, 1.0)
    return -np.log(p)

# Probabilidades predichas para la clase correcta
p = np.linspace(0.01, 1.0, 200)

# Calcular entropía cruzada
ce = entropia_cruzada(p)

# Crear gráfica
plt.plot(p, ce, label="Entropía cruzada")

plt.xlabel("Probabilidad predicha para la clase correcta")
plt.ylabel("Pérdida")
plt.title("Entropía cruzada binaria")

plt.scatter([0.1, 0.5, 0.9], entropia_cruzada(np.array([0.1, 0.5, 0.9])),
            label="Ejemplos: p=0.1, 0.5, 0.9")

plt.legend()
plt.grid(True)
plt.show()
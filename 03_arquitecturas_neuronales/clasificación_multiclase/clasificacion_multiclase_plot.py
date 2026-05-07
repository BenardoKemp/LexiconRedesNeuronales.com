import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Clases posibles
# -----------------------------

clases = ["Gato", "Perro", "Pájaro", "Conejo"]

# -----------------------------
# Probabilidades predichas
# (deben sumar 1)
# -----------------------------

probabilidades = [0.15, 0.65, 0.10, 0.10]

# -----------------------------
# Crear gráfica
# -----------------------------

plt.bar(clases, probabilidades)

# -----------------------------
# Etiquetas
# -----------------------------

plt.ylabel("Probabilidad")
plt.title("Clasificación multiclase")

# -----------------------------
# Mostrar probabilidades
# -----------------------------

for i, p in enumerate(probabilidades):
    plt.text(i, p + 0.02, f"{p:.2f}", ha="center")

# -----------------------------
# Limitar eje Y
# -----------------------------

plt.ylim(0, 1)

# -----------------------------
# Mostrar gráfica
# -----------------------------

plt.show()
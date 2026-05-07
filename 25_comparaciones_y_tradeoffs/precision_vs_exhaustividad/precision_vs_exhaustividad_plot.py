import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Umbrales de decisión
# -----------------------------

thresholds = [0.1, 0.3, 0.5, 0.7, 0.9]

# -----------------------------
# Valores simulados
# -----------------------------

precision = [0.45, 0.60, 0.75, 0.88, 0.97]
recall = [0.98, 0.90, 0.78, 0.55, 0.25]

# -----------------------------
# Crear gráfica
# -----------------------------

plt.plot(thresholds, precision, marker="o", label="Precisión")
plt.plot(thresholds, recall, marker="o", label="Exhaustividad")

# -----------------------------
# Etiquetas
# -----------------------------

plt.xlabel("Umbral de decisión")
plt.ylabel("Valor")
plt.title("Precisión vs exhaustividad")

# -----------------------------
# Límites
# -----------------------------

plt.ylim(0, 1)

# -----------------------------
# Cuadrícula y leyenda
# -----------------------------

plt.grid(True)
plt.legend()

# -----------------------------
# Mostrar gráfica
# -----------------------------

plt.show()
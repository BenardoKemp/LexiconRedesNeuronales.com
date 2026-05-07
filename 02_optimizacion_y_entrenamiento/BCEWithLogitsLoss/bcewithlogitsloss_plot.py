import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Función sigmoide
# -----------------------------

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# -----------------------------
# BCEWithLogitsLoss manual
# para y = 1
# -----------------------------

def bce_with_logits(logits, y=1):
    probs = sigmoid(logits)
    return -(y * np.log(probs) + (1 - y) * np.log(1 - probs))

# -----------------------------
# Valores de logits
# -----------------------------

logits = np.linspace(-10, 10, 200)

# -----------------------------
# Calcular pérdida
# -----------------------------

loss = bce_with_logits(logits, y=1)

# -----------------------------
# Crear gráfica
# -----------------------------

plt.plot(logits, loss)

# -----------------------------
# Etiquetas
# -----------------------------

plt.xlabel("Logits")
plt.ylabel("Pérdida")
plt.title("BCEWithLogitsLoss")

# -----------------------------
# Cuadrícula
# -----------------------------

plt.grid(True)

# -----------------------------
# Mostrar gráfica
# -----------------------------

plt.show()
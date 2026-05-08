import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Función sigmoide
# -----------------------------

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# -----------------------------
# Binary Cross-Entropy manual
# usando probabilidades
# -----------------------------

def binary_cross_entropy(p, y=1):
    p = np.clip(p, 1e-10, 1 - 1e-10)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))

# -----------------------------
# BCEWithLogitsLoss manual
# usando logits directamente
# -----------------------------

def bce_with_logits(logits, y=1):
    p = sigmoid(logits)
    return binary_cross_entropy(p, y)

# -----------------------------
# Valores de logits
# -----------------------------

logits = np.linspace(-10, 10, 200)

# -----------------------------
# Convertir logits a probabilidades
# -----------------------------

probs = sigmoid(logits)

# -----------------------------
# Calcular pérdidas
# -----------------------------

cross_entropy_loss = binary_cross_entropy(probs, y=1)
bce_logits_loss = bce_with_logits(logits, y=1)

# -----------------------------
# Crear gráfica
# -----------------------------

plt.plot(logits, cross_entropy_loss, label="Entropía cruzada")
plt.plot(logits, bce_logits_loss, linestyle="--",
         label="BCEWithLogitsLoss")

# -----------------------------
# Etiquetas
# -----------------------------

plt.xlabel("Logits")
plt.ylabel("Pérdida")
plt.title("Entropía cruzada vs BCEWithLogitsLoss")

# -----------------------------
# Cuadrícula y leyenda
# -----------------------------

plt.grid(True)
plt.legend()

# -----------------------------
# Mostrar gráfica
# -----------------------------

plt.show()
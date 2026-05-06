import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Datos de ejemplo
# -----------------------------

categorias = ["Perro", "Gato", "Pájaro"]

# Multiclase: solo una clase activa
multiclase = [1, 0, 0]

# Multilabel: varias etiquetas activas
multilabel = [1, 1, 0]

x = np.arange(len(categorias))
width = 0.35

# -----------------------------
# Crear gráfica
# -----------------------------

fig, ax = plt.subplots()

ax.bar(x - width/2, multiclase, width, label="Multiclase")
ax.bar(x + width/2, multilabel, width, label="Multilabel")

# -----------------------------
# Etiquetas
# -----------------------------

ax.set_ylabel("Activación")
ax.set_title("Clasificación multilabel vs multiclase")
ax.set_xticks(x)
ax.set_xticklabels(categorias)

# -----------------------------
# Leyenda
# -----------------------------

ax.legend()

# -----------------------------
# Mostrar gráfica
# -----------------------------

plt.show()
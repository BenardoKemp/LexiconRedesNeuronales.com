import matplotlib.pyplot as plt

# -----------------------------
# Clases binarias
# -----------------------------

clases = ["No spam", "Spam"]

# -----------------------------
# Probabilidades predichas
# -----------------------------

probabilidades = [0.25, 0.75]

# -----------------------------
# Crear gráfica
# -----------------------------

plt.bar(clases, probabilidades)

# -----------------------------
# Etiquetas
# -----------------------------

plt.ylabel("Probabilidad")
plt.title("Clasificación binaria")

# -----------------------------
# Mostrar valores
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
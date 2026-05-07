import matplotlib.pyplot as plt

# Clases
clases = ["Negativo", "Positivo"]

# Probabilidades
probabilidades = [0.35, 0.65]

# Umbral
threshold = 0.5

# Crear gráfica
plt.bar(clases, probabilidades)

# Línea del umbral
plt.axhline(threshold, linestyle="--", label=f"Umbral = {threshold}")

# Etiquetas
plt.ylabel("Probabilidad")
plt.title("Umbral de decisión")

# Mostrar valores
for i, p in enumerate(probabilidades):
    plt.text(i, p + 0.02, f"{p:.2f}", ha="center")

plt.ylim(0, 1)

plt.legend()
plt.show()
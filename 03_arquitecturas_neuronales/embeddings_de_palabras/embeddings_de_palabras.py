import matplotlib.pyplot as plt

# -----------------------------
# Palabras y coordenadas 2D
# (embeddings simulados)
# -----------------------------

words = ["rey", "reina", "hombre", "mujer",
         "gato", "perro"]

x = [0.8, 0.82, 0.65, 0.67, -0.5, -0.45]
y = [0.9, 0.75, 0.55, 0.40, -0.6, -0.55]

# -----------------------------
# Crear gráfica
# -----------------------------

plt.figure(figsize=(8, 6))

plt.scatter(x, y)

# -----------------------------
# Etiquetas de palabras
# -----------------------------

for i, word in enumerate(words):
    plt.text(x[i] + 0.02, y[i] + 0.02, word)

# -----------------------------
# Título y ejes
# -----------------------------

plt.title("Embeddings de palabras")
plt.xlabel("Dimensión 1")
plt.ylabel("Dimensión 2")

# -----------------------------
# Cuadrícula
# -----------------------------

plt.grid(True)

# -----------------------------
# Mostrar gráfica
# -----------------------------

plt.show()
import numpy as np
import matplotlib.pyplot as plt

# 1. Define sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 2. Generate x values
x = np.linspace(-10, 10, 200)

# 3. Compute sigmoid probabilities
y = sigmoid(x)

# 4. Plot sigmoid curve
plt.plot(x, y, label="Función sigmoide")

# 5. Add decision threshold
plt.axhline(0.5, linestyle="--", label="Umbral de decisión (0.5)")

# 6. Labels and title
plt.xlabel("Entrada (x)")
plt.ylabel("Probabilidad")
plt.title("Regresión logística")

# 7. Grid and legend
plt.grid(True)
plt.legend()

# 8. Show plot
plt.show()
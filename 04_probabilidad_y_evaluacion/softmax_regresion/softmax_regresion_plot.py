import numpy as np
import matplotlib.pyplot as plt

# 1. Define softmax function
def softmax(z):
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z)

# 2. Example scores (logits)
logits = np.array([2.0, 1.0, 0.1])

# 3. Compute probabilities
probabilidades = softmax(logits)

# 4. Class labels
clases = ["Clase A", "Clase B", "Clase C"]

# 5. Create bar chart
plt.bar(clases, probabilidades)

# 6. Labels and title
plt.ylabel("Probabilidad")
plt.title("Regresión Softmax")

# 7. Set y-axis range
plt.ylim(0, 1)

# 8. Display probability values
for i, p in enumerate(probabilidades):
    plt.text(i, p + 0.02, f"{p:.2f}", ha='center')

# 9. Show plot
plt.show()
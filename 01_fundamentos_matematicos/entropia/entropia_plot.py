import numpy as np
import matplotlib.pyplot as plt

# 1. Define entropy function (binary entropy)
def entropy(p):
    # Avoid log(0) issues
    p = np.clip(p, 1e-10, 1 - 1e-10)
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

# 2. Generate probability values
p = np.linspace(0, 1, 100)

# 3. Compute entropy
H = entropy(p)

# 4. Plot
plt.plot(p, H, label="Entropía")

# 5. Labels and title
plt.xlabel("Probabilidad (p)")
plt.ylabel("Entropía H(p)")
plt.title("Entropía de una variable binaria")

# 6. Highlight maximum entropy point
plt.scatter([0.5], [entropy(0.5)], label="Máxima entropía (p=0.5)")

# 7. Show legend
plt.legend()

# 8. Display plot
plt.show()
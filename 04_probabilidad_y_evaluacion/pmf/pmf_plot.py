import numpy as np
import matplotlib.pyplot as plt

# 1. Possible outcomes of a fair die
x = np.array([1, 2, 3, 4, 5, 6])

# 2. Probability for each outcome
p = np.array([1/6] * 6)

# 3. Create bar chart
plt.bar(x, p)

# 4. Labels and title
plt.xlabel("Resultado")
plt.ylabel("Probabilidad")
plt.title("Función de Masa de Probabilidad (PMF)")

# 5. Set x-axis ticks
plt.xticks(x)

# 6. Add grid
plt.grid(axis="y")

# 7. Display plot
plt.show()
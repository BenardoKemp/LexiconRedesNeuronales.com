import numpy as np
import matplotlib.pyplot as plt

# 1. Define Brier Score function
# y = actual outcome (0 or 1)
def brier_score(p, y):
    return (p - y) ** 2

# 2. Generate probability values
p = np.linspace(0, 1, 200)

# 3. Compute Brier scores for both cases
brier_y1 = brier_score(p, 1)  # when true label = 1
brier_y0 = brier_score(p, 0)  # when true label = 0

# 4. Plot
plt.plot(p, brier_y1, label="Real = 1")
plt.plot(p, brier_y0, label="Real = 0")

# 5. Labels and title
plt.xlabel("Probabilidad predicha")
plt.ylabel("Error (Brier Score)")
plt.title("Puntuación de Brier")

# 6. Highlight key points
plt.scatter([0, 1], [brier_score(0, 1), brier_score(1, 1)])
plt.scatter([0, 1], [brier_score(0, 0), brier_score(1, 0)])

# 7. Legend and grid
plt.legend()
plt.grid(True)

# 8. Show plot
plt.show()
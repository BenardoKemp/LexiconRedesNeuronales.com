import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Generate simple data
np.random.seed(42)
X = 2 * np.random.rand(50, 1)  # Input feature
y = 4 + 3 * X + np.random.randn(50, 1)  # y = 4 + 3x + noise

# 2. Train linear regression model
model = LinearRegression()
model.fit(X, y)

# 3. Make predictions
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)

# 4. Plot data points
plt.scatter(X, y, label="Datos reales")

# 5. Plot regression line
plt.plot(X_new, y_pred, color="red", label="Línea de regresión")

# 6. Labels and title
plt.xlabel("X")
plt.ylabel("y")
plt.title("Ejemplo de Regresión Lineal")

# 7. Show legend
plt.legend()

# 8. Display plot
plt.show()

import numpy as np

y_true = [1, 0, 0]
y_pred = [0.9, 0.05, 0.05]

loss = -np.sum(np.array(y_true) * np.log(y_pred))
print(loss)
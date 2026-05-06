from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([0, 1, 2, 1])

model = LogisticRegression(multi_class='multinomial')
model.fit(X, y)

print(model.predict_proba([[2.5]]))
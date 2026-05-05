import numpy as np

p = np.array([0.5, 0.5])
entropy = -np.sum(p * np.log(p))

print(entropy)
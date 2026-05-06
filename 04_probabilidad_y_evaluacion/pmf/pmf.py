import numpy as np

# simulación de dado
samples = np.random.randint(1, 7, 1000)

values, counts = np.unique(samples, return_counts=True)
pmf = counts / len(samples)

print(dict(zip(values, pmf)))
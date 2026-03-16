import numpy as np

data = np.array([12,15,18,20,22,25,28,30,35,40])

# Mean estimation
mean_est = np.mean(data)

# Variance estimation
var_est = np.var(data)

# Random sampling
sample = np.random.choice(data, size=5)

print("Sample Data:", sample)
print("Estimated Mean:", mean_est)
print("Estimated Variance:", var_est)

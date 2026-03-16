import numpy as np
from scipy import stats

# Sample revenue data (100 customers)
revenue = np.random.normal(500, 50, 100)

# Mean revenue
mean = np.mean(revenue)

# Standard error
sem = stats.sem(revenue)

# 95% confidence interval
confidence = stats.t.interval(0.95, len(revenue)-1, loc=mean, scale=sem)

print("Mean Revenue:", mean)
print("95% Confidence Interval:", confidence)

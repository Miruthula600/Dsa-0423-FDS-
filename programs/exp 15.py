from scipy import stats
import matplotlib.pyplot as plt

control = [20,22,19,24,21]
treat = [28,30,27,29,31]

t,p = stats.ttest_ind(control,treat)
print("p-value:",p)

plt.boxplot([control,treat],labels=["Control","Treatment"])
plt.show()

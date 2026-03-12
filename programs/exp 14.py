import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# sample dataset
data = {'feedback':[
'This product is amazing',
'Very good service',
'The product quality is good',
'Service is excellent and amazing'
]}

df = pd.DataFrame(data)

text = " ".join(df['feedback']).lower()

# remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()

stopwords = ['the','is','and','a','an','very']

words = [w for w in words if w not in stopwords]

freq = Counter(words)

N = 5
top_words = freq.most_common(N)

print(top_words)

words = [w[0] for w in top_words]
counts = [w[1] for w in top_words]

plt.bar(words,counts)
plt.title("Top Words")
plt.show()

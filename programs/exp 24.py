from collections import Counter

products = ['Laptop','Phone','Tablet','Laptop','Phone','Laptop','Tablet','Phone','Laptop']

frequency = Counter(products)

print("Product Frequency:", frequency)

most_popular = frequency.most_common(1)

print("Most Popular Product:", most_popular)

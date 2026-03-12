reviews = [
    "good product",
    "good quality product",
    "excellent product quality"
]

word_count = {}

for review in reviews:
    words = review.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

print(word_count)

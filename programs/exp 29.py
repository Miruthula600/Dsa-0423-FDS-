import pandas as pd
from scipy import stats

# Read CSV file
df = pd.read_csv("customer_reviews.csv")

ratings = df['rating']

mean_rating = ratings.mean()

sem = stats.sem(ratings)

confidence = stats.t.interval(0.95, len(ratings)-1, loc=mean_rating, scale=sem)

print("Average Rating:", mean_rating)
print("95% Confidence Interval:", confidence)

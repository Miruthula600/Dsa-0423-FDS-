import pandas as pd

# Sample temperature dataset
data = {
    'City':['CityA','CityB','CityC','CityD'],
    'Day1':[30,25,28,32],
    'Day2':[32,26,27,31],
    'Day3':[31,27,29,30],
    'Day4':[33,28,30,34],
    'Day5':[34,29,31,33]
}

df = pd.DataFrame(data)
df.set_index('City', inplace=True)

# Mean temperature
mean_temp = df.mean(axis=1)

# Standard deviation
std_temp = df.std(axis=1)

# Temperature range
temp_range = df.max(axis=1) - df.min(axis=1)

# City with highest range
highest_range_city = temp_range.idxmax()

# Most consistent city
consistent_city = std_temp.idxmin()

print("Mean Temperature:\n", mean_temp)
print("\nStandard Deviation:\n", std_temp)
print("\nTemperature Range:\n", temp_range)
print("\nCity with Highest Temperature Range:", highest_range_city)
print("Most Consistent City:", consistent_city)

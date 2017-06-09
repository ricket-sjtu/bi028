import pandas

df = pandas.read_csv('sample.csv')

# Any missing values?
print df['Price']
print df['Description']

# Fill missing prices by a linear interpolation
df['Description'] = df['Description'].fillna("No description is available.")
df['Price'] = df['Price'].interpolate()

print df
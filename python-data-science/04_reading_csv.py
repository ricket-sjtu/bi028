import pandas

df = pandas.read_csv('sample.csv')

# Display the DataFrame
print df
print

# DataFrame's columns
print df.columns
print

# Values of a given column
print df['Model']
print
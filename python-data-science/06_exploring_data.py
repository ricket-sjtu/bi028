import pandas
import matplotlib.pyplot as plt


df = pandas.read_csv('sample2.csv')

# This table has 3 columns: Office, Year, Sales
print df.columns

# It's really easy to query data with Pandas:
print df[(df['Office'] == 'Stockholm') & (df['Sales'] > 260)]

# It's also easy to do aggregations...
aggregated_sales = df.groupby('Year').sum()
print aggregated_sales

# ... and generate plots
aggregated_sales.plot(kind='bar')

plt.show()
import pandas

df = pandas.read_excel('input.xlsx')

# check what's in the excel data
print(df.head())

# create new column 'Total'
df['Total'] = df['Price'] * df['Quantity']
print(df.head())  # check on new col

# create new excel with extended data
df.to_excel('output.xlsx')

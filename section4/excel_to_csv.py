import pandas

df = pandas.read_excel('europe.xlsx')
df.to_json('europe.csv', orient='records')

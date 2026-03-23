import pandas as pd
df = pd.read_csv(r"C:\Users\vikra\Downloads\archive (3)\zomato.csv.csv")
df.head()
print(df.columns)
df = df.drop(['url','phone','dish_liked','reviews_list'], axis=1)
print(df.isnull().sum())
df = df.dropna()

df = df[df['rate'] != 'NEW']
df = df[df['rate'] != '-']

df['rate'] = df['rate'].str.split('/').str[0]
df['rate'] = df['rate'].astype(float)

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str).str.replace(',', '')
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(float)

df.rename(columns={
    'approx_cost(for two people)': 'cost',
    'listed_in(city)': 'city'
}, inplace=True)

df.to_csv("zomato_clean.csv", index=False)
print(df.groupby("city")["rate"].mean().sort_values(ascending=False).head())
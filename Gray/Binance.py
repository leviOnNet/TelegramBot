import pandas as pd

df = pd.read_html(
    "https://coinmarketcap.com/gainers-losers/", 
    attrs={'rules': 'all'}, 
    header=0, 
    index_col="#")[0]

print(df)
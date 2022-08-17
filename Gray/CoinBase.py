from cgitb import html
from site import addsitedir
from ssl import HAS_TLSv1_1
from bs4 import BeautifulSoup
import requests
import pandas as pd

cmc_page = requests.get("https://coinmarketcap.com/new/")
cmc_soup = BeautifulSoup(cmc_page.text,"html.parser")
# Creating list with all tables
tables = cmc_soup.find_all('table')

#  Looking for the table with the classes 'wikitable' and 'sortable'
table = cmc_soup.find('table', class_='h7vnx2-2 deceFm cmc-table')

CMC_df = pd.DataFrame(columns=['Name','Price','24H','Added'])

# Collecting Ddata
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        Name        = columns[2].p.text.strip()
        Price       = columns[3].text.strip()
        Hour1       = columns[4].text.strip()
        Hour24      = columns[5].text.strip()
        MarketCap   = columns[6].text.strip()
        Volume      = columns[7].text.strip()
        BlockChain  = columns[8].text.strip()
        Added       = columns[9].text.strip()

        CMC_df = CMC_df.append({'Name':Name,'Price':Price,'24H':Hour24,'Added':Added},ignore_index=True)

print(CMC_df.head())

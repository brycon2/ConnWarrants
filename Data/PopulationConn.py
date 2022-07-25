import pandas as pd # data analysis
import requests # handles data requests
from bs4 import BeautifulSoup # parases html documents

# table information

url = 'https://en.wikipedia.org/wiki/List_of_municipalities_in_Connecticut'
table_class = "wikitable sortable"

#parsing with requests and beautifulsoup
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
conn_table = soup.find('table',class_ = table_class)
 
#making table into dataframe and turning it into a csv
conn_df_list = pd.read_html(str(conn_table))
conn_df = pd.DataFrame(conn_df_list[0])
conn_df.to_csv('./ConnPopData.csv')

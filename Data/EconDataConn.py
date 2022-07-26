import pandas as pd # data analysis
import requests # handles data requests
from bs4 import BeautifulSoup # parases html documents

#table information

url = 'https://en.wikipedia.org/wiki/List_of_Connecticut_locations_by_per_capita_income#Incorporated_county_subdivisions'

#parsing page with requests and beautifulsoup
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

# get second table from the wikipedia page
conn_table = soup.find_all('table')[2]
 
#making table into dataframe and turning it into a csv
conn_df_list = pd.read_html(str(conn_table))
conn_df = pd.DataFrame(conn_df_list[0])

# keeping only data for town or cities
conn_df = conn_df[(conn_df['Unnamed: 2']=='Town') | (conn_df['Unnamed: 2']=='City')].reset_index(drop = True)

#dropping rank, county, and population columns as they aren't necessary for our purposes
conn_df.drop(columns = ['Rank','Population','County','Unnamed: 2'], inplace = True)
conn_df.rename(columns = {'Town':'Municipality','Per capitaincome':'Per Capita Income',
'Medianhouseholdincome': 'Med. Household Income','Medianfamilyincome':'Med. Family Income',
'Number ofhouseholds':'Num. of Households'}, inplace= True)

conn_df.to_csv('./Data/EconData.csv')
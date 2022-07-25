# merge all the months into one table

# pandas for dataframe handling
import pandas as pd

# setting up months and file naming stuff
months = ['Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
file_append = '-2019.csv'
file_prepend = './Data/FinalMonths/'

# blank list for inputting data for each month
df2019 = []

# iterating through each month's data and adding it to the list, and with each df add a column with the current month
for month in months:
    file = file_prepend + month + file_append
    data = pd.read_csv(file, index_col= 0)
    data['Month'] = month
    df2019.append(data)

# Take the list of dataframes and concatenate it into one table
df2019 = pd.concat(df2019,ignore_index=True, join = 'outer')

# This is to fix a glitch where for some reason, concat duplicates a column and attaches it with NaN values
df2019 = df2019.iloc[:,:-1]
# export csv with final data
df2019.to_csv('./Data/WarrantData2019.csv')
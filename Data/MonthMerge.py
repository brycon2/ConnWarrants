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
    # there is regex in the file names so removing them to avoid future errors
    data.columns = data.columns.str.replace('[\n]','',regex = True)
    data['Month'] = month
    df2019.append(data)

# Take the list of dataframes and concatenate it into one table
df2019 = pd.concat(df2019,ignore_index=True, join = 'outer')

# the month and served warrants are in awkward places relative to rest of data, moving them 
df2019.insert(1,'Month',df2019.pop('Month')) #putting month in the second column

# renaming column titles
df2019.rename(columns = {'Municipality *':'Municipality','Warrants with Law Enforcement Actions Noted':'Warrants with LEA', 
 'Issued Warrants For Month':'Issued Warrants','Served Warrants For Month':'Served Warrants',
 'Warrants Foreign Served For Month':'Warrants Foreign Served'},inplace = True)

# export csv with final data
df2019.to_csv('./Data/WarrantData2019.csv')
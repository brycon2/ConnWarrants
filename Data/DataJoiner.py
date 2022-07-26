from audioop import cross
from numpy import outer
import pandas as pd

#month abbreviations
months = ['Jan', 'Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#pages of each month range from 2 to 13
pages = [x for x in range(2,14)]

#odd pages are added vertically, even pages are added to the right with municipality 

for month in months:
    monthcsv = './FinalMonths/' + month + "-2019.csv"
    
    for page in pages:
        #current page of month's csv
        currentcsv =  './MonthIntermediates/' + month + '2019-page-' + str(page) + '-table-1.csv' 
        
        # if we are on first page, create new dataframe
        if page == pages[0]: 
             #create dataframe with first page and do nothing else
            evenpage = pd.read_csv(currentcsv)
        
        elif page == pages[1]:
            oddpage = pd.read_csv(currentcsv)

        #if page number is even and not first even page, add it to the bottom of even page df
        elif page%2 == 0: 
            workingdf = pd.read_csv(currentcsv)
            evenpage = pd.concat([evenpage, workingdf], join = 'outer')
        
        #if page number is odd and is not first , add it to the bottom of odd page df
        else: 
            workingdf = pd.read_csv(currentcsv)
            oddpage = pd.concat([oddpage, workingdf], join = 'outer')
        
    #merge the odd page df and the even page df
    monthdf = pd.merge(evenpage,oddpage, on = 'Municipality *')
    
    #read out csv
    monthdf.to_csv(monthcsv)




    
import camelot #note, use pip install camelot-py and requires opencv-python and ghostscript 
import PyPDF2

#pdfs to be turned into tables
pdfs = ['./Data/pdfs/rearrestmunicipaltab20190102.pdf','./Data/pdfs/rearrestmunicipaltab20190201.pdf',
'./Data/pdfs/rearrestmunicipaltab20190301.pdf','./Data/pdfs/rearrestmunicipaltab20190401.pdf',
'./Data/pdfs/rearrestmunicipaltab20190501.pdf','./Data/pdfs/rearrestmunicipaltab20190604.pdf',
'./Data/pdfs/rearrestmunicipaltab20190702.pdf','./Data/pdfs/rearrestmunicipaltab20190801.pdf',
'./Data/pdfs/rearrestmunicipaltab20190903_EDIT.pdf','./Data/pdfs/rearrestmuicipaltab20191001_EDIT.pdf',
'./Data/pdfs/rearrestmunicipaltab20131101_GOOD.pdf','./Data/pdfs/rearrestmuniciapltab20191202_EDIT.pdf']

#csv names
csvs = ['./Data/MonthIntermediates/Jan2019.csv','./Data/MonthIntermediates/Feb2019.csv','./Data/MonthIntermediates/Mar2019.csv','./Data/MonthIntermediates/Apr2019.csv','./Data/MonthIntermediates/May2019.csv','./Data/MonthIntermediates/Jun2019.csv',
'./Data/MonthIntermediates/Jul2019.csv','./Data/MonthIntermediates/Aug2019.csv','./Data/MonthIntermediates/Sep2019.csv','./Data/MonthIntermediates/Oct2019.csv','./Data/MonthIntermediates/Nov2019.csv','./Data/MonthIntermediates/Dec2019.csv']

for i in range(len(pdfs)):
    file = open(pdfs[i],'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    pages = str(readpdf.numPages)

    table = camelot.read_pdf(pdfs[i], pages = '2 - ' + pages)
    table.export(csvs[i],f = "csv")
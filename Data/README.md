# Data Layout and Information

[PopulationConn.py](./PopulationConn.py) took the population data from Wikpedia for the different towns in Connecticut. Resulting data can be seen in [ConnPopData](./ConnPopData.csv).  

[PDFScrubber.py](./PDFSCrubber.py) scrubbed the PDFs released by the State of Connecticut on warrant information and created tables that go into the [Month Intermediates](./MonthIntermediates) folder. 

[DataJoiner.py](./DataJoiner.py) takes these intermediate tables and joins them so there is one table for each month. The resultant data is in [FinalMonths](./FinalMonths)

[MonthMerge.py](./MonthMerge.py) takes the data for each month and makes it into one giant table, which is [WarrantData2019.csv](./WarrantData2019.csv)

[2010_2020_population_changes.csv](./2010_2020_population_changes.csv) is from CTDataHaven and contains demographic data for the year 2020 from the census. 
# Data Layout and Information

## Scripts

[PopulationConn.py](./PopulationConn.py) took the population data from Wikpedia for the different towns in Connecticut. Resulting data can be seen in [ConnPopData](./ConnPopData.csv).  

[PDFScrubber.py](./PDFSCrubber.py) scrubbed the PDFs released by the State of Connecticut on warrant information and created tables that go into the [Month Intermediates](./MonthIntermediates) folder. 

[DataJoiner.py](./DataJoiner.py) takes these intermediate tables and joins them so there is one table for each month. The resultant data is in [FinalMonths](./FinalMonths)

## Files and Folders

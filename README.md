## Input 
AddressBuilding.csv 
AddressCompany.csv
Company.csv

## Output
companies_in_office_buildings.csv

### Notes
I have found buildings where only firms are located (without flats). 

## Instructions for the candidate

Hi,

we're glad you agreed to work on our little case. The aim of this is to show some of your skills in data analysis and research. Please do not spend an awful lot of time on this.
Anything between 2-4 hours should be entirely sufficient.

1. Collect the file and import into your preferred database engine (SQL Server,MySQL,Postgres, ...) or scripting language session (R,Python,Julia, ...) or both
2. The file contains data for addresses, buildings at these addresses and companies operating on these addresses in Karlin, Prague 8
3. Once your files are imported, check their consistency and follow to the case in --Task-- section below.


## Task

We would like to find out, which rows in the Building dataset (ObjectCode) are likely to be office buildings (have a look at some of the addresses to understand)
The task is to try to build an analytical procedure, a classifier or predictive model which will make allow that - note that for a predictive model, you will have to find a way to make you own labels/training data.
Use the variables to compute your own indicators if needed. Use any library, statistical method or analytical approach you find suitable or you have experience with - but be ready to explain your choice of method.

Hint1: A lot about a building can be infered from the number,types and sizes of companies residing there. <br/>
Hint2: Study the datamap.txt file to learn more about the columns <br/>
Hint3: The data about buildings comes from the Czech Cadaster office and cannot be assumed 100 percent accurate - add your own logic before jumping to conclusions from fe. UsageCode

## Output

1. Try to write your analysis so that anyone reading your script can understand what is being done. The script should be as reproducible as possible. Think about how new data can be plugged into the model.
2. Choose how you present, visualize or summarise your findings - in the plotting library of your scripting language or simply in Microsoft Excel / Google Apps or a similar tool
3. Remember that how you will proceed is entirely up to you, we have no prefabricated answers to this exercise. 
4. Do not focus on accuracy too much, we also value clarity, reproducibility, creative approach and elegance of the model.


# NYC Property and a predictor of Crime

This exploration has been organized as a set of Jupyter Notebooks.
The notebooks should be executed in a specific order as each notebook will mutate the state of the overall exploration in steps.

### data folder
Working directory where data is loaded and various iterations of the data is stored.

Some files have been prepared for mapping various columns in the data to ordinal/score and categorical values.
### mappings folder

### scripts folder
Contains order set of Jupyter note books

- severity_score.csv - mapping crime types to a severity_score
- crime_type_categories.csv - mapping crime types a super category
- economic_values.csv - mapping property types to an economic score

## Step 1 - Loading Data
Loads the data from AWS S3 to a local "Data" Directory with progress indicators

- Property Data: NYC Property Valuation and Assessment Data
  - Real Estate Assessment Property data. The Department of Finance values properties every year as one step in calculating property tax bills.
  - Rows 9.85M, Columns 40, File size 2.8GB

- Crime Data: NYPD Complaints Data
  - List of every arrest in NYC going back to 2006 through the end of the previous calendar year. This is a breakdown of every arrest effected in NYC by the NYPD going back to 2006 through the end of the previous calendar year.
  - Rows 5.72M, Columns 19, File size, 3.03GB

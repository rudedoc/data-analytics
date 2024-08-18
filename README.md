# NYC predictors of Crime
This exploration has been organized as a set of Jupyter Notebooks.
The notebooks should be executed in a specific order as each notebook will mutate the state of the overall exploration in steps.
### data folder
Working directory where data is loaded and various iterations of the data is stored.
### mappings folder
Some files have been prepared for mapping various columns in the data to ordinal/score and categorical values.
### scripts folder
Contains order set of Jupyter note books

- severity_score.csv - mapping crime types to a severity_score
- crime_categories.csv - mapping crime types a super category
- economic_values.csv - mapping property types to an economic score
- nyc_landmarks.csv - couple of landmarks for context on the geospatial diagrams
- boundaries - draw borough boundaries on the maps/geospatial diagrams
## Step 1 - Loading Data
Loads the data from AWS S3 to a local "Data" Directory with progress indicators

- Mental Health Services Data
- Population Census Data
- Crime Data: NYPD Complaints Data
  - List of every arrest in NYC going back to 2006 through the end of the previous calendar year. This is a breakdown of every arrest effected in NYC by the NYPD going back to 2006 through the end of the previous calendar year.
  - Rows 5.72M, Columns 19, File size, 3.03GB



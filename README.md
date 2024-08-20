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

## Running the experiment
The experiment is contained in a number of jupyter notebooks in the script folder.
The experiment should be run in the order as set in the file names in the script folder:

|Order    |File Name                                              |
|---------|-------------------------------------------------------|
|1        |1 - Loading Data.ipynb                                 |
|2        |2 - NYC Mental Health Services Data Preparation.ipynb  |
|3        |3 - NYC Mental Health Services Data Exploration.ipynb  |
|4        |4 - NYC Census Data Preparation.ipynb                  |
|5        |5 - NYC Census Data Exploration.ipynb                  |
|6        |6 - NYPD Complaints Data Preparation.ipynb             |
|7        |7 - NYPD Complaints Data Exploration.ipynb             |
|8        |8 - Model Training.ipynb                               |
|8        |9 - NYC Classification Model Evaluation.ipynb          |

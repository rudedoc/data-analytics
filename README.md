# NYC predictors of Crime
## Mark Finlay - National College of Ireland - x10209221@student.ncirl.ie
Code artifact for Data Analytics Module for PGDAI, August 2024

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

## Final Model
You can download the final trained model here: `https://mf-data-analytics.s3.eu-west-1.amazonaws.com/nyc_crime_category_random_forest_model_180_18.pkl`. It is approx 11.GB in size.

## Video Presentation
https://studentncirl-my.sharepoint.com/:v:/r/personal/x10209221_student_ncirl_ie/Documents/Recordings/Data%20Analytics%20Presentation%20-%20Mark%20Finlay%20-%20x10209221%20-%20NYC%20Data-20240820_214800-Meeting%20Recording.mp4?csf=1&web=1&e=5FCgVG&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D

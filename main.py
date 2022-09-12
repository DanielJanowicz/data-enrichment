## Importing packages
import pandas as pd
import numpy as np

## Loading data
NY = pd.read_csv('data/NYHIVReport.csv')
SPS = pd.read_csv('data/SPARCS.csv')

## Getting column names
SPS.columns
NY.columns 

## Sampling for testing
NY.sample(20)
SPS.sample(20)

## Removing special characters and white space
NY.columns = NY.columns.str.replace('[^A-Za-z0-9]+', '_')
SPS.columns = SPS.columns.str.replace('[^A-Za-z0-9]+', '_')

## Creating smaller tables for merge
SPS_small = SPS[['Health_Service_Area', 'Hospital_County', 'Facility_Id', 'Zip_Code_3_digits']]
NY_small = NY[['Gender', 'Age', 'Race', 'HIV_diagnoses', 'HIV_diagnosis_rate']]

## Merging NY_small to SPS_small
NY_combined = SPS_small.merge(NY_small, how='left', left_on='Health_Service_Area', right_on='Gender')

## Alternative way
NY_combined2 = pd.merge(NY_small, SPS_small, how='left', left_on='Gender', right_on='Health_Service_Area')

############################
##### Second alternative way
############################
SPS_small.to_csv('alt/SPS_small.csv')
NY_small.to_csv('alt/NY_small.csv')

## Defining sets to csv
SPS_df = pd.read_csv('alt/SPS_small.csv')
NY_df = pd.read_csv('alt/NY_small.csv')

## Alternative Merge
cdf = [SPS_df, NY_df]
NY_combined = pd.concat(cdf)

## Cleaning up of NaN (Refer to errors.md)
# NY_combined.replace(to_replace='', value=np.nan, inplace=True)
# NY_combined.replace(to_replace=' ', value=np.nan, inplace=True)

# NY_combined.dropna(inplace=True)
# NY_combined.isnull().sum()

## Saved merge to CSV
NY_combined.to_csv('data/NY_combined.csv')


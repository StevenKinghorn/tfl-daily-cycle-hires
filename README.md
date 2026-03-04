# ⚠️ Work in Progress
## Stage:
### Downloaded tfl cycle hire data
- Finished python script (scripts/download-csv.py) that downloads 48 csv files from [cycling.data.tfl.gov.uk](https://cycling.data.tfl.gov.uk/#!usage-stats%2F). These 48 files contain cycle hire purchases from 2024 to 2025. The python script uses json file to locate appropriate csv's (json/cycling_data.json) 


### Data Cleaning:
- There are roughly 18 million records of cycle hires spread over 48 .csv files (2024-2025)
- Out of the 48 files, from years 2024 and 2025, 11 csv files have inconsistent schema. Will need to ensure all features are consistent across all 48 files before performing exploritory data analysis. 

import boto3
import os
import json
from botocore import UNSIGNED
from botocore.config import Config

# Number of csv files to download for this project
csv_no = 48 
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

def download_from_config(config_path):
    i = 0
    with open(config_path, 'r') as file:
        data = json.load(file) 

    for entry in data['entries']:
        s3_url = entry['url']
        clean_url =s3_url.replace("s3://", "")
        bucket_name, key = clean_url.split("/", 1)
        filename = os.path.basename(key)
        i = i + 1
        
        print(f"Downloading file {i} of {csv_no}:  {filename}")
        try:
            s3.download_file(bucket_name, key, f"../data/tfl-cycling-journey-data-2024-2025/raw-2024-2025-csv/{filename}")
            print(f"Done: ../data/tfl-cycling-journey-data-2024-2025/raw-2024-2025-csv/{filename}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
        
        
if __name__ == "__main__":
    print(f"WARNING: Download size is quite large ({csv_no} .csv files, ~2.8G) and may take some time.")
    user_input = input("Are you sure you want to continue? (Y,n)").strip().lower()

    if user_input in ['y', 'yes', '']:
        file_path = "../json/cycling_data.json"
        download_from_config(file_path)
    else:
        print("Download cancelled.")
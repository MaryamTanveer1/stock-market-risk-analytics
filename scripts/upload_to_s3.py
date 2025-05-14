# upload_to_s3.py
import boto3

session = boto3.Session(
    aws_access_key_id='****',       
    aws_secret_access_key='*****',
    region_name='us-east-1' 
)
s3 = session.client('s3')

local_file = '/Users/mac/Desktop/stock-market-risk-analytics/data/downloaded_results.csv'  
bucket_name = 'stock-market-data-demo-maryam-gen'  
s3_key = 'processed/final_results.csv'             

try:
    s3.upload_file(local_file, bucket_name, s3_key)
    print(f"✅ File uploaded to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print(f"❌ Upload failed: {e}")


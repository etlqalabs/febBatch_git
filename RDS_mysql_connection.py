import pandas as pd
from sqlalchemy import create_engine
import boto3
from io import StringIO

mysql_engine = create_engine("mysql+pymysql://admin:password@mysqlaws.cnkoc8gg2fb4.ap-south-1.rds.amazonaws.com:3306/testDB")

def fetch_products_details():
    query = """select * from products"""
    df = pd.read_sql(query,mysql_engine)
    print("actual data :",df)
# fetch_products_details()




# s3://bucket-employees-file/sources/sales_data.csv
#s3://bkt-s3-demo/empdata/salary.csv

# initiate a session with aws
s3  = boto3.client('s3')

def read_file_from_s3(bucket_name,file_key):
    # fetch a csv file from s3
    response = s3.get_object(Bucket=bucket_name,Key=file_key)

    csv_content = response['Body'].read().decode('utf-8')

    data = StringIO(csv_content)
    df = pd.read_csv(data)
    return df

df = read_file_from_s3("bkt-s3-demo","empdata/salary.csv")
print(df)
import pandas as pd
import boto3

def write_dataframe_to_csv_on_s3(dataframe, filename, **kwarg):
    """ Write a dataframe to a CSV on S3 """
    print("Writing {} records to {}".format(len(dataframe), filename))
    path = 'tmp/out.csv'
    dataframe.to_csv(path, sep=";", index=False, decimal = ',', encoding='ISO-8859-1', **kwarg)
    s3_resource = boto3.resource("s3")
    s3_resource.Object('krotonanalytics', filename).upload_file(path)
    print('Done')
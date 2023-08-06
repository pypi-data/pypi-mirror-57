# -*- coding: utf-8 -*-
"""
utility functions for parsing html files

@author: bernsteind
"""

from shutil import rmtree, copyfileobj
import glob
import boto3
import pandas as pd
import os

s3_client = boto3.client('s3')

def setup_dirs(parsing_ext='',
               dirs=[], 
               sub_dirs=[],
               parsing_dir_name = 'parsing'):
    
    if not os.path.isdir(parsing_dir_name):
        os.makedirs(parsing_dir_name)
        
    if parsing_ext:
        for dir_name in dirs:
            dir_path = '{0}/{1}/{2}'.format(parsing_dir_name, parsing_ext, dir_name)
            if os.path.isdir(dir_path):
                rmtree(dir_path)        
            
            os.makedirs(dir_path)
        
        if sub_dirs:
            for sub_dir in sub_dirs:
                sub_dir_path = '{0}/{1}/{2}/{3}'.format(parsing_dir_name, parsing_ext, 'parsed_htmls', sub_dir)
                os.mkdir(sub_dir_path)
        
        log_dir_path = 'parsing/{0}/logs'.format(parsing_ext)
        if not os.path.exists(log_dir_path):
            os.mkdir(log_dir_path)
    else:
        for dir_name in dirs:
            dir_path = '{0}/{1}'.format(parsing_dir_name, dir_name)
            if os.path.isdir(dir_path):
                rmtree(dir_path)        
            
            os.makedirs(dir_path)
        
        if sub_dirs:
            for sub_dir in sub_dirs:
                sub_dir_path = '{0}/{1}/{2}'.format(parsing_dir_name, 'parsed_htmls', sub_dir)
                os.mkdir(sub_dir_path)
        
        log_dir_path = 'parsing/logs'
        if not os.path.exists(log_dir_path):
            os.mkdir(log_dir_path)


def merge_csvs(key, # table name
               merged_file, # year or month value used in aggregation
               local_dir_ext='parsing' # local subdirectory used for containing parsed files
               ):
    try:
        print('processing: ' + key)
        file_list = glob.glob('{0}/parsed_htmls/{1}/*.csv'.format(local_dir_ext, key))
        if len(file_list) > 0:
            with open(merged_file, 'wb') as outfile:
                for i, fname in enumerate(file_list):
                    with open(fname, 'rb') as infile:
                        if i != 0:
                            infile.readline()  # Throw away header on all but first file
                        # Block copy rest of file from input to output without parsing
                        copyfileobj(infile, outfile)

                    os.remove(fname)
    except Exception as e:
  #      logging.exception("error: process_df_list : {0}".format(str(key)), exc_info=True)
        print(e)


def write_to_s3(agg_value, section_name, locale, output_bucket, merged_file):
    try:
        # convert the merged csv to parquet
        df = pd.read_csv(merged_file)
        os.remove(merged_file)

        if not df.empty:
            local_file=merged_file.replace('.csv', 'parquet.gzip')
            df.to_parquet(local_file, index=False)
            if locale:
                s3_key='parsed/{0}/{1}/year={2}/{1}.parquet.gzip'.format(locale, section_name, agg_value)
            else:
                s3_key='parsed/{0}/year={1}/{0}.parquet.gzip'.format(section_name, agg_value)
            s3_client.upload_file(
                    Filename=local_file,
                    Bucket = output_bucket,
                    Key=s3_key,
                    ExtraArgs={"ServerSideEncryption": "aws:kms", "SSEKMSKeyId": 'd70f9891-24db-4c2e-8473-7ae14c5e2dd6' })
            os.remove(local_file)

    except Exception as e:
        #logging.exception("error: write_to_s3 : {0}".format(str(key)), exc_info=True)
        print(e)

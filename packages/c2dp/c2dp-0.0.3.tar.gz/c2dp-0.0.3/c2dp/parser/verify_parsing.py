# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:12:38 2019

@author: bernsteind
"""


import pandas as pd
import numpy as np
import boto3

import sys
import os
sys.path.insert(0, os.path.abspath('../aws'))
from aws.aws import read_parquet


def verify_row_count(locale, 
                     html_locale_ext, 
                     parsed_bucket, 
                     years = [2000, 2019],
                     clean=False):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket('odga')
    count_list = []

    for year in range(years[0], years[1], 1):
        print(year)
        
        # raw html files
        obj_list = []        
        [obj_list.append(obj.key) for obj in bucket.objects.filter(Prefix='{0}/raw/htmls_civil_cases/{1}/'.format(html_locale_ext, year))]
        
        # parsed file
        if locale:
            parsed_path = 'parsed/{1}/case_info/year={0}/case_info.parquet.gzip'.format(year, locale)
        else:
            parsed_path = 'parsed/case_info/year={0}/case_info.parquet.gzip'.format(year)
            
           
        parsed_case_info = read_parquet(parsed_bucket, parsed_path)
                    
        count_dict = {
                'year' : str(year),
                'locale' : str(html_locale_ext),
                'scraped_files' : str(len(obj_list)),
                'num_parsed_rows' :str(parsed_case_info.shape[0]),
                }
    
        if clean:
            clean_case_info = read_parquet(parsed_bucket, parsed_path.replace('parsed/', 'clean/'))
            count_dict.update({
                    'num_clean_rows' : str(clean_case_info.shape[0])
                    })

               
        count_list.append(count_dict)
        print(count_list)
        
    return pd.DataFrame(count_list)


#verify_row_count('north_dakota', 'courtdata-nd')

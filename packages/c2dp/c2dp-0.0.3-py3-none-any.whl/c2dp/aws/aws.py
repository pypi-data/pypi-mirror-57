# -*- coding: utf-8 -*-
"""
aws helper functions 

@author: bernsteind
"""

import io
import pyarrow
import pandas as pd
import boto3
import pyarrow as pa
import pyarrow.parquet as pq


# Read the parquet file
def read_parquet(bucket, key, columns=None):
    s3_client = boto3.client('s3')
    buffer = io.BytesIO()
    s3_client.download_fileobj(Fileobj=buffer, Bucket=bucket, Key=key)
    df = pd.read_parquet(buffer, columns=columns)
    
    return df


def dataframe_to_s3(input_datafame, bucket_name, filepath, format):

        s3_client = boto3.client('s3')
        
        if format == 'parquet':
            out_buffer = io.BytesIO()
            input_datafame.to_parquet(out_buffer, index=False)

        elif format == 'csv':
            out_buffer = io.StringIO()
            input_datafame.to_parquet(out_buffer, index=False)

        s3_client.put_object(Bucket=bucket_name, Key=filepath, Body=out_buffer.getvalue())


def filter_data(bucket,
                locale,
                tables_dict,
                case_type_list,
                years = [2000, 2018],
                merge_vars=['case_num'],
                format='parquet'):
    if len(years) == 1:
        years.append(years[0])
    if format == 'parquet':
        output_dict = {}

        for key, value in tables_dict.items():
            print(key)
            df_list = []

            for year in range(years[0], years[1] + 1, 1):
                print(year)
                if locale:
                    df = read_parquet(bucket, 'clean/{2}/{1}/year={0}/{1}.parquet.gzip'.format(year, key, locale),
                                      columns=value)
                else:
                    df = read_parquet(bucket, 'clean/{1}/year={0}/{1}.parquet.gzip'.format(year, key),
                                      columns=value)
                if key == 'case_info':
                    df = df[df.case_type.apply(lambda x: any(val in x for val in case_type_list))]

                df_list.append(df)

            all_years_df = pd.concat(df_list).reset_index(drop=True)

            output_dict.update({key: all_years_df})

        # filter all other tables to only include case numbers that are in the case_info table
        for key, value in output_dict.items():
            if key != 'case_info':
                value = output_dict[key][output_dict[key]['case_num'].isin(output_dict['case_info'].case_num)].reset_index()
                output_dict.update({key : value})

    return output_dict


# -*- coding: utf-8 -*-
"""
utility functions for automated documentation generation

@author: bernsteind
"""

import pandas as pd
import numpy as np
import os
import boto3
import io 

def make_documentation_dir(dir_path = 'documentation'):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)


def get_locale_info(s3_file ='locale_info/locale_info.csv', bucket = 'courtdata-docs'):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=s3_file)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))

    return df


def filter_locale_info(locale):
    df = get_locale_info()
    locale_row = df[df['locale'] == locale.lower()].melt()
    locale_row = locale_row[locale_row.variable != 'locale']

    return locale_row


def get_caseCount(df, 
                  key, 
                  case_num_var, 
                  case_type_var, 
                  date_var, 
                  filter_text = 'case_info'):
   # print(df)
   if filter_text:
       if filter_text in key:

           df['year'] = df[date_var].apply(pd.to_datetime).apply(lambda x: x.strftime('%Y'))
           df_caseType = df.groupby(['year', case_type_var])[case_num_var].agg('nunique').reset_index()
           df_caseType.columns = ['year', case_type_var, 'case_count']
           return df_caseType
       else:
            return pd.DataFrame()
   else:
        df['year'] = df[date_var].apply(pd.to_datetime).apply(lambda x: x.strftime('%Y'))
        df_caseType = df.groupby(['year', case_type_var])[case_num_var].agg('nunique').reset_index()
        df_caseType.columns = ['year', case_type_var, 'case_count']
    
        return df_caseType


def summarize_numeric(series):
    var_kurtosis = series.kurtosis()
    var_skew = series.skew()
    variable_type = 'numeric'
                    
    var_range = '[{0}, {1}]'.format(series.min(), series.max())
    var_median = series.median()
                
    var_row = {'variable' : series.name, 
               'variable_type' : variable_type,
               'median' : var_median, 
               'range' : var_range, 
               'skewness' : var_skew, 
               'kurtosis' : var_kurtosis}
    
    return var_row

def summarize_categorical(series):
    variable_type = 'string'

    var_row = {'variable' : series.name, 
               'variable_type' : variable_type,
               'median' :  np.nan, 
               'range' :  np.nan, 
               'skewness' :  np.nan, 
               'kurtosis' :  np.nan}
    
    return var_row



def generate_frequency_df(df, col, case_num_var):
    df_freq = df.groupby(col)[case_num_var].nunique().reset_index()
    df_freq.columns = ['value label', 'frequency']
    df_freq['percentage'] = 100 * df_freq['frequency'] / sum(df_freq['frequency'])
            
    return df_freq


def get_variableSummary(df, case_num_var):
    var_list = []

    for col in list(df):
        if col != 'year':
            print(col)
    
            var_series = df[col]
            num_unique_vals = var_series.agg('nunique', axis = 0)
            missing_vals = var_series.isnull().sum() # missing observations
            nonmissing_vals = var_series.count() # non-missing values
            if var_series.dtypes == 'float64':
                var_row = summarize_numeric(var_series)
            
            else:
                var_row = summarize_categorical(var_series)
                
            var_row.update(
                    {'variable' : col,
                   'nonmissing_values' : nonmissing_vals,
                   'missing_values' : missing_vals,
                   'num_unique_values' : num_unique_vals,
            #       'df_freq' : df_freq
                   })
        
            var_list.append(var_row)
        
    return var_list




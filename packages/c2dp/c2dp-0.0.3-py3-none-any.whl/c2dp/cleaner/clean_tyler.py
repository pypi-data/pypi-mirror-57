# -*- coding: utf-8 -*-
"""

Functions to parsing Tyler Technology website HTML pages

Created on Wed Oct 30 13:45:22 2019

@author: bernsteind
"""

import logging
import boto3
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import numpy as np
import glob
from shutil import rmtree
import shutil, os, sys
from itertools import chain


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



def clean_case_info(soup, case_num):
    try:
        summary_dict = {'case_num' : case_num}

        child_els = str(soup).rsplit('§', 1)
        case_title = bs(child_els[0].lower()).b.text.replace('\n', ' ').strip()
        summary_dict.update({'case_title': case_title})

        # extract all section strings from the righthand side table
        summary_strings = [x for x in bs(child_els[-1]).stripped_strings]

        # loop through the list, assigning the odd index values to the key and next one to the value
        for value in summary_strings[0::2]:
            summary_dict.update({value : summary_strings[summary_strings.index(value) + 1]})
            summary_dict = dict((k.lower(), v.lower().strip()) for k, v in summary_dict.items())

    except Exception as e:
        print('no summary table')
        print(e)
        summary_dict = {}

    return summary_dict



def clean_parties(soup, case_num, delimiter='|||'):
    try:
        party_information_table = pd.read_html(str(soup).replace(u'\xa0', u' ').replace('<br/>', delimiter).replace('</i>', delimiter))[0]
        party_information_table.columns = ['party_type', 'party_name', 'x1', 'x2', 'attorney']
        
        out = []
        for el in soup.find_all('td', attrs={'headers':'PIc5'}):
            try:
                attorney_name = el.b.text.lower()
            except:
                attorney_name = str(np.nan)
            try:
                retained_status = el.i.text.lower()
            except:
                retained_status = str(np.nan)
                
            try:                    
                attorney_address = ' '.join(bs(str(el.find('table')).replace('<br/>', delimiter)).text.lower().split())
            except:
                attorney_address = str(np.nan)
            
            out.append([attorney_name, retained_status, attorney_address])
        attorney_df = pd.DataFrame(out, columns=['attorney_name', 'retained_status', 'attorney_address'])

        # use the empty rows between parties to define which addresses are associated with which parties
        party_information_table['FLAG'] = np.where(party_information_table['party_type'].isnull(), party_information_table.index, np.NaN)

        # fill forward (down) the FLAG column to give an ID to each person
        party_information_table[['FLAG']] = party_information_table[['FLAG']].fillna(method='ffill')
        party_information_table = party_information_table[party_information_table.party_type.notnull()]
        party_information_table = party_information_table[party_information_table.party_name.notnull()]

        # group by the FLAG (ID) value and concatenate the strings in the name column to merge locations with persons
        party_information_table['party_name'] = party_information_table.groupby(['FLAG']).party_name.transform(lambda x: delimiter.join(x))
        party_information_table = party_information_table.drop_duplicates().drop(['FLAG'], axis=1)
        party_information_table['party_name'] , party_information_table['party_location'] = zip(*party_information_table['party_name'].apply(parse_party_info))
        party_information_table = party_information_table.reset_index(drop=True)
        party_information_table = party_information_table.apply(lambda x: x.str.lower() if (x.dtype == 'object') else x)
        
        party_information_table['attorney_name'] = party_information_table.attorney.fillna('').apply(lambda x: str(x.split(delimiter)[0]))
        party_information_table=party_information_table.merge(attorney_df, on=['attorney_name'], how='left')
        party_information_table['attorney'] = party_information_table.attorney.fillna('')
        party_information_table['phone_number'] = party_information_table.apply(lambda x: str(x.attorney).replace(str(x.attorney_name) + delimiter, '').replace(str(x.retained_status) + delimiter, '').replace(str(x.attorney_address), '').strip().replace(delimiter, ', ').lstrip(', '), axis = 1)
        party_information_table['phone_number'] = party_information_table.phone_number.replace('nan', np.nan).replace('pro se', np.nan).replace('', np.nan)
        party_information_table['attorney_address'] = party_information_table.attorney_address.apply(lambda x: str(x).replace(delimiter, ', '))
        party_information_table['attorney_address'] = party_information_table.attorney_address.replace('nan', np.nan).replace('none', np.nan).replace('', np.nan)
        party_information_table['retained_status'] = party_information_table.retained_status.replace('nan', np.nan).replace('none', np.nan).replace('', np.nan)

        party_information_table['case_num'] = case_num
        party_information_table=party_information_table.drop(['x1', 'x2'], axis=1)

    except Exception as e:
        print('no party table')
        print(case_num)
        print(e)
        party_information_table = pd.DataFrame()

    return party_information_table


def parse_party_info(x, delimiter='|||'):
    try:
        party_split = x.split(delimiter, 1)
        party_name = party_split[0]
        
        if len(party_split) > 1:
            party_location = party_split[-1].replace(delimiter, ', ').strip().rstrip(',')
        else:
            party_location = np.nan
    except:
        party_name = x
        party_location = np.nan

    return party_name, party_location


def clean_disposition(soup, case_num):
    soup = bs(str(soup).replace('</nonobr>', '').replace('<nonobr>', '').replace('<nobr>', '').replace('</nobr>', ''))
    disp_date = soup.find('th', attrs = {'id' : re.compile('RDISPDATE')}).text

    disp_dict = {
            'case_num' : case_num,
            'disp_date' : disp_date
            }
    try:
        disposition_header_el = soup.find('td', attrs = {'headers' : 'CDisp'})
        
        try:
            disposition_header = disposition_header_el.b.get_text()
            disp_dict.update({'disposition_header' : disposition_header})
        except:
            disposition_header = np.nan
        try:            
            judicial_officer_el = [x for x in soup.find('td', attrs={'headers': 'CDisp'}).stripped_strings if 'Judicial Officer:' in x][0]
            result = re.search('Judicial Officer:(.*)\)', judicial_officer_el)
            judicial_officer = result.group(1).strip()
            disp_dict.update({'judicial_officer' : judicial_officer})
            
        except:
            judicial_officer = np.nan
        try:
            full_judgment_info = '|||'.join([x for x in soup.find('td', attrs={'headers': 'CDisp'}).stripped_strings if x not in [disposition_header, judicial_officer_el]])
            ' '.join(full_judgment_info.replace('(|||', '(').replace('|||)', ')').replace('\r\n', ' ').split())
            disp_dict.update({'full_judgment_info' : full_judgment_info})
        except:
            full_judgment_info = np.nan            
    except:
        print('disposition error up front')

    try:
        judgment_amount = soup.find(text=re.compile(r'Judgment of')).parent.span.get_text()
        disp_dict.update({'judgment_amount' : judgment_amount})
    except:
        print('no judgment amount matching `Judgment of`')

    # separate the elements that are separated by ': '
    try:
        els = soup.find_all('td', class_ = 'ssMenuText ssSmallText', attrs = {'style' : 'padding-left:40px'})
        disp_list = [x.get_text() for x in els if x.get_text() != '']
        for y in disp_list:
            tuple = y.split(': ', 1)
            disp_dict.update({tuple[0] : tuple[1]})

    except Exception as e:
        print('no disposition details')
        print(e)
     #   disp_dict = {}

    disp_dict = dict((k.lower(), v.lower().strip()) for k, v in disp_dict.items())

    return disp_dict

# Extract Information for Other Events and Hearings Table
def clean_other_events(soup, case_num, delimiter = '|||'):
    try:
        # find all Other Events and Entry Rows by the header in the td elements in the table (this also removes the disposition information, if present)
        event_header = soup.find('td', attrs = {'headers' : 'COtherEventsAndHearings'}).b.text.replace('\xa0', ' ')
        event_header = re.sub('\s+', ' ', event_header).strip()

        event_date = soup.find('th', attrs = {'id' : re.compile('RCDER')}).text

        event_info = [x for x in soup.find('td', attrs={'headers': 'COtherEventsAndHearings'}).stripped_strings]
        if event_info[0] == event_header:
            event_info.pop(0)

        event_info_string = re.sub(r'\s+', ' ',  delimiter.join(event_info).replace('\n', ' '))

        event_dict = {
            'case_num' : case_num,
            'event_date' : event_date,
            'event_header' : event_header,
            'event_info' : event_info_string}

        event_dict = dict((k.lower(), v.lower().strip()) for k, v in event_dict.items())

    except:
        print('no events table')
        event_dict = {}

    return event_dict


def clean_related_cases(soup, case_num):
    related_cases_el = soup.find_all('td', class_='ssSmallText')
    related_cases_list = [x.text.replace(u'\xa0', ' ').strip() for x in related_cases_el]
   # related_cases_string = '|||'.join(related_cases_list)

    related_cases_df = pd.DataFrame(related_cases_list, columns = ['related_cases'])
    related_cases_df['case_num'] = case_num
 #   related_cases_dict = {
 #       'case_num' : case_num,
 #       'related_cases' : related_cases_string
 #   }
 
    return related_cases_df


def move_case_num_to_front(df, case_num_var = 'case_num'):
    cols = list(df)
    # move the column to head of list using index, pop and insert
    cols.insert(0, cols.pop(cols.index(case_num_var)))
    # use ix to reorder
    df = df.ix[:, cols]

    return df


def tidy_split(df, column, sep='|', keep=False):
    """
    Split the values of a column and expand so the new DataFrame has one split
    value per row. Filters rows where the column is missing.

    Params
    ------
    df : pandas.DataFrame
        dataframe with the column to split and expand
    column : str
        the column to split and expand
    sep : str
        the string used to split the column's values
    keep : bool
        whether to retain the presplit value as it's own row

    Returns
    -------
    pandas.DataFrame
        Returns a dataframe with the same columns as `df`.
    """
    indexes = list()
    new_values = list()
    df = df.dropna(subset=[column])
    for i, presplit in enumerate(df[column].astype(str)):
        values = presplit.split(sep)
        if keep and len(values) > 1:
            indexes.append(i)
            new_values.append(presplit)
        for value in values:
            indexes.append(i)
            new_values.append(value)
    new_df = df.iloc[indexes, :].copy()
    new_df[column] = new_values
    return new_df


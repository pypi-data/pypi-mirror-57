# -*- coding: utf-8 -*-
"""
Functions to parse Tyler Technology website HTML pages

@author: bernsteind
"""

import logging
import boto3
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
from shutil import rmtree
import os, sys

sys.path.insert(0, os.path.abspath('../scraper'))
from scraper.scrape_tyler_technologies import setup_driver, pass_page, set_case_number, submit_form

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

def verify_file(file, 
                bad_strings,
                base_url,
                select_text,
                link_text):
    body = get_file(bucket='odga', file_name=file)
    soup = bs(body, features='lxml')
    
    if (any(string in str(soup) for string in bad_strings)) or (soup.body.text == ''):
        with open('parsing/logs/error_rescraped_files.out', "a+") as f:
            f.write('{0}\n'.format(file))
        print('bad file detected: {0}'.format(file))
        rescrape_file(file,
                      base_url=base_url,
                      select_text=select_text,
                      link_text=link_text)
        
        body = get_file(bucket='odga', file_name=file)
        soup = bs(body, features='lxml')

    return soup
    

def rescrape_file(file, 
                  base_url,
                  select_text,
                  link_text):
    
    try:
        case_num = os.path.basename(file).split('.html')[0]
        sess = setup_driver(headless=True)

        pass_page(sess, 
                  base_url,
                  select_text,
                  link_text,
                  select_type = "visible text")
        
        set_case_number(sess, case_num)
        
        submit_form(sess)
        sess.driver.find_element_by_partial_link_text(case_num).click()
    
        html_text = sess.driver.page_source
        save_to_s3(html_text, file)
    except Exception as e:
        with open('parsing/logs/error_during_rescraping.out', "a+") as f:
            f.write('{0}\n {1}\n'.format(file, e))


def save_to_s3(html_text, file, bucket = 'odga'):
    s3_client = boto3.client('s3')
    s3_client.put_object(Body=html_text, Bucket=bucket, Key=file)


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

def get_file(bucket, file_name):
    obj = s3_resource.Object(bucket, file_name)
    body = obj.get()['Body'].read()
    return body

def get_case_info(soup):
    try:
        # get case summary table
        summary_table = str(soup.find('div', class_ = 'ssCaseDetailCaseNbr').find_next('table'))
        summary_table = pd.DataFrame([summary_table], columns = ['parsed'])

        return summary_table

    except AttributeError:
        print('no summary table')
        return pd.DataFrame()

    except Exception as e:
        logging.error(e, exc_info=True)

def get_related_cases(soup):
    try:
        related_cases_table = str(soup.find(text=re.compile(r'Related Case Information')).find_parent('table'))
        related_cases_table = pd.DataFrame([related_cases_table], columns=['parsed'])

        return related_cases_table

    except AttributeError:
       # print('no related cases')
        return pd.DataFrame()

    except Exception as e:
        logging.error(e, exc_info=True)


def get_parties(soup):
    try:
        party_information_table = str(soup.find(text=re.compile(r'Party Information')).find_parent('table'))
        party_information_table = pd.DataFrame([party_information_table], columns = ['parsed'])

        return party_information_table

    except AttributeError:
        print('no party information')
        return pd.DataFrame()

    except Exception as e:
        logging.error(e, exc_info=True)


def get_disposition(soup):
    try:                
        disp_rows = soup.find_all('td', attrs = {'headers' : 'CDisp'})
        disp_row_list = [str(x.find_parent('tr')) for x in disp_rows]
        disp_table = pd.DataFrame(disp_row_list, columns = ['parsed'])

        return disp_table

    except AttributeError:
        print('no disposition information')
        return pd.DataFrame()

    except Exception as e:
        logging.error(e, exc_info=True)



# Extract Information for Other Events and Hearings Table
def get_other_events(soup):
    try:
        # find all Other Events and Entry Rows by the header in the td elements in the table (this also removes the disposition information, if present)
        event_entries = soup.find_all('td', attrs = {'headers' : 'COtherEventsAndHearings'})
        event_list = [x.find_parent('tr') for x in event_entries]
        event_table = pd.DataFrame([str(x) for x in event_list], columns = ['parsed'])

        return event_table

    except AttributeError:
        print('no events information')
        return pd.DataFrame()

    except Exception as e:
        logging.error(e, exc_info=True)


def get_financial_info(soup):
    try:
        # find all Other Events and Entry Rows by the header in the td elements in the table (this also removes the disposition information, if present)
        financial_information_table = str(soup.find(text=re.compile(r'Financial Information')).find_parent('table'))
        financial_information_table = pd.DataFrame([financial_information_table], columns = ['parsed'])

        return financial_information_table

    except AttributeError:
        print('no financial information')
        return pd.DataFrame()

    except Exception as e:
        logging.error(e, exc_info=True)


def parse_html(file, 
               output_dir,
               bad_strings,
               base_url,
               select_text,
               link_text
               ):    
    
    df_list = {}

    try:
        soup = verify_file(file, 
                           bad_strings,
                           base_url,
                           select_text,
                           link_text)
        
        file_name = os.path.basename(file).replace('.html', '')
        case_num = soup.find('div' , class_ = 'ssCaseDetailCaseNbr').get_text(strip=True).replace('Case No.', '')

        tables = ['case_info', 'parties', 'disposition', 'other_events', 'financial_info', 'related_cases']

        for table in tables:
            get_function = eval('get_' + table)
            df_list.update({table : get_function(soup)})

        for key, value in df_list.items():
         #   print(len(value.index))
            if len(value.index) > 0:
                value = value.assign(file_name = file_name)
                value = value.assign(case_num = case_num)

                # write out individal tables for each case HTML
                value.to_csv('{2}/{1}/{0}.csv'.format(re.sub(r"[^a-zA-Z0-9]","_", file_name), key, output_dir), index=False)        

        return df_list
    except KeyboardInterrupt:
        print('keyboard interrupt')
    except Exception as e:
        logging.error(e, exc_info=True)
        print(file)
        print(e)
              


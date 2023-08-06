#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open Acess Technology Provier: Scrape civil case URLs

@author: lsc
"""

from bs4 import BeautifulSoup as bs
import pandas as pd
import re, os, sys, logging
from requestium import Session, Keys, Select
import datetime 

#sys.path.append('/home/lsc/SiteMonitor/')
sys.path.append('C:/Users/bernsteind/Documents/SiteMonitor/')
import site_monitor

sys.path.append('C:/Users/bernsteind/Documents/scraper/')
from scraper.scraper import setup_driver, setup_dirs, tidy_split


def pass_landing(sess, 
              sm,
              base_url='http://icms.cc-courts.org/iotw/default.asp',
          #    select_text='C - Concord Civil',
              landing_submit='NOTHING1234567',
              select_element="courtcode"              
              ):
    t0=datetime.datetime.now()
    sess.driver.get(base_url)   
    duration=datetime.datetime.now()-t0
    sm.track_request(duration, 'base')

    t0=datetime.datetime.now()
    sess.driver.ensure_element_by_name(landing_submit).ensure_click()
    duration=datetime.datetime.now()-t0
    sm.track_request(duration, 'login')
    

def pass_logIn(sess,
               sm,
               next_submit='submit'):
    # just have to 'log in' to one court, then we can navigate to any of the courts' query pages
    t0=datetime.datetime.now()
    sess.driver.ensure_element_by_name(next_submit).ensure_click()
    duration=datetime.datetime.now()-t0
    sm.track_request(duration, 'pass_page')
    

def pass_calendar(sess,
                  sm,
                  calendar_submit="Calendar Search"):
    t0=datetime.datetime.now()
    sess.driver.ensure_element_by_css_selector("input[type='submit'][value='{0}']".format(calendar_submit)).ensure_click()
    duration=datetime.datetime.now()-t0
    sm.track_request(duration, 'calendar')
   

def query_website(sess, 
                  query_url, 
                  sm):
    # get to the query pages
    res = sess.get(query_url)
    sm.track_request(res, 'query')

    return res


def get_resultCount(res, date, write=False):
    result_count = res.xpath('/html/body/font/small').extract_first()
    if 'There are no cases scheduled' in result_count:
        result_count = '0'
    else:
        regex = re.compile(': (\d+)')
        result_count=regex.findall(result_count)[0]

    if write:
        output_file = query_type + "/logs/resultCount.txt"
        with(open(output_file, 'a')) as f:
            f.write('{0}\n'.format(', '.join([date, result_count])))

    return result_count


def get_resultsTable(res, resultCount, date, write=False):
    if resultCount != '0':
        soup = bs(res.content)
        caseUrls = soup.find_all('a', attrs = {'href': re.compile(r'casenumber=')})
    
        case_href = []
        case_num = []
        for x in caseUrls:
            case_href.append(x['href'])
            case_num.append(x.text.strip())
        case_id_df = pd.DataFrame(zip(case_href, case_num), columns = ['case_href', 'Case Number'])
    
        result_table=pd.read_html(res.xpath('/html/body/table[3]').extract_first())[0]
        result_table.columns = ['Time', 'Category' , 'Case Number', 
                                'Case Name', 'Description', 'Hearing']
        result_table = result_table[~result_table.Time.str.contains("Time")]
        result_table = pd.merge(result_table, case_id_df, on='Case Number')
        # some rows are duplicated when converted to table form with pd.read_html, so we drop duplicate rows (all columns must be the same)
        result_table=result_table.drop_duplicates()
        
        if write:
            output_file = query_type + "/case_info/{0}.txt".format(date)
            result_table.to_csv(output_file, mode = "a", header=False,index=False)
    else:
        result_table=pd.DataFrame()
    
    return result_table

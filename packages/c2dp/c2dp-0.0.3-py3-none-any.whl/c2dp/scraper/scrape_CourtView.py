# -*- coding: utf-8 -*-
"""

Scrape Alaska: https://records.courts.alaska.gov/eaccess/home.page.2

Query limit: 500

@author: bernsteind
"""

from bs4 import BeautifulSoup as bs
import os, sys
import pandas as pd
import numpy as np
from itertools import product
from string import ascii_lowercase, digits
import datetime
import logging
import itertools

from requestium import Session, Keys, Select

sys.path.append('C:/Users/bernsteind/Documents/SiteMonitor/')
#sys.path.append('/home/lsc/SiteMonitor/')
import site_monitor

sys.path.append('C:/Users/bernsteind/Documents/scraper/')
from scraper.scraper import setup_driver, setup_dirs, tidy_split



def setup_siteMonitor(categories=['pass_page', 'change_tab', 'submit_query', 'change_page'],
                      burn_in=20):
    sm = site_monitor.SiteMonitor(categories=categories, burn_in=burn_in)
    return sm

def pass_page(sess,
              base_url,
              sm,
              button_class="anchorButton"):
    # get past the first page
    print('started getting past first page')
    sess.driver.get(base_url)
    button = sess.driver.ensure_element_by_class_name(button_class)
    t0=datetime.datetime.now()
    button.click()
    duration=datetime.datetime.now()-t0
    sm.track_request(duration, 'pass_page')
    print('finished getting past first page')
    

def change_to_tab(sess,
                  sm,
                  tab_xpath='//*[@id="id1d"]/div[1]/ul/li[2]/a'):
    name_tab_el = sess.driver.ensure_element_by_xpath(tab_xpath)
    t0=datetime.datetime.now()
    name_tab_el.click()
    duration=datetime.datetime.now()-t0
    sm.track_request(duration, 'change_tab')
    

def get_caseTypes(sess):
    caseType_el = sess.driver.ensure_element_by_name('caseCd')
    options = [x for x in caseType_el.find_elements_by_tag_name("option")]
    caseTypes_list = [i.text for i in options]
    
    return caseTypes_list


def set_resultShow(sess, resultShow):
        # change display from 25 to 75 to make the number of page turns fewer
    result_display_el = sess.driver.ensure_element_by_name('bodyLayout:topSearchPanel:pageSize')
    #webdriver.find_element_by_name('bodyLayout:topSearchPanel:pageSize')
    result_display_el.send_keys(resultShow)


def set_startDate(sess, startDate):
    start_date_el = sess.driver.ensure_element_by_id("id4a")
   # start_date_el = date_el_parent[0]
    start_date_el.clear()
    sess.driver.execute_script("arguments[0].setAttribute('value','{0}')".format(startDate), start_date_el)


def set_endDate(sess, endDate):
    end_date_el = sess.driver.ensure_element_by_id("id4c")
    end_date_el.clear()
    sess.driver.execute_script("arguments[0].setAttribute('value','{0}')".format(endDate), end_date_el)


def set_caseType(sess, caseType):
    select_el = Select(sess.driver.ensure_element_by_name('caseCd'))
    select_el.select_by_visible_text(caseType)


def set_lastName(sess, lastName):    
    last_name_el = sess.driver.ensure_element_by_xpath("//*[contains(text(), 'Last Name')]/following-sibling::input")
    last_name_el.clear()
    sess.driver.execute_script("arguments[0].setAttribute('value','{0}')".format(lastName), last_name_el)
    

def set_firstName(sess, firstName):
    first_name_el = sess.driver.find_element_by_xpath("//*[contains(text(), 'First Name')]/following-sibling::input")
    first_name_el.clear()
    sess.driver.execute_script("arguments[0].setAttribute('value','{0}')".format(firstName), first_name_el)


def submit_query(sess, sm):
    submit_el = sess.driver.ensure_element_by_name('submitLink')
    t0=datetime.datetime.now()
    submit_el.ensure_click()
    duration=datetime.datetime.now()-t0
    sm.track_request(duration, 'submit_query')
    

def set_caseNumber(sess, caseNumber):
    caseNumber_el = sess.driver.ensure_element_by_id("caseDscr")
    caseNumber_el.clear()
    caseNumber_el.send_keys(caseNumber)
    

def check_numResults(sess, query_type, row):
    sess.driver.ensure_element_by_xpath("//*[contains(text(), 'Search Results')]")
    
    link_els = bs(sess.driver.page_source).find_all('td', attrs = {'class' : 'bookmarkablePageLinkPropertyColumnLink'})
    link_list = [link.find_next('a')['href'] for link in link_els]
    num_links = len(set(link_list))
    
    if num_links != 1:
        with open(query_type + "/logs/multiple_results.txt", "a") as file:
            file.write(row['case_number'])
            
    return num_links

def get_case_page(sess, sm, table_element='grid'):
            
    t0=datetime.datetime.now()
    sess.driver.ensure_element_by_class_name('bookmarkablePageLinkPropertyColumnLink').ensure_click()
    duration=datetime.datetime.now()-t0
    sm.track_request(duration, 'change_page')


def get_queryString(row, query_vars):
    queryString = '_'.join(row[query_vars])
    return queryString

def get_recordCount(sess, 
                    query_type,
                    queryString,
                    write=True):
    # keeping the record of number of results outside the loop because we only need to capture it once per query
    element_results = sess.driver.ensure_element_by_class_name("feedback")
    num_results = element_results.text
    
    if write:
        output_file = query_type + '/logs/record_count.txt'
        with open(output_file, "a") as file:
            file.write('{0},{1}\n'.format(queryString, num_results))

    
    return num_results  
    










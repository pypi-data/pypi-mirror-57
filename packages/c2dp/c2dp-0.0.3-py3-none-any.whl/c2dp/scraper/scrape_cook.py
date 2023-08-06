# -*- coding: utf-8 -*-
"""
Functions to scrape Cook County, IL case website

@author: bernsteind
"""
from bs4 import BeautifulSoup as bs
import numpy as np
import re, sys
import boto3
import datetime
import pandas as pd

from selenium.webdriver.common.action_chains import ActionChains


def get_query_page(sess, url, sm):
    t0 = datetime.datetime.now()
    sess.driver.get(url)
    duration = datetime.datetime.now() - t0
    sm.track_request(duration, 'pass_page')
    

def set_division(sess, division_text):
    el = sess.driver.ensure_element_by_xpath('//*[@id="ctl00_MainContent_ddlDatabase_Input"]')
    el.clear()
    el.send_keys(division_text)


def get_case_types(sess):
    print('collecting case types...')
    selection_page = bs(sess.driver.page_source).find_all('div', attrs = {'class' : 'makeSmaller'})
    options = [x.text for x in selection_page]

    return options


def set_searchType(sess, searchType_text):
    el = sess.driver.ensure_element_by_xpath('//*[@value="{0}"]'.format(searchType_text))
    el.ensure_click()

def set_filingDate(sess, date):
    el = sess.driver.ensure_element_by_id('ctl00_MainContent_dtFilingDate')    
    el.clear()
    el.send_keys(date)
    
    
def submit_query(sess, sm):
    t0 = datetime.datetime.now()
    sess.driver.ensure_element_by_id('ctl00_MainContent_btnSearch').ensure_click()
    duration = datetime.datetime.now() - t0
    sm.track_request(duration, 'query')


def generate_queryString(division_text, filingDate):
    queryString = '_'.join([division_text, filingDate])
    
    return queryString


def set_caseNumber(sess, year, code, number):
    year_el = sess.driver.ensure_element_by_id('ctl00_MainContent_txtCaseYear')

    code_el = sess.driver.ensure_element_by_id('ctl00_MainContent_txtCaseCode')

    number_el = sess.driver.ensure_element_by_id('ctl00_MainContent_txtCaseNumber')
    
    actions = ActionChains(sess.driver)

    actions.click(year_el).send_keys(year).click(code_el).send_keys(code).click(number_el).send_keys(number).perform()


def get_recordCount(sess, 
                    query_type,
                     queryString, 
                     write=True):
    case_num_elements = bs(sess.driver.page_source).find_all( id=re.compile("^MainContent_gvResults_lbDetail"))
    case_num = [el.text for el in case_num_elements]
             
    numResults = len(case_num)
    
    if write:
        output_file = query_type + '/logs/record_count.txt'
        with open(output_file, "a") as file:
            file.write('{0},{1}\n'.format(queryString, numResults))
    
    return case_num


def get_resultTable(sess,
                    query_type,
                    date_output,
                    write=True):
    resultTable = pd.read_html(sess.driver.css('table').extract_first())[0]
    
    if 'There are no cases matching the search criteria in your selected division. If you feel this is an error try your search using the case number if known.' in str(resultTable.iloc[0][0]):
        resultTable = pd.DataFrame()
        
    if (not resultTable.empty) and (write):
        output_file = query_type + "/case_info/{0}.txt".format(date_output)
        resultTable.to_csv(output_file, mode = "a", header=False,index=False)
    return resultTable

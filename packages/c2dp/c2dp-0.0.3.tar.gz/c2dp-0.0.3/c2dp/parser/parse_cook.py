import boto3
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import os

def download_file(s, file_name, bucket='odga'):
    if not os.path.isdir('/tmp'):
        os.makedirs("/tmp")
    local_file = '/tmp/local_copy.html'
    boto3.client('s3').download_file(bucket, file_name, local_file)
    s.driver.get('file://' + local_file)

def verify_file(s, file_name, bad_strings):
    page = s.driver.page_source
    if (any(string in page  for string in bad_strings)) or (page == ''):
        with open('parsing/logs/error_bad_file.out', "a+") as f:
            f.write('{0}\n'.format(file_name))

        return False
    else:
        return True


def get_iframe(s):

    s.driver.switch_to.frame(s.driver.find_element_by_tag_name('iframe'))
    soup = bs(s.driver.page_source)

    return soup


def get_case_number(soup):
    case_num = soup.find('span', attrs={'id': 'lblBottom'}).text
    return case_num


def get_case_info(soup):
    case_info_el = soup.find(text=re.compile(r'Division:')).find_parent('table')
    return case_info_el


def parse_party_info(df):
    df = df.reset_index(drop=True)
    output_dict = {'party_type': df.party[0],
                   'party_names': '___'.join(df.party[1:].dropna()),
                   'attorney_info': '___'.join(df.attorney).lstrip('Attorney(s)___')}

    return output_dict


def get_parties(soup):
    party_table_el = soup.find(text=re.compile(r'Party Information')).find_next('table')
    return party_table_el


def get_activities(soup):
    case_activity_el = soup.find(text=re.compile(r'Case Activity')).find_all_next('table', recursive=False)
    return str(case_activity_el)


def parse_activity_entry(header_table):
    info_table = header_table.find_next('table')

    activity_date, participant = header_table.get_text().strip().split('\n')
    event_header = info_table.find('font').get_text()
    table_els = info_table.find_all('table')
    df_list = [pd.read_html(str(x))[0] for x in table_els if x.get_text() != '']

    event_info_df = pd.concat(df_list)
    event_info_df.columns = ['var', 'value']

    event_info_df['index'] = 0
    event_info_df = event_info_df.pivot(index='index', columns='var', values='value')
    event_dict = event_info_df.to_dict(orient='records')[0]
    event_dict.update({
        'activity_date': activity_date,
        'participant': participant,
        'header': event_header
    })

    return event_dict


def parse_section(table, case_num, soup):
    get_function = eval('get_' + table)
    indiv_dict = {
        'case_num': case_num,
        'parsed': get_function(soup)}

    table_df = pd.DataFrame([indiv_dict])

    return table_df

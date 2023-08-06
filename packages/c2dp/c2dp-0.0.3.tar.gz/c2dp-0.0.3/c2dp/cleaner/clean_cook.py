import pandas as pd
import itertools


def clean_case_info(soup):
    case_info_table = pd.read_html(str(soup))[0].dropna(axis=1)
    l = case_info_table.values.tolist()
    l = list(itertools.chain.from_iterable(l))
    df = pd.DataFrame(l, columns=['a'])

    df[['variable', 'value']] = df.a.str.split(': ', n=1, expand=True)
    df = df.drop(['a'], axis=1)
    df['index'] = 0
    df = df.pivot(index='index', columns='variable', values='value').reset_index(drop=True)

    return df


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return list(zip(a, b))


def clean_parties(soup):
    party_table = pd.read_html(str(soup))[0]
    party_table.columns = ['party', 'x1', 'attorney']
    attorney_rows = party_table.index[party_table.attorney == 'Attorney(s)'].tolist()

    party_df_list = [party_table[pair[0]:pair[1]] for pair in pairwise(attorney_rows + [party_table.shape[0]])]
    parties_dict_list = [clean_party_info(df) for df in party_df_list]
    parties_df = pd.DataFrame(parties_dict_list).reset_index(drop=True)
    return parties_df


def clean_party_info(df):
    df = df.reset_index(drop=True)
    output_dict = {'party_type': df.party[0],
                   'party_names': '___'.join(df.party[1:].dropna()),
                   'attorney_info': '___'.join(df.attorney).lstrip('Attorney(s)___')}

    return output_dict


def clean_activities(soup):
    case_activity_el = [x.find_parent('table') for x in soup.find_all(text=re.compile(r'Activity Date'))]
    event_dict_list = [clean_activity_entry(table) for table in case_activity_el]
    df = pd.DataFrame(event_dict_list)
    return df


def clean_activity_entry(header_table):
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


def clean_section(table, case_num, soup):
    clean_function = eval('clean_' + table)
    indiv_dict = {
        'case_num': case_num,
        'clean' : clean_function(soup)}

    table_df = pd.DataFrame([indiv_dict])

    return table_df

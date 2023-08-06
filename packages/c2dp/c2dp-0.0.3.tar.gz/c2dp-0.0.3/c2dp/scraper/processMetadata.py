# -*- coding: utf-8 -*-
"""
Functions to combine and deduplicate case metadata

@author: bernsteind
"""

import glob, os , re
import pandas as pd
import pathlib


def setup_dirs(input_dir='', root=''):
    if root:
        output_dir = 'metadata'
    else:
        output_dir = input_dir + '/metadata'

    for i in ['/all_metadata', '/unique_metadata', '/clean_metadata']:
        if not os.path.exists(output_dir + i):
            pathlib.Path(output_dir + i).mkdir(parents=True)

def combine_metadata_files(input_dir,
                           col_names='', 
                           date_structure=r'\d{4}-\d{2}-\d{2}', 
                           file_name=False,
                           root=True):
    """
    Combine multiple metadata txt files into a single txt file

    Params
    ------
    input_dir : str
        the directory to the files that will be combined. The input directory must contain a sub-directory called `case_info` that contains 
        text files containing the case metadata
    output_dir : str
        the directory to which the output will be written
    col_names : list
        the names of all columns in each file in the input_dir (the function assumes that all files have the same columns)
    date : bool
        boolean of whether to extract a date from each file's base name to append to each row. This is helpful when the metadata does not contain
        the date filed
    root : bool
        boolean of whether to write metadata files to the top-level root directory where the command is executed, or to the input directory path

    Returns
    -------
    pandas.DataFrame
        Returns a dataframe with the same columns as the data.frame in `metadata_file`. The dataframe is written to `output_file`
    """
    
    file_list = list(pathlib.Path(input_dir).glob('**/case_info/*.txt'))
    
  #  glob.glob(input_dir + '/*/case_info/*.txt') 
    if root: 
        output_dir = 'metadata'
    else:
        output_dir = input_dir + '/metadata'

    output_file = '{0}/all_metadata/{1}_all_metadata_raw.txt'.format(output_dir, input_dir.replace('/','_'))
        
    # loop through the files within each directory and append to a single file
    for file in file_list:
        if col_names:
            df = pd.read_csv(file, names=col_names)
        else:
            df = pd.read_csv(file)
        # extract the date
        if date_structure:
            df['filename'] = re.search(date_structure, os.path.basename(file)).group() 
        if file_name:
            df['name2var'] = str(input_dir).rsplit('/', 1)[-1]
 
     #   df=df.applymap(lambda x: str(x).replace('Â', ''))
        if os.path.exists(output_file):
            df.to_csv(output_file, mode = 'a',header=False,index=False)
        else:
            df.to_csv(output_file, mode = 'a',header=True,index=False)

        

# deduplicate the civil metadata
def get_unique_metadata(input_dir, 
                        dup_index, 
                        col_names='',
                        root=True, 
                        merge_files=True):
    """
    Deduplicate a file based on the values of 'dup_index'

    Params
    ------
    metadata_file : str
        the path to the file containing all metadata, the metadata file should contain a pandas data.frame object
    col_names : list
        the names of all columns in the metadatafile
    date_var : list
        the variable name to arrange values by before removing duplicates (we only keep the first one)
    dup_index : list
        the name(s) of the column(s) to use to deduplicate the data.frame
    root : bool
        boolean of whether to write metadata files to the top-level root directory where the command is executed, or to the input directory path
    merge_files : bool
        boolean of whether to combine multiple files in the 'unique_metadata' folder into one file one level up in the directory
        
    Returns
    -------
    pandas.DataFrame
        Returns a dataframe with the same columns as the data.frame in `metadata_file`. The dataframe is written to `output_file`
    """

    if root:
        metadata_path = 'metadata/all_metadata/{0}_all_metadata_raw.txt'.format(input_dir.replace('/','_'))
    else:
        metadata_path = input_dir + '/metadata/{0}_all_metadata_raw.txt'.format(input_dir.replace('/','_'))
        
    if col_names:
        all_metadata = pd.read_csv(metadata_path, names=col_names)
    else:
        all_metadata = pd.read_csv(metadata_path)
    
    unique_metadata = all_metadata.drop_duplicates(subset = dup_index) 
    
    output_file = metadata_path.replace('all', 'unique')
    unique_metadata.to_csv(output_file, header=True,index=False)
    

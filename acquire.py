'''This module provides functions that help acquire 5 different types of dataframes'''

# General imports for working on the notebook on this exercise

import pandas as pd
import requests
import os

# Putting the function together for reproduction

def get_api_data(endpoint):
    '''
    Using a for loop to get each page from
    the data via url until last page.
    Stops the loop when request gets a None
    at the end of the pages
    '''
    
    # API parameters setup and entry check
    if endpoint not in ['items', 'stores', 'sales']:
        return "Entry not for API. Check documentation with: response = requests.get(base_url + /documentation))"
    host = "https://python.zgulde.net/"
    api = "api/v1/"
    url = host + api + endpoint
    response = requests.get(url)
    # Endpoint must only be 'stores', 'items', or 'sales'
    if response.ok:
        payload = response.json()["payload"]
        contents = payload[endpoint]
        df = pd.DataFrame(contents)
        next_page = payload["next_page"]
        # Loading content page after page into a df then printing the process
        while next_page:
            url = host + next_page
            response = requests.get(url)
            payload = response.json()["payload"]
            next_page = payload["next_page"] 
            print(f'\rGetting page {payload["page"]} of {payload["max_page"]}: {url}', end='')      
            contents = payload[endpoint]
            df = pd.concat([df, pd.DataFrame(contents)])
            df = df.reset_index(drop=True) 
    return df


# This function allows the user to retrieve
# the local items_df obtained from the link above
def get_local_items_df():
    if os.path.exists('items_df.csv'):
        return pd.read_csv('items_df.csv')
    df = get_api_data('items_df')
    df.to_csv('items_df.csv', index=False)
    return df


# This function allows the user to retrieve
# the local stores_df obtained from the link above
def get_local_stores_df():
    if os.path.exists('stores_df.csv'):
        return pd.read_csv('stores_df.csv')
    df = get_api_data('stores_df')
    df.to_csv('stores_df.csv', index=False)
    return df


# This function allows the user to retrieve
# the local sales_df obtained from the link above
def get_local_sales_df():
    if os.path.exists('sales_df.csv'):
        return pd.read_csv('sales_df.csv')
    df = get_api_data('sales_df')
    df.to_csv('sales_df.csv', index=False)
    return df

# This function allows the user to retrieve
# the local sales df obtained from the link above
def get_local_sales():
    if os.path.exists('sales.csv'):
        return pd.read_csv('sales.csv')
    df = get_api_data()
    df.to_csv('sales_df.csv', index=False)
    return df


#################################################################
# This function creates and retrieves the sales data

def get_sales():
    '''
    This function retrieves 3 different df obtained
    in the setup part of the function, then transforms
    the sales_df dfto allow for concatnation and then
    returns a df from all 3
    '''
def get_sales_data():
    # Setup
    items_df = get_api_data('items_df')
    stores_df = get_api_data('stores_df')
    sales_df = get_api_data('sales_df')

    sales_df.rename(columns={'item': 'item_id', 'store': 'store_id'}, inplace=True)

    df = pd.merge(sales_df, items_df, how='left', on='item_id')
    df = pd.merge(df, stores_df, how='left', on='store_id')
    return df


#################################################################
# This function gets the opsd_germany data

def get_opsd_germany():
    if os.path.exists('opsd.csv'):
        return pd.read_csv('opsd.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv('opsd.csv', index=False)
    return df

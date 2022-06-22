'''This module provides functions that help acquire 5 different types of dataframes'''

# General imports for working on the notebook on this exercise

import pandas as pd
import requests
import os

# This function gets the items dataframe
def get_items():
    '''
    Using a for loop to get each page from
    the data via url until last page.
    Stops the loop when request gets a None
    at the end of the pages
    '''
    # Setting up variables
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/items'
    items = []
        
    for i in endpoint:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        items.extend(data['payload']['items'])
        endpoint = data['payload']['next_page']
        if endpoint == None:
            break
    return pd.DataFrame(items)

# This function gets the store data

def get_stores():
    '''
    Using a for loop to get each page from
    the data via url until last page.
    Stops the loop when request gets a None
    at the end of the pages
    '''
    # Setup
    domain = 'https://api.data.codeup.com'
    endpoint = '/api/v1/stores'
    stores = []
    for i in endpoint:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        stores.extend(data['payload']['stores'])
        endpoint = data['payload']['next_page']
        if endpoint == None:
            break
    return pd.DataFrame(stores)


# This function gets the sales data

def get_sales():
    '''
    Using a for loop to get each page from
    the data via url until last page.
    Stops the loop when request gets a None
    at the end of the pages
    '''
    # Setup
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/sales'
    sales = []
    for i in endpoint:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        sales.extend(data['payload']['sales'])
        # Update the endpoint
        endpoint = data['payload']['next_page']
        if endpoint == None:
            break
    return pd.DataFrame(sales)


# This function gets the opsd_germany data

def get_opsd_germany():
    if os.path.exists('opsd.csv'):
        return pd.read_csv('opsd.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv('opsd.csv', index=False)
    return df


# This function gets any data regardless
# of its endpoint for this exercise

def get_api_data():
    '''
    Using a for loop to get each page from
    the data via url until last page.
    Stops the loop when request gets a None
    at the end of the pages
    '''
    # Setup
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/sales'
    sales = []
    for i in endpoint:
        url = domain + endpoint
        response = requests.get(url)
        data = response.json()
        sales.extend(data['payload']['sales'])
        # Update the endpoint
        endpoint = data['payload']['next_page']
        if endpoint == None:
            break
    return pd.DataFrame(sales)

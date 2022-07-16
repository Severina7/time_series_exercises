# Ignoring warning messages from python
import warnings
warnings.filterwarnings('ignore')

# General use imports
import pandas as pd
import numpy as np

# Modules and data
import acquire
from datetime import datetime

def prep_sales_data(df):
    df.sale_date = pd.to_datetime(df.sale_date)
    sales1 = df.set_index('sale_date').sort_index()
    sales1['month']  = sales1.index.strftime('%m %b, %Y')
    sales1['day_of_week'] = sales1.index.strftime('%a %b %d, %Y')
    sales1['sales_total'] = sales1.sale_amount * sales1.item_price
    return df


def prep_opsd_data(df):
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date').sort_index()
    df['month'] = df.index.strftime('%m-%b')
    df['year'] = df.index.strftime('%Y')
    df = df.replace(np.nan, 0)
    df['Wind_and_Solar'] = df.Wind + df.Solar
    return df
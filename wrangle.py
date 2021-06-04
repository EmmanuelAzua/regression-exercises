import scipy.stats as stats
from pydataset import data
import os
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env
from env import username, password, host




def get_connection(db, user=username, host=host, password=password):
    '''
    This function makes a connection with and pulls from the CodeUp database. It 
    takes the database name as its argument, pulls other login info from env.py.
    Make sure you save this as a variable or it will print out your sensitive user
    info as plain text. 
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def telco_churn_data():
    '''
    This function pulls the telco_churn dataset and turns it into a python-ready dataframe,
    '''
    # Wrap the process of creating a SQL query into python function structure
    sql_query = '''select *
    from customers
    join contract_types using(contract_type_id)
    join internet_service_types using(internet_service_type_id)
    join payment_types using(payment_type_id)'''
    # Returns the SQL dataset as a python-ready dataframe
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df


def churn_data_csv(cached = False):
    '''
    This function pulls in the telco_churn database, saves it as a csv file, and returns a pandas dataframe
    '''
    if cached == False or os.path.isfile('telco_churn.csv') == False:
        df = telco_churn_data()
        df.to_csv('telco_churn_df.csv')
    else:
        df = pd.read_csv('telco_churn_df.csv', index_col=0)
    return df
# transformations.py contains all the transformation functions used to process the inputted dataset.

import pandas as pd

#Transformation 1
'''
Drop all unnecessary columns from the dataset: ['name', 'email', 'phone-number', credit_card']
These columns were determined to not be needed for further analysis.
'''
def drop_columns(df):
    df = df.drop(['name', 'email', 'phone-number', 'credit_card'], axis = 1)
    return df

#Transformation 2
'''
Change the data type of certain columns to string to fit their categorical or descriptive nature.
Columns to be changed: ['is_canceled', 'arrival_date_year', 'arrival_date_week_number', 'arrival_date_day_of_month', 'is_repeated_guest', 'agent', 'company']
'''
def change_to_string(df):
    df['is_canceled'] = df['is_canceled'].astype(str)
    df['arrival_date_year'] = df['arrival_date_year'].astype(str)
    df['arrival_date_week_number'] = df['arrival_date_week_number'].astype(str)
    df['arrival_date_day_of_month'] = df['arrival_date_day_of_month'].astype(str)
    df['is_repeated_guest'] = df['is_repeated_guest'].astype(str)
    return df

#Transformation 3
'''
Add an 'A-'at the beginning of each value in the 'agent' column and 'C-' in the 'company' column to differentiate the two.
Combine the 'agent' and 'company' columns into one column called 'booked_through'.
Fill any null values in the 'booked_through' column with 'nan'.
This is because of the exclusive nature between the two columns. A booking is either made with via an agent or a company.
'''
def combine_columns(df):
    df['agent'] = df['agent'].apply(lambda x: f"A-{int(x)}" if pd.notnull(x) else x)
    df['company'] = df['company'].apply(lambda x: f"C-{int(x)}" if pd.notnull(x) else x)
    df['booked_through'] = df['agent'].combine_first(df['company'])
    df = df.drop(['agent', 'company'], axis=1)
    return df

#Transformation 4
'''
Drop all remaining rows with null values in the dataset.
'''
def drop_nulls(df):
    df = df.dropna()
    return df

#Transformation 5
'''
Change the data type of the 'children' column to an integer as there cannot be a fraction of a child.
'''
def change_to_int(df):
    df['children'] = df['children'].astype(int)
    return df

#Transformation 6
'''
Replace all 'Undefined' values in the 'meal' column with 'SC' which were determined to be the same values.
'''
def replace_undefined(df):
    df['meal'] = df['meal'].replace('Undefined', 'SC')
    return df

# etl.py contains the ETL pipeline.
# The ETL pipeline takes the dataset as its input, processes and applies the transoformations from transformations.py, and loads it into a .csv file.

import pandas as pd

from transformations import drop_columns, change_to_string, combine_columns, drop_nulls, change_to_int, replace_undefined

#Extract
df = pd.read_csv('hotel_booking.csv')

#Transform
function_sequence = [drop_columns, change_to_string, combine_columns, drop_nulls, change_to_int, replace_undefined]

for i in function_sequence:
    df = i(df)

#Load
df.to_csv('processed_hotel_bookings.csv', index = False)
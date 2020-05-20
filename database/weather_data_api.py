'''
DOCUMENTATION:
This is for downloading weather data at ulat.asti.dost.gov.ph:8080 (local).
The script converts the weather data in PST insted of UTC. Hence the weather
data can be accessed in the timeframe of the Philippines

From the website, data is uploaded every 8:00am (PST)

ex.
weather data for May 15 (UTC) is uploded at:
2020-05-16 08:00 (PST) --> weather_00181271_20200515.csv (UTC-based csv)

   -which means weather_00181271_20200515.csv only contains May 15 data from:
    8:00AM PST (20200515000000 UTC) - 23:59PM PST (20200515165900 UTC)
 
The other missing 8 hours can be obtained in:
2020-05-15 08:00 (PST) --> weather_00181271_20200514.csv (UTC-based csv)

    -wherein the remaining hours is from:
    00:00MN PST (20200514160000 UTC) to 7:59AM PST (20200514235900 UTC)
    
*note the UTC format is in YYYYMMDDHHMMSS

For integration in other python codes, comment out inputs and execute section
'''

import data_pipeline as dp
import requests as req
import pandas as pd
import numpy as np
import csv
import os

def extract_from_csv(poteka_type, station_id, year, month, data, date, file_path):
    date_shift = "{:02d}".format(int(date) - 1)
    
    with req.Session() as s:
        user = 'kyle'
        password = 'kyle-esg@12[3]4'
        
        #extract 8:00am - 11:59pm
        url = f"http://ulat.asti.dost.gov.ph:8080/{poteka_type}/{station_id}/{year}/{month}/{data}/{data}_{station_id}_{year}{month}{date}.csv"
        download = s.get(url, auth = (user, password))
        decoded_content = download.content.decode('utf-8')
        upper_half = pd.DataFrame(csv.reader(decoded_content.splitlines(), delimiter=','))
        max_range = upper_half.index[upper_half[1] == f'{year}{month}{date}160000'].astype(int)[0]
        upper_half = upper_half.drop(upper_half.index[max_range:len(upper_half)])
        
        #adjust UTC to PST of upper half
        for row in range(len(upper_half[1])):
            upper_half.loc[row,1] = str(int(upper_half.loc[row, 1]) + 80000)
        
        #extract 00:00mn - 7:59am
        url = f"http://ulat.asti.dost.gov.ph:8080/{poteka_type}/{station_id}/{year}/{month}/{data}/{data}_{station_id}_{year}{month}{date_shift}.csv"
        download = s.get(url, auth = (user, password))
        decoded_content = download.content.decode('utf-8')
        lower_half = pd.DataFrame(csv.reader(decoded_content.splitlines(), delimiter=','))
        min_range = lower_half.index[lower_half[1] == f'{year}{month}{date_shift}160000'].astype(int)[0]
        length = len(lower_half)
        lower_half = lower_half.drop(lower_half.index[:min_range])
        
        #adjust UTC to PST of lower half
        for row in range(min_range, length):
            min_sec = lower_half.loc[row, 1][-4:]
            hour_shift = f'0{str(int(lower_half.loc[row, 1][-6:-4]) - 16)}'
            lower_half.loc[row,1] = f'{year}{month}{date}{hour_shift}{min_sec}'


    #combine into single dataframe and fix headers                                                        
    weather_data = lower_half.append(upper_half).reset_index()
    weather_data = weather_data.drop(['index'], axis = 1)
    clean_data = dp.vis_data()
    weather_data = clean_data.fix_headers(weather_data)
    
    # print(weather_data)
    weather_data.to_csv(f'{file_path}/{station_name}.csv')
    print(f'{station_name} saved to {file_path}')
    return weather_data
     

#input station data needed
poteka_type = 'P-POTEKA' #all caps only
# station_id = '00181271' #all caps only
# station_name = 'QCSHS'
year = '2020'
month = '05' #dates and months have to be 2 digits
data = 'weather' 
date = '06'
file_path = 'D:/ULAT/Data/May_6 (heat index)' #change file path as needed

#execute functions
# weather_data = extract_from_csv(poteka_type,station_id, year, month, data, date, file_path)

stations = pd.read_csv('C:/Users/Jeckow236/Desktop/Taal Lightning Data/p-poteka-coordinates.csv')
stations = stations[['Station Name', 'Station Code']]

for index, row in stations.iterrows():
    station_name = row['Station Name']
    station_id = row['Station Code']
    
    weather_data = extract_from_csv(poteka_type, f'00{station_id}', year, month, data, date, file_path)
    
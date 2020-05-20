'''
This is for downloading VLF data only at ulat.asti.dost.gov.ph:8080 (local).
Downloading data weather from the local serverdata from poteka weather data is
separated in a different API

For integration in other python codes, comment out inputs and execute section
'''
import requests as req
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import csv
import os

#returns name in specific directory
def filenames(poteka_type, station_id, year, month, data, date):
    user = 'kyle'
    password = 'kyle-esg@12[3]4'
    url = f"http://ulat.asti.dost.gov.ph:8080/{poteka_type}/{station_id}/{year}/{month}/{data}"
    resp = req.get(url, auth = (user, password))
    soup = BeautifulSoup(resp.text, 'lxml')
    file_link = []
    date_shift = str(int(date) - 1)
  
    
    #get filenames with specific year, time, and date
    for link in soup.find_all('a'):  
        
        if f"{data}_{station_id}_{year}{month}{date_shift}16" in str(link):
            file_link.append(link.get('href'))
            
        elif f"{data}_{station_id}_{year}{month}{date_shift}17" in str(link):
            file_link.append(link.get('href'))
            
        elif f"{data}_{station_id}_{year}{month}{date_shift}18" in str(link):
            file_link.append(link.get('href'))
            
        elif f"{data}_{station_id}_{year}{month}{date_shift}19" in str(link):
            file_link.append(link.get('href'))
            
        elif f"{data}_{station_id}_{year}{month}{date_shift}20" in str(link):
            file_link.append(link.get('href'))
            
        elif f"{data}_{station_id}_{year}{month}{date_shift}21" in str(link):
            file_link.append(link.get('href'))
            
        elif f"{data}_{station_id}_{year}{month}{date_shift}22" in str(link):
            file_link.append(link.get('href'))
            
        elif f"{data}_{station_id}_{year}{month}{date_shift}23" in str(link):
            file_link.append(link.get('href'))
        
        if f'{data}_{station_id}_{year}{month}{date}16' in str(link):
            break
        
        if f"{data}_{station_id}_{year}{month}{date}" in str(link):
            file_link.append(link.get('href'))
    
    return file_link


#downloading csvs
def download_csv(file_path, poteka_type, station_id, station_name, year, month, data, date, files_list):
    print('Downloading csv files...')
    date_shift = str(int(date) - 1)
    user = 'kyle'
    password = 'kyle-esg@12[3]4'
    
    #Change where the filed is saved here
    os.mkdir(f'{file_path}/{station_name}')
    
    #renaming csvs before saving
    with req.Session() as s:
        for file in files_list:
            url = f"http://ulat.asti.dost.gov.ph:8080/{poteka_type}/{station_id}/{year}/{month}/{data}/{file}"
            download = s.get(url, auth = (user, password))
            decoded_content = download.content.decode('utf-8')
            convert = pd.DataFrame(csv.reader(decoded_content.splitlines(), delimiter=','))
            
            if f"{data}_{station_id}_{year}{month}{date_shift}" in file:
                file = "{0}_{1}_{2}{3}{4}{5:02d}{6}".format(data, station_id, year, month, str(int(date_shift) + 1), int(file[-8:-6]) - 16, file[-6:])
                convert.to_csv(f'{file_path}/{station_name}/{file}', header = None, index = False)
                
            if f"{data}_{station_id}_{year}{month}{date}" in file:
                file = "{0}_{1}_{2}{3}{4}{5:02d}{6}".format(data, station_id, year, month, date, int(file[-8:-6]) + 8, file[-6:])
                convert.to_csv(f'{file_path}/{station_name}/{file}', header = None, index = False)
            
            print(f'{file} saved to local repository')
            

#input station data needed
poteka_type = 'V-POTEKA' #all caps only
station_id = '00173478' #all caps only
station_name = 'UPLB'
year = '2020'
month = '01' #dates and months have to be 2 digits
data = 'vlf' 
date = '12'
file_path = 'D:/ULAT/Data/May_15(Ambo)' #change file path as needed

#execute functions
files_list = filenames(poteka_type,station_id, year, month, data, date)
csv_files = download_csv(file_path, poteka_type, station_id, station_name, year, month, data, date, files_list)
import csv
import requests
from contextlib import closing

class ManagerFile:
    BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
    CONFIRMED = 'time_series_covid19_confirmed_global.csv'
    DEATH = 'time_series_covid19_deaths_global.csv'
    RECOVERED = 'time_series_covid19_recovered_global.csv'
    
    def __init__(self):
        self.fields = [] 
        self.rows = [] 

    def choice_a_filename(self) -> None:
        # date = input('Insert a date from daily reports: ')
        self.filename = f"{self.BASE_URL}{self.CONFIRMED}"

    def load_file_csv(self) -> None:
        url = f"{self.filename}"

        with closing(requests.get(url, stream=True)) as r:
            csvfile = r.iter_lines()
            self.fields = str(next(csvfile)).split(',')
            next(csvfile) 
            for row in csvfile:
                data_row = str(row).replace("b'",'')
                self.rows.append(data_row)  
        # get total number of rows 
        print(f"Total number of rows: {len(self.rows)}") 


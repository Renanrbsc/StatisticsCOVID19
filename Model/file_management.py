import requests
from contextlib import closing
from Data.data_processing import DataProcess
from requests.exceptions import MissingSchema


class ManagerFile:
    BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
    CONFIRMED = 'time_series_covid19_confirmed_global.csv'
    DEATH = 'time_series_covid19_deaths_global.csv'
    RECOVERED = 'time_series_covid19_recovered_global.csv'
    
    def __init__(self):
        self.rows = [] 
        self.fields = [] 
        self._dpross = DataProcess()

    def choice_a_filename(self) -> None:
        # date = input('Insert a date from daily reports: ')
        self.filename = f"{self.BASE_URL}{self.CONFIRMED}"

    def load_file_csv(self) -> None:
        url = f"{self.filename}"
       
        try:
            with closing(requests.get(url, stream=True)) as r:
                csvfile = r.iter_lines()
                
                for row in csvfile:
                    data_row = self._dpross.replace_characters(row, "b'", '')
                    data_row = self._dpross.replace_characters(data_row, "'", '')
                    data_row = self._dpross.replace_characters(data_row, '"', '')
                    list_data_row = self._dpross.convert_string_to_list(data_row)
                    self.rows.append(list_data_row)  
                self.fields = self.rows.pop(0)

                return self.fields, self.rows

        except MissingSchema:
            print("HTTP link appears to be broken!")
            return
            
        finally:
            # get total number of rows 
            print(f"Total number of rows: {len(self.rows)}") 



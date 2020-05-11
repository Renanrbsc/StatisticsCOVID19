import requests
from contextlib import closing
from requests.exceptions import MissingSchema
from app.Treatment.data_processing import DataProcess


class ManagerFile:
    BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
    CONFIRMED = 'time_series_covid19_confirmed_global.csv'
    DEATH = 'time_series_covid19_deaths_global.csv'
    RECOVERED = 'time_series_covid19_recovered_global.csv'
    
    def __init__(self):
        self.filenames = dict()
        self.data_csv = list()
        self.rows = [] 
        self.fields = [] 
        self._dpross = DataProcess()

    def build_update_access(self) -> None:
        self.filenames = {'confirmed':f"{self.BASE_URL}{self.CONFIRMED}",
                          'death':f"{self.BASE_URL}{self.DEATH}",
                          'recovered':f"{self.BASE_URL}{self.RECOVERED}"
                          }

    def load_file_csv(self) -> None:
        for filename in self.filenames:    
            try:
                with closing(requests.get(self.filenames[filename], stream=True)) as r:
                    csvfile = r.iter_lines()
                    
                    for row in csvfile:
                        data_row = self._dpross.replace_characters(row, "b'", '')
                        data_row = self._dpross.replace_characters(data_row, "'", '')
                        data_row = self._dpross.replace_characters(data_row, '"', '')
                        list_data_row = self._dpross.convert_string_to_list(data_row)
                        self.rows.append(list_data_row)  
                    self.fields = self.rows.pop(0)
                    
                    self.data_csv.append([self.fields, self.rows, filename])


            except MissingSchema:
                print("HTTP link appears to be broken!")
                return
                
            finally:
                # get total number of rows 
                print(f"Number of rows updated in the '{filename}' file: {len(self.rows)}") 

        return self.data_csv



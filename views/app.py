# importing csv module 
import sys
sys.path.append(r"C:\Users\renan.ribas\Documents\Github")

import csv 
from StatisticsCOVID19.views.file_management import ManagerFile

class RequestsDataFile:
    def __init__(self):
        self._manager_file = ManagerFile()

    def loading_manager_methods(self):
        self._manager_file.choice_a_filename()
        self._manager_file.load_file_csv()

    def search_the_first_five_countries(self):      
        # printing first 5 rows 
        print('\nFirst 5 rows are:\n') 
        for row in self._manager_file.rows[:5]: 
            # parsing each column of a row 
            for index, column in enumerate(row): 
                print(f"{self._manager_file.fields[index]}: {column}"), 
            print('\n') 

    def search_name_country(self) -> None:
        name_country = input('Search country: ')
        print(f'\nSearch name of country: {name_country}\n') 
        for row in self._manager_file.rows: 
            if name_country == row[3]:
            # parsing each column of a row 
                for index, column in enumerate(row): 
                    print(f"{self._manager_file.fields[index]}: {column}") 
                return 



datafile = RequestsDataFile()
datafile.loading_manager_methods()
datafile.search_name_country()



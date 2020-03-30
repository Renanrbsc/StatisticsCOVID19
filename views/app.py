# importing csv module 
import sys
sys.path.append(r"C:\Users\renan.ribas\Documents\Github")
sys.path.append(r"C:\Users\Usuario\Documents\GitHub\StatisticsCOVID19")

import csv 
from views.file_management import ManagerFile

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
            data = str(row).split(',')
            print(data)
            for index, value in enumerate(self._manager_file.fields):
                print(f"{value}: {data[index]} ")  
            print('\n') 

    def search_name_country(self) -> None:
        name_country = input('Search country: ')
        print(f'\nSearch name of country: {name_country}\n') 
        for row in self._manager_file.rows: 
            if name_country in row:
            # parsing each column of a row 
                data = str(row).split(',')
                for index, value in enumerate(self._manager_file.fields):
                    print(f"{value}: {data[index]} ") 
                return 


datafile = RequestsDataFile()
datafile.loading_manager_methods()
# datafile.search_the_first_five_countries()
datafile.search_name_country()
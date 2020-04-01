# importing csv module 
import matplotlib.pyplot
import sys
sys.path.append(r"C:\Users\renan.ribas\Documents\Github")
sys.path.append(r"C:\Users\Usuario\Documents\GitHub\StatisticsCOVID19")

from Process.file_management import ManagerFile

class RequestsDataFile:
    def __init__(self):
        self._manager_file = ManagerFile()

    def loading_manager_methods(self):
        self._manager_file.choice_a_filename()
        self._manager_file.load_file_csv()

    def search_name_country(self) -> None:
        name_country = input('Search name of country: ')

        for row in self._manager_file.rows: 
            if name_country in row:
                # parsing each column of a row 
                for index, value in enumerate(self._manager_file.fields):
                    print(f"{value}: {row[index]} ") 
                self.simple_graphic(row)
                return 


    def simple_graphic(self, row: list):
        date = self._manager_file.fields[4:]        
        daily_cases = row[4:]

        case = []
        for i in daily_cases:
            daily = int(i)
            case.append(daily)


        matplotlib.pyplot.plot(date, daily_cases)
        matplotlib.pyplot.show()

datafile = RequestsDataFile()
datafile.loading_manager_methods()
datafile.search_name_country()
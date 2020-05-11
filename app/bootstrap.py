from app.Process.process_update import RequestsDataFile
from app.Process.process_quest import StatisticsSearch

class Startup:
    def __init__(self):
        self.datafile = RequestsDataFile()
        self.search = StatisticsSearch()

    def initial_menu(self):
        print("--------- Sars-Cov-2 data analysis system ------------\n" \
              " 1 - Update statistics data from the system\n" \
              " 2 - Search methods in updated data\n")
        option = int(input('Enter the desired action for the system: '))
        if option == 1:
            self.datafile.update_database_data()
        else:
            self.search.method_menu()


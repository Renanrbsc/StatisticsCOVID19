from Process.process_update import RequestsDataFile
from Process.process_quest import StatisticsSearch

class Startup:
    def __init__(self):
        self.datafile = RequestsDataFile()
        self.search = StatisticsSearch()

    def initial_menu(self):
        print(" 1 - Update statistics data from the system\n" \
              " 2 - Search methods in updated data\n")
        option = int(input('Enter the desired action for the system: '))
        if option == 1:
            self.datafile.update_database_data()
        else:
            self.search.method_menu()

if __name__ == "__main__":
    a = Startup()
    a.initial_menu()

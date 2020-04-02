# importing csv module 
import matplotlib.pyplot
# import sys
# sys.path.append(r"C:\Users\renan.ribas\Documents\Github")
# sys.path.append(r"C:\Users\Usuario\Documents\GitHub\StatisticsCOVID19")

from Process.methods import Request

class RequestsDataFile:
    def __init__(self):
        self._manager_file = ManagerFile()

    def loading_manager_methods(self):
        self._manager_file.choice_a_filename()
        self._manager_file.load_file_csv()

datafile = RequestsDataFile()
datafile.search_name_country()
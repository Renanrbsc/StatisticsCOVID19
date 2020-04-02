# importing csv module 
import matplotlib.pyplot
# import sys
# sys.path.append(r"C:\Users\renan.ribas\Documents\Github")
# sys.path.append(r"C:\Users\Usuario\Documents\GitHub\StatisticsCOVID19")
from Process.file_management import ManagerFile
from Process.methods import Methods

class RequestsDataFile:
    def __init__(self):
        self._manager_file = ManagerFile()
        self._methods = Methods()

    def loading_manager_methods(self):
        self._manager_file.choice_a_filename()

    def loadind_methods(self):
        fields, rows = self._manager_file.load_file_csv()
        self._methods.search_name_country(fields, rows)

datafile = RequestsDataFile()
datafile.loading_manager_methods()
datafile.loadind_methods()
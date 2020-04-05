from Model.file_management import ManagerFile
from Model.methods import Methods

class RequestsDataFile:
    def __init__(self):
        self._manager_file = ManagerFile()
        self._methods = Methods()

    def loading_manager_methods(self):
        self._manager_file.choice_a_filename()

    def loadind_methods(self):
        fields, rows = self._manager_file.load_file_csv()
        self._methods.search_name_country(fields, rows)

    def loading_top_five_cases(self):
        fields, rows = self._manager_file.load_file_csv()
        self._methods.top_five_biggest_cases(fields, rows)

if __name__ == "__main__":
    datafile = RequestsDataFile()
    datafile.loading_manager_methods()
    # datafile.loadind_methods()
    datafile.loading_top_five_cases()
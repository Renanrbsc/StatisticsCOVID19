from Model.file_management import ManagerFile
from Model.methods import Methods
from Services.database.methods import Database

class RequestsDataFile:
    def __init__(self):
        self._manager_file = ManagerFile()
        self._methods = Methods()
        self._db = Database()
        
    def update_database_data(self):
        self._manager_file.choice_a_filename()

        fields, rows = self._manager_file.load_file_csv()
        self._db.save_data(fields, rows)

    def loadind_methods(self):
        fields, rows = self._db.load_data()
        self._methods.search_name_country(fields, rows)

    def loading_top_five_cases(self):
        fields, rows = self._db.load_data()
        self._methods.top_five_biggest_cases(fields, rows)


if __name__ == "__main__":
    datafile = RequestsDataFile()
    # datafile.update_database_data()
    # datafile.loadind_methods()
    datafile.loading_top_five_cases()
from Model.file_management import ManagerFile
from Services.database.methods import Database

class RequestsDataFile:
    def __init__(self):
        self._manager_file = ManagerFile()
        self._db = Database()
        
    def update_database_data(self):
        self._manager_file.choice_a_filename()

        fields, rows = self._manager_file.load_file_csv()
        self._db.save_data(fields, rows)
        
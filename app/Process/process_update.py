from app.Model.file_management import ManagerFile
from app.Services.database.methods import Database

class RequestsDataFile:
    def __init__(self):
        self._manager_file = ManagerFile()
        self._db = Database()
        
    def update_database_data(self):
        self._manager_file.build_update_access()

        data_csv_for_update = self._manager_file.load_file_csv()
        self._db.save_data(data_csv_for_update)
        
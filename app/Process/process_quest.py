from app.Model.methods import Methods
from app.Services.database.methods import Database

class StatisticsSearch:
    def __init__(self):
        self._methods = Methods()
        self._db = Database()
        self.fields = list()
        self.rows = list()
    
    def choose_type_archive(self):
        print("-------- Search data in -----------\n" \
              " 1 - Confirmed\n" \
              " 2 - Death\n" \
              " 3 - Recovered\n")
        option = int(input('Enter the desired data:'))

        self.fields, self.rows = self._db.load_data(option)

    def method_menu(self):
        print("-------- Search methods -----------\n" \
              " 1 - Search by country name\n" \
              " 2 - Search for the top 5\n")
        option = int(input('Enter the desired method:'))

        if option == 1:
            self._methods.search_name_country(self.fields, self.rows)
        elif option == 2:
            self._methods.top_five_biggest_cases(self.fields, self.rows)

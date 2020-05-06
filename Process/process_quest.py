from Model.methods import Methods
from Services.database.methods import Database

class StatisticsSearch:
    def __init__(self):
        self._methods = Methods()
        self._db = Database()

    def method_menu(self):
        fields, rows = self._db.load_data()

        print(" 1 - Search by country name\n" \
              " 2 - Search for the top 5\n")
        option = int(input('Enter the desired method:'))

        if option == 1:
            self._methods.country_name_search(fields, rows)
        elif option == 2:
            self._methods.top_five_biggest_cases(fields, rows)

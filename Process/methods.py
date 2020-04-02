import matplotlib.pyplot
from Process.data_processing import DataProcess

class Methods:
    def __init__(self):
        self._dpross = DataProcess()


    def search_name_country(self, fields: list, rows: list) -> None:
        name_country = input('Search name of country: ')

        for row in rows: 
            if name_country in row:
                # parsing each column of a row 
                for index, value in enumerate(fields):
                    print(f"{value}: {row[index]} ") 
                self.simple_graphic(fields, row)
                return 


    def simple_graphic(self, fields: list, row: list):
        header_field, date_field = self._dpross.remove_header_from_list(fields)     
        header_row, date_row = self._dpross.remove_header_from_list(row)   

        dates = ['1','2','3','4']
        month_date = []
        month_cases = []
        for index, date in enumerate(date_field):
            if date[0] == dates[0]:
                month_date.append(date)
                month_cases.append(date_row[index])

        date_int = self._dpross.converts_data_to_integers(month_cases)

        matplotlib.pyplot.plot(month_date, date_int)
        matplotlib.pyplot.xlabel('Dias do mes')
        matplotlib.pyplot.ylabel('Casos contabilizados')

        matplotlib.pyplot.show()

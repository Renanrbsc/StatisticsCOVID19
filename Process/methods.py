import matplotlib.pyplot as plt
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
        months_dates, months_cases = self._dpross.create_months_list(date_row, date_field)
        months = ['Janeiro','Fevereiro','Março','Abril']
        for index, value in enumerate(months):
            months_cases_int = self._dpross.converts_data_to_integers(months_cases[index])
            plt.plot(months_dates[index], months_cases_int, label = value)
            plt.ylabel('Casos contabilizados')
            plt.xticks(rotation='vertical')
            plt.xlabel(f'Datas')
            plt.legend()
        plt.show()

        for index, value in enumerate(months):
            months_cases_int = self._dpross.converts_data_to_integers(months_cases[index])
            plt.plot(months_dates[index], months_cases_int, label = value)
            plt.ylabel('Casos contabilizados')
            plt.xticks(rotation='vertical')
            plt.xlabel(f'Datas')
            plt.legend()
            plt.show()

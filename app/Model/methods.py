import matplotlib.pyplot as plt
from app.Treatment.data_processing import DataProcess

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

    def top_five_biggest_cases(self, fields: list, rows: list) -> None:
        print(f'Top 5 biggest cases')
        list_total_cases = []
        for row in rows:
            header_row, cases = self._dpross.remove_header_from_list(row)
            last_case = cases.pop(-1)
            cases_int = self._dpross.converts_data_to_integers(last_case)
            list_total_cases.append([cases_int, row])
        list_total_cases.sort(reverse=True)

        list_top_five = []
        for index in range(5):
            list_top_five.append(list_total_cases[index])

        for index, row in enumerate(list_top_five):
            print(f"Top{index+1}: {row[1][1]} ")

        for row in list_top_five:
            print('\n')
            for index, value in enumerate(fields):
                print(f"{value}: {row[1][index]} ")
            self.simple_graphic(fields, row[1])






    def simple_graphic(self, fields: list, row: list):
        header_field, date_field = self._dpross.remove_header_from_list(fields)
        header_row, date_row = self._dpross.remove_header_from_list(row)
        months_dates, months_cases = self._dpross.create_months_list(date_row, date_field)
        months = ['Janeiro','Fevereiro','Março','Abril','Maio']
        for index, value in enumerate(months):
            months_cases_int = self._dpross.converts_data_to_integers(months_cases[index])
            plt.plot(months_dates[index], months_cases_int, label = value)
            plt.title(f'{header_row[1]} - {header_row[0]}')
            plt.ylabel('Casos contabilizados')
            plt.xticks(rotation='vertical')
            plt.xlabel(f'Datas')
            plt.legend()
        plt.show()

        for index, value in enumerate(months):
            months_cases_int = self._dpross.converts_data_to_integers(months_cases[index])
            plt.plot(months_dates[index], months_cases_int, label = value)
            plt.title(f'{header_row[1]} - {header_row[0]}')
            plt.ylabel('Casos contabilizados')
            plt.xticks(rotation='vertical')
            plt.xlabel(f'Datas')
            plt.legend()
            plt.show()

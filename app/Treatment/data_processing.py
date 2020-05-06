class DataProcess:
    def __init__(self):
        pass

    def convert_string_to_list(self, data: str) -> list:
        new_data = str(data).split(',')
        return new_data
    
    def replace_characters(self, data: bytes or str,
                                 old: str, new: str) -> str:
        new_data = str(data).replace(old, new)
        return new_data

    def remove_header_from_list(self, data: list) -> tuple:
        header = data[:5]
        date = data[5:]

        return header, date

    def converts_data_to_integers(self, data: list or str) -> list or int:
        list_data = []
        if isinstance(data, list):     
            for index in data:
                if '.' in index:
                    index = float(index)
                new_data = int(index)
                list_data.append(new_data)
            return list_data
        else:
            if '.' in data:
                data = float(data)
            data = int(data)
            return data

    def create_months_list(self, date_row: list, date_field: list) -> tuple:
        dates = ['1','2','3','4']
        months_dates = []
        months_cases = []
        for index_number, index_month in enumerate(dates):
            month_date = []
            month_case = []      
            for index, date in enumerate(date_field):
                if date[0] == index_month:
                    month_date.append(date)
                    month_case.append(date_row[index])
            months_dates.append(month_date)
            months_cases.append(month_case)
        return months_dates, months_cases

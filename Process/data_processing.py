import csv


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
        header = data[:4]
        date = data[4:]

        return header, date

    def converts_data_to_integers(self, data: list):
        list_data = []
        for index in data:
            new_data = int(index)
            list_data.append(new_data)
        return list_data
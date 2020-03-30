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
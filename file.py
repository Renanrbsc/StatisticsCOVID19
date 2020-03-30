import csv


class ManagerFile:
    def __init__(self):
        self.fields = [] 
        self.rows = [] 

    def choice_a_filename(self) -> None:
        date = input('Insert a date from daily reports: ')
        self.filename_daily_report = r"C:\Users\renan.ribas\Documents\Github\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\03-28-2020.csv"

    def load_file_csv(self) -> None:
        with open(self.filename_daily_report, 'r') as csvfile: 
            csvreader = csv.reader(csvfile) 

            self.fields = next(csvreader) 
            next(csvreader) 

            for row in csvreader:
                self.rows.append(row)  

            # get total number of rows 
            print(f"Total number of rows: {csvreader.line_num}") 
  

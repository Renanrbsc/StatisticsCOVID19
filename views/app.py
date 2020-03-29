# importing csv module 
import csv 
  
# csv file name 
filename = r"C:\Users\renan.ribas\Documents\Github\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\03-28-2020.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 

    # extracting field names through first row 
    fields = next(csvreader) 
    next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print(f"Total number of rows: {csvreader.line_num}") 
  
# printing the field names 
print('Field names are: ' + ', '.join(field for field in fields)) 
  
#  printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
    # parsing each column of a row 
    for index, column in enumerate(row): 
        print(f"{fields[index]}: {column}"), 
    print('\n') 

def search_name_country():
    name_country = input('Search country: ')
    print(f'\nSearch name of country: {name_country}\n') 
    for row in rows: 
        if name_country == row[3]:
        # parsing each column of a row 
            return row

row = search_name_country()
for index, column in enumerate(row): 
    print(f"{fields[index]}: {column}"), 
print('\n') 


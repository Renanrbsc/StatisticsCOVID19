import csv

with open(r'COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\03-26-2020.csv') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        print(linha)
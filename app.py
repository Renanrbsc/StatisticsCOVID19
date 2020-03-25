import csv

with open(r'data\\time_series_covid19_confirmed_global.csv') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        print(linha)
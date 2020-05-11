class Database:
    def __init__(self):
        self.name_archive = 'confirmed'
        self.fields = []
        self.rows = []

    def save_data(self, data_csv_for_update):
        for filename in data_csv_for_update:
            fields = filename[0]
            rows = filename[1] 
            name_archive = filename[2]

            with open(f"app\Services\{name_archive}.txt",'w') as arc:
                arc.write(','.join(fields)+'\n')
                for row in rows:
                    arc.write(','.join(row)+'\n')
            print(f"{name_archive.capitalize()} data updated successfully!")


    def load_data(self):
        with open(f'app\Services\{self.name_archive}.txt', 'r') as arc:
            for row in arc:
                row = row.strip()
                new_row = row.split(',')
                self.rows.append(new_row)
            self.fields = self.rows.pop(0)
        print("Data loaded successfully!")
        return self.fields, self.rows
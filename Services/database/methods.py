class Database:
    def __init__(self):
        self.name_archive = 'confirmed'
        self.fields = []
        self.rows = []

    def save_data(self, fields, rows):
        with open(f'Services\{self.name_archive}.txt','w') as arc:
            arc.write(','.join(fields)+'\n')
            for row in rows:
                arc.write(','.join(row)+'\n')

    def load_data(self):
        with open(f'Services\{self.name_archive}.txt', 'r') as arc:
            for row in arc:
                row = row.strip()
                new_row = row.split(',')
                self.rows.append(new_row)
            self.fields = self.rows.pop(0)

        return self.fields, self.rows
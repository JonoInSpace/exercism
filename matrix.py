class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string
        self.rows = matrix_string.split('\n')
        
    def row(self, index):
        int_row = []
        for element in self.rows[index-1].split(' '):
            int_row.append(int(element))
        return int_row

    def column(self, index):
        col = []
        for i in range(len(self.rows)):
            col.append(self.row(i+1)[index-1])
        return col
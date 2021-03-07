PLANTS = {'G':'Grass', 'C':'Clover', 'V':'Violets', 'R':'Radishes'}
STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
            'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
class Garden:
    def __init__(self, diagram, students = STUDENTS):
        self.students = sorted(students)
        self.diagram = diagram.split('\n')

    def plants(self, student):
        n = self.students.index(student)
        plants = [PLANTS[self.diagram[0][n*2]], PLANTS[self.diagram[0][n*2 + 1]],
                  PLANTS[self.diagram[1][n*2]], PLANTS[self.diagram[1][n*2 + 1]]]               
        return plants
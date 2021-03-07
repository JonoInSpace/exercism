class School:
    def __init__(self):
        self.grades = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}

    def add_student(self, name, grade):
        self.grades[grade].append(name) 

    def roster(self):
        roster = []
        for grade in self.grades:
            students = sorted(self.grades[grade])
            for student in students:
                roster.append(student)
        return roster

    def grade(self, grade_number):
        return sorted(self.grades[grade_number])
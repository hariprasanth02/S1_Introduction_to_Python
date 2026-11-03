class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self,g):
        self.grades.append(g)

    def compute_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

tom = Student("Tom")

for g in [15,17,13]:
    tom.add_grade(g)

jerry = Student("Jerry")
print(tom.name,tom.compute_average())
print(jerry.name,jerry.compute_average())


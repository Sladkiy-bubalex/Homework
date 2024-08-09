from statistics import mean


class Student:

    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self) -> str:
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.aver_rate_stud(self.grades):.1f}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def aver_rate_stud(self, grades: dict) -> float:
        all_grades = []
        for value in grades.values():
            for grade in value:
                all_grades.append(grade)
        return mean(all_grades)

    def add_fin_courses(self, course_name: str):
        self.finished_courses.append(course_name)

    def add_prog_course(self, course_name: str):
        self.courses_in_progress.append(course_name)

    def grading(self, lecturer, course: str, grade: int):
        possible_assessment = [1,2,3,4,5,6,7,8,9,10]
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and
        course in self.courses_in_progress and grade in possible_assessment):
            if course in lecturer.lecture_gr:
                lecturer.lecture_gr[course] += [grade]
            else:
                lecturer.lecture_gr[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_attached_course(self, course_name: str):
        self.courses_attached.append(course_name)

class Lecturer(Mentor):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.lecture_gr = {}

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.aver_rate_lect(self.lecture_gr):.1f}')

    def aver_rate_lect(self, grades: dict) -> float:
        all_grades = []
        for value in grades.values():
            for grade in value:
                all_grades.append(grade)
        return mean(all_grades)


class Reviewer(Mentor):

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}')

    def rate_hw(self, student, course: str, grade: int):
        if (isinstance(student, Student) and course in self.courses_attached and
         course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def stud_of_ratings(stud1_rating, stud2_rating) -> str:
    st_grade1 = stud1_rating.aver_rate_stud(stud1_rating.grades)
    st_grade2 = stud2_rating.aver_rate_stud(stud2_rating.grades)
    if st_grade1 > st_grade2:
        return (f'Средняя оценка у {stud1_rating.name} {stud1_rating.surname} больше,'
                f'чем у {stud2_rating.name} {stud2_rating.surname}')
    elif st_grade2 > st_grade1:
        return (f'Средняя оценка у {stud2_rating.name} {stud2_rating.surname} больше,'
                f'чем у {stud1_rating.name} {stud1_rating.surname}')
    else:
        return 'Средние оценки у студентов равны'


def lect_of_ratings(lect1_rating, lect2_rating):
    lt_grade1 = lect1_rating.aver_rate_lect(lect1_rating.lecture_gr)
    lt_grade2 = lect2_rating.aver_rate_lect(lect2_rating.lecture_gr)
    if lt_grade1 > lt_grade2:
        return (f'Средняя оценка у {lect1_rating.name} {lect1_rating.surname} больше,'
                f'чем у {lect2_rating.name} {lect2_rating.surname}')
    elif lt_grade2 > lt_grade1:
        return (f'Средняя оценка у {lect2_rating.name} {lect2_rating.surname} больше,'
                f'чем у {lect1_rating.name} {lect1_rating.surname}')
    else:
        return 'Средние оценки у лекторов равны'



lector1 = Lecturer('Gennadiy', 'Malyavin')
lector2 = Lecturer('Vitaliy', 'Zherlitsyn')
student1 = Student('Artur', 'Emrahov', 'men')
student2 = Student('Alexey', 'Belashov', 'men')
reviewer1 = Reviewer('Maxim', 'Rochev')
reviewer2 = Reviewer('Dmitriy', 'Semenov')

student1.add_prog_course('Python')
student2.add_prog_course('Python')

lector1.add_attached_course('Python')
lector1.add_attached_course('C++')
lector2.add_attached_course('Python')
lector2.add_attached_course('C#')

reviewer1.add_attached_course('Python')
reviewer1.add_attached_course('Java')
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
print(reviewer1, end='\n\n')

reviewer2.add_attached_course('C++')
reviewer2.add_attached_course('Python')
reviewer2.add_attached_course('Java')
reviewer2.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 3)
print(reviewer2, end='\n\n')

student1.add_fin_courses('C#')
student1.aver_rate_stud(student1.grades)
student1.grading(lector1, 'Python', 3)
student1.grading(lector1, 'Python', 10)
print(student1, end='\n\n')

student2.add_fin_courses('C++')
student2.aver_rate_stud(student2.grades)
student2.grading(lector2, 'Python', 8)
student2.grading(lector2, 'Python', 9)
print(student2, end='\n\n')

lector1.aver_rate_lect(lector1.lecture_gr)
print(lector1, end='\n\n')

lector2.aver_rate_lect(lector2.lecture_gr)
print(lector2, end='\n\n')

print(stud_of_ratings(student1,student2), end='\n\n')

print(lect_of_ratings(lector1,lector2), end='\n\n')


list_studets = [student1, student2]
def aver_rate_all_stud(students: list, course: str) -> str:
    all_grades = []
    for student in students:
        if course in student.courses_in_progress:
            for grade in student.grades[course]:
                all_grades.append(grade)
    return f'Средняя оценка студентов по курсу {course}: {mean(all_grades)}'

print(aver_rate_all_stud(list_studets, 'Python'))


list_lectors = [lector1, lector2]
def aver_rate_all_lect(lectors: list, course: str) -> str:
    all_grades = []
    for lector in lectors:
        if course in lector.courses_attached:
            for grade in lector.lecture_gr[course]:
                all_grades.append(grade)
    return f'Средняя оценка лекторов по курсу {course}: {mean(all_grades)}'

print(aver_rate_all_lect(list_lectors,'Python'))
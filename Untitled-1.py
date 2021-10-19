class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
          if course in lecturer.grades:
                lecturer.grades[course] += [grade]
          else:
                lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'     

    def __str__(self):
      res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{get_avg(self.grades)}\nКурсы в процессе изучения:{','.join(self.courses_in_progress)}\nЗавершенные курсы:{', '.join(self.finished_courses)}"
      return res 

    def __lt__(self, other):
      if not isinstance(other, Student):
        print('Not a Student') 
        return
      return get_avg(self.grades) < get_avg(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
  def __str__(self):
      res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{get_avg(self.grades)}'
      return res

  def get_avg(people):
    values_sum = sum(map(sum, people.values()))
    count = 0
    for x in people:
      count += len(people[x])
    return round(values_sum / count, 1)

  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Not a Lecturer') 
      return
    return get_avg(self.grades) < get_avg(other.grades)      

class Reviewer(Mentor): 
    def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
                student.grades[course] += [grade]
          else:
                student.grades[course] = [grade]
      else:
          return 'Ошибка' 

    def __str__(self):
      res = f'Имя: {self.name}\nФамилия: {self.surname}'
      return res 

def get_avg(people):
  values_sum = sum(map(sum, people.values()))
  count = 0
  for x in people:
      count += len(people[x])
  return round(values_sum / count, 1)                    
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'GIT']
best_student.finished_courses += ['Введение в програмированние']

best_student_2 = Student('Mike', 'Tyson', 'man')
best_student_2.courses_in_progress += ['Java', 'GIT', 'Python' ] 

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'GIT']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'GIT', 10)
cool_mentor.rate_hw(best_student, 'GIT', 10)
cool_mentor.rate_hw(best_student, 'GIT', 9)
cool_mentor.rate_hw(best_student, 'GIT', 10) 

cool_mentor_1 = Reviewer('Adam', 'Sandler')
cool_mentor.courses_attached += ['Python', 'GIT']
best_student.rate_hw(cool_mentor_1, 'Python', 10)
best_student.rate_hw(cool_mentor_1, 'Python', 8)
   

cool_mentor_2 = Lecturer('Alex', 'Black')
cool_mentor_2.courses_attached += ['Python']
best_student.rate_hw(cool_mentor_2, 'Python', 9)
best_student.rate_hw(cool_mentor_2, 'Python', 9)
best_student.rate_hw(cool_mentor_2, 'Python', 8)

cool_mentor_3 = Lecturer('Bob', 'Fisher')
cool_mentor_3.courses_attached += ['Java', 'Python' ]
best_student_2.rate_hw(cool_mentor_3, 'Java', 9)
best_student_2.rate_hw(cool_mentor_3, 'Java', 9)
best_student_2.rate_hw(cool_mentor_3, 'Python', 10)
cool_mentor.rate_hw(best_student_2, 'GIT', 10)
cool_mentor.rate_hw(best_student_2, 'GIT', 9)
cool_mentor.rate_hw(best_student_2, 'GIT', 10) 
cool_mentor.rate_hw(best_student_2, 'Python', 7) 

print(best_student.grades)
print(cool_mentor_2.grades)
print(cool_mentor)
print(cool_mentor_2)
print(best_student)
print(cool_mentor_2 < cool_mentor_3)
print(best_student > best_student_2)

def avg_rate_course(data, course):
  total = []
  for el in data:
    total.append(sum(el.grades[course]) / len(el.grades[course]))
  return round(sum(total) / len(total), 1)

list_1 = [best_student, best_student_2]
print(avg_rate_course(list_1, 'GIT'))

list_2 = [cool_mentor_2, cool_mentor_3]
print(avg_rate_course(list_2, 'Python'))



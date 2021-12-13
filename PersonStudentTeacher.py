class Person():
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name
    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def toString(self):
        return f'{self.name}({self.address})'

class Student():
    def __init__(self, name, address, courses, grades, numCourses=1):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades

    def toString(self):
        return f'Name = {self.name}, Address = {self.address} Number of courses = {self.numCourses}, Courses = {self.courses} Grades = {self.grades}'

    def addCourseGrade(self, course, grade):
        self.courses.append(course)
        self.grades.append(grade)

    def printGrades(self):
        print(self.grades)

    def getAverageGrade(self):
        avg = sum(self.grades)/len(self.grades)
        return avg

class Teacher():
    def __init__(self, name, address, courses, numCourses=1):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses

    def toString(self):
        return f'Name = {self.name}, Address = {self.address} Number of courses = {self.numCourses}, Courses = {self.courses}'

    def addCourse(self, course):
        if course in self.courses:
            return False
        else:
            self.courses.append(course)
            return True

    def removeCourse(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return True
        else:
            return False

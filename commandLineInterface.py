# This programme adds courses with cgpa, display cgpa, calculate cumulative cgpa.

# => Here I use dictionary to store my CGPA and course.
# => And the whole programme works using OOP.
# => Language of this programme is PYTHON.

# => Formula:
# Cumulative CGPA = ( summation of(individual course cgpa * individual credit) ) / ( total credit )

# => sample of storing data in "grades" class instance is:
# {'Semester=01': {'CSE110': 4.0, 'MAT110': 3.7}, 'Semester=02': {'CSE111': 4.0, 'CSE260': 3.7, 'ENG101': 2.7, 'MAT120': 4.0}, 'Semester=03': {'CSE220': 3.3, 'CSE230': 4.0, 'PHY111': 3.0, 'STA201': 3.7}}


class CGPA_Calculator:
    grades = {}
    allMethods = []

    def __init__(self):
        print("Welcome to CGPA Calculator")

    def addCourseWithCGPA(self, semester, course, cgpa):
        if semester not in CGPA_Calculator.grades:
            CGPA_Calculator.grades[semester] = {course: cgpa}
        else:
            CGPA_Calculator.grades[semester][course] = cgpa

    def showCourseWithCGPA(self):
        print()
        if len(CGPA_Calculator.grades) == 0:
            print("No Courses in the list.")
        else:
            print("Course || CGPA")
            print("-" * 14)
            for i in CGPA_Calculator.grades:
                print(i, "=>")
                for j in CGPA_Calculator.grades[i]:
                    print(f"{j} || {CGPA_Calculator.grades[i][j]}")

    def calculateCGPA(self):
        print()
        if len(CGPA_Calculator.grades) == 0:
            print("No Courses in the list.")
        else:
            sum = 0
            for i in CGPA_Calculator.grades:
                for j in CGPA_Calculator.grades[i]:
                    sum += CGPA_Calculator.grades[i][j] * 3
            numOfCourse = 0
            for i in CGPA_Calculator.grades:
                numOfCourse += len(CGPA_Calculator.grades[i])
            print("The CGPA is = {:.2f}".format(sum / (numOfCourse * 3)))
            print("Total Courses =", numOfCourse)


####################################################################################
################################## Driver Code #####################################
####################################################################################

c1 = CGPA_Calculator()

c1.addCourseWithCGPA("Semester=01", "CSE110", 4.0)
c1.addCourseWithCGPA("Semester=01", "MAT110", 3.7)

c1.addCourseWithCGPA("Semester=02", "CSE111", 4.0)
c1.addCourseWithCGPA("Semester=02", "CSE260", 3.7)
c1.addCourseWithCGPA("Semester=02", "ENG101", 2.7)
c1.addCourseWithCGPA("Semester=02", "MAT120", 4.0)

c1.addCourseWithCGPA("Semester=03", "CSE220", 3.3)
c1.addCourseWithCGPA("Semester=03", "CSE230", 4.0)
c1.addCourseWithCGPA("Semester=03", "PHY111", 3.0)
c1.addCourseWithCGPA("Semester=03", "STA201", 3.7)

c1.showCourseWithCGPA()
c1.calculateCGPA()

# Output is like:
# Welcome to CGPA Calculator

# Course || CGPA
# --------------
# Semester=01 =>
# CSE110 || 4.0
# MAT110 || 3.7
# Semester=02 =>
# CSE111 || 4.0
# CSE260 || 3.7
# ENG101 || 2.7
# MAT120 || 4.0
# Semester=03 =>
# CSE220 || 3.3
# CSE230 || 4.0
# STA201 || 3.7
# PHY111 || 3.0

# The CGPA is = 3.61
# Total Courses = 10

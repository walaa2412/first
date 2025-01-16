# Write a program called StudentGrades using lists and loops to ask for student name and 3 test scores Calculate the average of the test scores and assign a letter score. Write for 3 students, then modify to ask user how many students. Create separate lists for Student, Score1, Score2, Score3.  Use "FOR" loops to populate and extract data from the lists.
 
def calcGrade(num):
    if num > 89:
        return 'A'
    elif num > 79 and num <= 89:
        return 'B'
    elif num > 69 and num <= 79:
        return 'C'
    elif num > 59 and num <=69:
        return 'D'
    else:
        return 'F'
         
amountOfStudents = int(input('Plese enter the amount of students: '))
i=0
studentNames = []
names = []
while i < amountOfStudents:
    studentNames.append([])
    student = input('Please enter the name of the student #' + str (i+1) + ": ")
    studentNames[i].append(student)
    names.append(student)
    i=i+1
     
j = 0
avg = []
grade = []
totalSum = 0
 
for name in names:
    i = 0
    totalSum = 0
    while i < amountOfStudents:
        student = float(input("enter test #"+ str(i+1) + " for " + str(name) + ": "))
        totalSum = totalSum + student
        studentNames[j].append(student)
        i = i + 1
    averageScore = totalSum / 3.0
    avg.append (averageScore)
    grade.append (calcGrade (averageScore))
    j = j + 1
     
     
i = 0
 
for name in studentNames:
    print(str(name[i]), "'s average test score is ", avg[i])
    print(str(name[i]), "'s average test score is ", grade[i])
    i = i + 1
     
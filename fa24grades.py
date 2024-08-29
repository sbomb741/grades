LetterGrades = []

totalSemCredits = 13
credits = (3,3,3,3,1)

def cse410():

    #Quizzes = 10%
    Quiz1 = 100
    Quiz2 = 100
    Quiz3 = 100
    Quiz4 = 14/16*100 
    Quiz5 = 100
    Quiz6 = 100
    Quizzes = (Quiz1+Quiz2+Quiz3+Quiz4+Quiz5+Quiz6)/(600) * 10

    #Projects = 60%
    lab1 = 90
    lab2 = 100
    lab3 = 100
    lab4 = 88
    lab5 = 100
    lab6 = 100
    lab7 = 110*2
    labExam = 1
    if labExam >=.65:
        labExam = 1

    Projects = (lab1+lab2+labExam*(lab3+lab4+lab5+lab6+lab7))/800 * 60
    
    #Exams 30% (10% each)
    Exam1 = 100
    Exam2 = 92
    FE = 98

    Exams = (Exam1+Exam2+FE)/(300) * 30

    #Total Grade
    CurrentGrade = (Quizzes + Projects + Exams )/(100)

    
    if CurrentGrade >= .93333:
        LetterGrade = "A"
    elif CurrentGrade >= .90:
        LetterGrade = "A-"
    elif CurrentGrade >= .86667:
        LetterGrade = "B+"
    elif CurrentGrade >= .83333:
        LetterGrade = "B"
    elif CurrentGrade >= .80:
        LetterGrade = "B-"
    elif CurrentGrade >= .76667:
        LetterGrade = "C+"
    elif CurrentGrade >= .73333:
        LetterGrade = "C"
    elif CurrentGrade >= .70:
        LetterGrade = "C-"
    elif CurrentGrade >= .66667:
        LetterGrade = "D+"
    elif CurrentGrade >= .65:
        LetterGrade = "D"
    else:
        LetterGrade = "F"

    LetterGrades.append(LetterGrade)
    gr = round (CurrentGrade*100,2)

    print("Current CSE 410 Grade = " + LetterGrade + "\tAverage = " +
                str(gr))


def cse450():

    #Quizzes = 10%
    Quiz1 = 100
    Quiz2 = 100
    Quiz3 = 100
    Quiz4 = 14/16*100 
    Quiz5 = 100
    Quiz6 = 100
    Quizzes = (Quiz1+Quiz2+Quiz3+Quiz4+Quiz5+Quiz6)/(600) * 10

    #Projects = 60%
    lab1 = 90
    lab2 = 100
    lab3 = 100
    lab4 = 88
    lab5 = 100
    lab6 = 100
    lab7 = 110*2
    labExam = 1
    if labExam >=.65:
        labExam = 1

    Projects = (lab1+lab2+labExam*(lab3+lab4+lab5+lab6+lab7))/800 * 60
    
    #Exams 30% (10% each)
    Exam1 = 100
    Exam2 = 92
    FE = 98

    Exams = (Exam1+Exam2+FE)/(300) * 30

    #Total Grade
    CurrentGrade = (Quizzes + Projects + Exams )/(100)

    
    if CurrentGrade >= .93333:
        LetterGrade = "A"
    elif CurrentGrade >= .90:
        LetterGrade = "A-"
    elif CurrentGrade >= .86667:
        LetterGrade = "B+"
    elif CurrentGrade >= .83333:
        LetterGrade = "B"
    elif CurrentGrade >= .80:
        LetterGrade = "B-"
    elif CurrentGrade >= .76667:
        LetterGrade = "C+"
    elif CurrentGrade >= .73333:
        LetterGrade = "C"
    elif CurrentGrade >= .70:
        LetterGrade = "C-"
    elif CurrentGrade >= .66667:
        LetterGrade = "D+"
    elif CurrentGrade >= .65:
        LetterGrade = "D"
    else:
        LetterGrade = "F"

    LetterGrades.append(LetterGrade)
    gr = round (CurrentGrade*100,2)

    print("Current CSE 450 Grade = " + LetterGrade + "\tAverage = " +
                str(gr))


def cse496():
    LetterGrades.append('A')
    print("Current CSE 496 Grade = A\tAverage = 100")


def sta301LEC():

    #Participation 5%
    Participation = 6

    #Homeworks 20% (5% each)
    HW1 = 93
    HW2 = 86
    HW4 = 52
    Homeworks = (HW1+HW2+HW4)/(300) * 15

    #Project Assignment 35% +5% for hw3
    PA1_HW3 = .20* 79
    PA2 = .20* 94
    PAs = (PA1_HW3+PA2)

    #Final 20%
    FinalPresentation     = .10* 75.8
    FinalProjectReport    = .10* 80
    Final = FinalPresentation+FinalProjectReport

    #Final Exam 20%
    FinalExam = .20* 131/2 #/200*100

    #Total Grade
    CurrentGrade = (Participation+Homeworks+PAs+Final+FinalExam)/100 #change to 100 for all grades

    if CurrentGrade >= .80:
        LetterGrade = "A"
    elif CurrentGrade >= .75:
        LetterGrade = "A-"
    elif CurrentGrade >= .70:
        LetterGrade = "B+"
    elif CurrentGrade >= .65:
        LetterGrade = "B"
    elif CurrentGrade >= .60:
        LetterGrade = "B-"
    elif CurrentGrade >= .55:
        LetterGrade = "C+"
    elif CurrentGrade >= .45:
        LetterGrade = "C"
    else:
        LetterGrade = "F/D"

    LetterGrades.append(LetterGrade)

    print("Current STA 301 Grade = " + LetterGrade + "\tAverage = " +
                str(CurrentGrade*100))
    

def sta301REC():
    pass


# def cse495():
#     LetterGrades.append('A')

#======================================================================#

#Converts Letter Grade to Decimal (out of 4.0) helper function
def letterToGPA(letter):
    if letter == 'A':
        return 12 / 3
    elif letter == 'A-':
        return 11 / 3
    elif letter == 'B+':
        return 10 / 3
    elif letter == 'B':
        return 9 / 3
    elif letter == 'B-':
        return 8 / 3
    elif letter == 'C+':
        return 7 / 3
    elif letter == 'C':
        return 6 / 3
    elif letter == 'C-':
        return 5 / 3
    elif letter == 'D+':
        return 4 / 3
    elif letter == 'D':
        return 3 / 3
    else:
        return 0


#Obtains list of GPA values
def listGradePoints(LetterGrades):
    gradePointList = list()
    count = 0

    # Calls lettertoGPA for each letter
    for _ in LetterGrades: 
        gradePointList.append(letterToGPA(LetterGrades[count]))
        count += 1

    return gradePointList


#Multiplies GPA by number of Gradepoints
def gradePoints(gradePointList):
    actualGradePoints = 0
    count = 0

    for _ in gradePointList:
        actualGradePoints += (gradePointList[count] * credits[count])
        count += 1

    return actualGradePoints


#Calculates current semester gpa
def GPA(LetterGrades):

    #Gets list of GPA Values by class
    gradePointList = listGradePoints(LetterGrades)

    #Gets number of Gradepoints earned
    actualGradePoints = gradePoints(gradePointList)

    return actualGradePoints / totalSemCredits


#Calculates and displays various GPAs
def printGPAs():

    #First six semesters
    cumulativeOverallQualityPoints = 435.71
    cumulativeOverallCredits = 114

    cumulativeUBQualityPoints = 354.67
    cumulativeUBCredits = 92

    # get current semester gpa
    currentSemGPA = GPA(LetterGrades)
    
    # calculate overall gpa with previous and current semesters
    cumulativeOverallQualityPoints += currentSemGPA*totalSemCredits
    cumulativeOverallCredits += totalSemCredits
    overallGPA = cumulativeOverallQualityPoints/cumulativeOverallCredits

    # calculate ub gpa with previous and current semesters
    cumulativeUBQualityPoints += currentSemGPA*totalSemCredits
    cumulativeUBCredits += totalSemCredits
    overallUBGPA = cumulativeUBQualityPoints/cumulativeUBCredits

    # determine latin for graduation
    latin = ""
    if overallUBGPA >=3.75:
        latin = "\t\tsumma cum laude"
    elif overallUBGPA >=3.5:
        latin = "\t\tmagna cum laude"
    elif overallUBGPA >=3.2:
        latin = "\t\tcum laude"

    print("Current GPA:\t " + str(round(GPA(LetterGrades),4)))
    print("UB GPA:\t\t " +  str(round(overallUBGPA,4))+latin)
    print("Cummulative GPA: " + str(round(overallGPA,4)))
    print(" ")


#Main function to call the classes
def callClasses():
    print(" ")
    cse410()
    cse450()
    cse496()
    sta301LEC()
    sta301REC()
    # cse495()
    print(" ")

callClasses()
printGPAs()
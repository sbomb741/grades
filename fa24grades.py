LetterGrades = []

totalSemCredits = 13
credits = (3,3,4,3)

def cse410():

    # Projects 65%
    project1 = 0
    project2 = 0
    project3 = 0
    project4 = 0
    project5 = 0
    project6 = 0
    project7 = 0
    projects = (project1+project2+project3+project4+project5+project6+project7)/1 *.65

    # Presentation 15%
    presentation = 0 *.15
    
    # Exams 10% each
    midterm = 0 *.1
    final_exam = 0 *.1

    #Total Grade
    CurrentGrade = (projects+presentation+midterm+final_exam)/100

    
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

    requirement_doc =                   .12* 0
    design_doc =                        .20* 0
    engineering_notebook =              .04* 0
    requirement_presentation =          .04* 0
    midsem_design_review_presentation = .08* 0
    final_design_review_presentation =  .10* 0
    client_assessment =                 .10* 0
    bill_of_materials =                 .08* 0
    skills_assessment =                 .08* 0
    work_environment_assessment =       .04* 0
    progress_reports =                  .04* 0
    attendance_for_required_lectures =  .04* 0
    group_peer_review =                 .04* 0

    total_percent_earned = (requirement_doc+design_doc+engineering_notebook+requirement_presentation+
                            midsem_design_review_presentation+final_design_review_presentation+client_assessment+
                            bill_of_materials+skills_assessment+work_environment_assessment+progress_reports+
                            attendance_for_required_lectures+group_peer_review)
    total_percent_attempted = (0+1)

    
    CurrentGrade = total_percent_earned/total_percent_attempted

    
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


def sta301():

    # Extra credit earned through the semester
    earned_extra_credit = 0

    # Graded homeworks 
    # 
    # There will be 105-115 points worth of graded homework throughout the semester. 
    # Your homework grade will be a number between 0 and 100, depending on how many graded homework points you got correct. 
    # If you get 90 out of 110, your grade will be 90 out of 100. 
    # If you get 104 out of 110, your grade will record as 100 out of 100. 
    homeworks = {
        "hw2yellow" : 0,
        "hw2blue"   : 0,
        "hw2green"  : 0,
        "hw2gray"   : 0
    }

    earned_homework_points = 0
    total_homework_points = 1

    for value in homeworks.values():
        earned_homework_points += value


    # Quizzes: up to 6 quizzes, 5 points each (drop 1)
    quiz1 = 0
    quiz2 = 0
    quiz3 = 0
    quiz4 = 0
    quiz5 = 0
    quiz6 = 0
    
    earned_quiz_points = quiz1+quiz2+quiz3+quiz4+quiz5+quiz6
    total_quiz_points = 0


    # Exams: 3 @ 100 points each
    exam1 = 0
    exam2 = 0
    exam3 = 0

    earned_exam_points = exam1+exam2+exam3
    total_exam_points = 0

    CurrentGrade = ((earned_homework_points+earned_quiz_points+earned_exam_points+earned_extra_credit)/
                    (total_homework_points+total_quiz_points+total_exam_points))

    if CurrentGrade >= .94:
        LetterGrade = "A"
    elif CurrentGrade >= .91:
        LetterGrade = "A-"
    elif CurrentGrade >= .88:
        LetterGrade = "B+"
    elif CurrentGrade >= .84:
        LetterGrade = "B"
    elif CurrentGrade >= .81:
        LetterGrade = "B-"
    elif CurrentGrade >= .78:
        LetterGrade = "C+"
    elif CurrentGrade >= .71:
        LetterGrade = "C"
    elif CurrentGrade >= .68:
        LetterGrade = "C-"
    elif CurrentGrade >= .60:
        LetterGrade = "D+"
    elif CurrentGrade >= .55:
        LetterGrade = "D"
    else:
        LetterGrade = "F"

    LetterGrades.append(LetterGrade)

    print("Current STA 301 Grade = " + LetterGrade + "\tAverage = " +
                str(CurrentGrade*100))

def cse496():
    LetterGrades.append('A')
    print("Current CSE 496 Grade = A\tAverage = 100")


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

    print("Current GPA:\t" + str(round(GPA(LetterGrades),4)))
    print("UB GPA:\t\t" + str(round(overallUBGPA,4))+latin)
    print("Cumulative GPA:\t" + str(round(overallGPA,4)))

    # determine latin based on previous semesters
    overallUBGPA = 354.67/92
    if overallUBGPA >=3.75:
        latin = "\tsumma cum laude"
    elif overallUBGPA >=3.5:
        latin = "\tmagna cum laude"
    elif overallUBGPA >=3.2:
        latin = "\tcum laude"
    print("\nSP24 UB GPA:\t\t" + str(round(overallUBGPA,4))+latin)
    print("SP24 Cumulative GPA:\t" + str(round(435.71/114,4)))


#Main function to call the classes
def callClasses():
    print(" ")
    cse410()
    cse450()
    sta301()
    cse496()
    # cse495()
    print(" ")

callClasses()
printGPAs()
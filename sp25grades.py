letter_grades = []

credits = (3,3,3,4,1,2)
totalSemCredits = sum(credits)
# 453,490,102,412,399,496


def cse453():
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

    
    current_grade = .95 #total_percent_earned/total_percent_attempted

    if current_grade >= .93333:
        letter_grade = "A"
    elif current_grade >= .90:
        letter_grade = "A-"
    elif current_grade >= .86667:
        letter_grade = "B+"
    elif current_grade >= .83333:
        letter_grade = "B"
    elif current_grade >= .80:
        letter_grade = "B-"
    elif current_grade >= .76667:
        letter_grade = "C+"
    elif current_grade >= .73333:
        letter_grade = "C"
    elif current_grade >= .70:
        letter_grade = "C-"
    elif current_grade >= .66667:
        letter_grade = "D+"
    elif current_grade >= .65:
        letter_grade = "D"
    else:
        letter_grade = "F"

    letter_grades.append(letter_grade)
    gr = round (current_grade*100,2)

    print("Current CSE 453 Grade = " + letter_grade + "\tAverage = " +
                str(gr))
    

def cse490():
    """cse 490 grade"""

    # Quizzes 10%, drops lowest quiz 1-3
    quiz_list = [
        ('quiz1', 44, 50), # 0
        ('quiz2', 47, 50), # 0
        ('quiz3', -1), # 0
        ]
    quiz_x = 0 *2
    quiz_weight = list_averaging(quiz_list) * 8 + quiz_x

    # Projects 30%
    project1 = 0 * 20
    project2 = 0 * 10

    # Midterm 25%
    midterm = 73/100 * 25

    # Final 35%
    final = 0/100 * 35

    # Total Grade
    current_grade = ((quiz_weight + project1 + project2 + midterm + final) 
                     / (8 + 0 + 0 + 25 + 0))
    
    if current_grade >= .90:
        letter_grade = "A"
    elif current_grade >= .88:
        letter_grade = "A-"
    elif current_grade >= .86:
        letter_grade = "B+"
    elif current_grade >= .80:
        letter_grade = "B"
    elif current_grade >= .78:
        letter_grade = "B-"
    elif current_grade >= .75:
        letter_grade = "C+"
    elif current_grade >= .70:
        letter_grade = "C"
    elif current_grade >= .65:
        letter_grade = "C-"
    elif current_grade >= .60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    letter_grades.append(letter_grade)
    gr = round (current_grade*100,2)

    print("Current CSE 490 Grade = " + letter_grade + "\tAverage = " +
                str(gr))
    

def geo102():
    """Intro to Human Geography grade"""
    bonusAttendance = 5 
    extra_credit = 1 + 0.5 # 1 for EC 1 and the rest for songs

    # lowest map gets dropped
    mapQuizzesList = [
        ('mapQuiz1', 17, 17), # SA
        ('mapQuiz2', 31, 31), # NA
        ('mapQuiz3', 52, 52), # Middle East Asia
        ('mapQuiz4', 59, 60), # Europe
        ('mapQuiz5', -1), # SE Asia and Oceania
        ('mapQuiz6', -1) # Africa
    ]

    readingQuizzesList = [
        ('readingQuiz1', 7, 7),
        ('readingQuiz2', 11, 11),
        ('readingQuiz3', 11, 13),
        ('readingQuiz4', -1),
        ('readingQuiz5', -1),
    ]

    focusTopicList = [
        ('focusTopic1', 10, 10),
        ('focusTopic2', 30, 30),
        ('focusTopic3', 29, 30),
        ('focusTopic4', 30, 30),
        ('focusTopic5', 29, 30),
        ('focusTopic6', -1),
        ('focusTopic7', -1),
        ('focusTopic8', -1),
        ('focusTopic9', -1)
    ]

    mapQuizWeight = list_averaging(mapQuizzesList) * 20
    readingQuizWeight = list_averaging(readingQuizzesList) * 20
    focusTopicWeight = list_averaging(focusTopicList) * 25
    digitalParticipationWeight = (15/15) * 10
    finalExamWeight = (0/1) * 25

    # Total Grade
    current_grade = (mapQuizWeight + readingQuizWeight + focusTopicWeight 
                    + digitalParticipationWeight + finalExamWeight) / (20 + 20 + 25 + 10) + (bonusAttendance + extra_credit)/100
    
    if current_grade >= .93:
        letter_grade = "A"
    elif current_grade >= .90:
        letter_grade = "A-"
    elif current_grade >= .87:
        letter_grade = "B+"
    elif current_grade >= .83:
        letter_grade = "B"
    elif current_grade >= .80:
        letter_grade = "B-"
    elif current_grade >= .77:
        letter_grade = "C+"
    elif current_grade >= .73:
        letter_grade = "C"
    elif current_grade >= .70:
        letter_grade = "C-"
    elif current_grade >= .67:
        letter_grade = "D+"
    elif current_grade >= .60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    letter_grades.append(letter_grade)
    gr = round (current_grade*100,2)

    print("Current GEO 102 Grade = " + letter_grade + "\tAverage = " +
                str(gr))
    

def mth412():
    """Stats 2 grade"""

    participation_weight = 5

    homework_list = [
        ('homework1', 20, 20),
        ('homework2', 20, 20),
        ('homework3', 9, 10),
        ('homework4', 10, 10),
        ('homework5', 10, 10),
        ('homework6', 16.5, 20),
        ('homework7', 15, 15),
        ('homework8', 0, 0),
        ('homework9', 0, 0),
        ('homework10', 0, 0),
        ('homework11', 0, 0),
        ('homework12', 0, 0),
    ]
    homework_weight = list_averaging(homework_list) * 30

    exam1 = 4.95/5 * 20
    exam2 = 0/5 * 20
    exam3 = 0/5 * 25

    current_grade = ((participation_weight + homework_weight + exam1 + exam2 + exam3) 
                     / (5 + 30 + 20 + 0 + 0))
    
    if current_grade >= 4.66/5:
        letter_grade = "A+"
    if current_grade >= 4.33/5:
        letter_grade = "A"
    elif current_grade >= 4/5:
        letter_grade = "A-"
    elif current_grade >= 3.66/5:
        letter_grade = "B+"
    elif current_grade >= 3.33/5:
        letter_grade = "B"
    elif current_grade >= 3/5:
        letter_grade = "B-"
    elif current_grade >= 2.66/5:
        letter_grade = "C+"
    elif current_grade >= 2.33/5:
        letter_grade = "C"
    elif current_grade >= 2/5:
        letter_grade = "C-"
    elif current_grade >= 1.66/5:
        letter_grade = "D+"
    elif current_grade >= 1.33/5:
        letter_grade = "D"
    elif current_grade >= 1/5:
        letter_grade = "D-"
    else:
        letter_grade = "F"

    letter_grades.append(letter_grade)
    gr = round (current_grade*100,2)

    print("Current MTH 412 Grade = " + letter_grade + "\tAverage = " +
                str(gr))
    

def ubc399():
    """ubc 399 grade"""
    orientation_quiz = 5
    coursework_quiz = 5
    ub_experience = 15
    foundations = 20
    thematic = 20
    globalp = 20
    reflection = 15
    current_grade = sum([orientation_quiz, coursework_quiz, ub_experience, foundations, thematic, globalp, reflection])
    
    if current_grade >= 93:
        letter_grade = "A"
    elif current_grade >= 90:
        letter_grade = "A-"
    elif current_grade >= 87:
        letter_grade = "B+"
    elif current_grade >= 83:
        letter_grade = "B"
    elif current_grade >= 80:
        letter_grade = "B-"
    elif current_grade >= 77:
        letter_grade = "C+"
    elif current_grade >= 73:
        letter_grade = "C"
    elif current_grade >= 70:
        letter_grade = "C-"
    elif current_grade >= 67:
        letter_grade = "D+"
    elif current_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    letter_grades.append(letter_grade)

    print("Current UBC 399 Grade = " + letter_grade + "\tAverage = " +
                str(current_grade))

def cse496():
    """internship class"""
    letter_grades.append("A")
    print("Current CSE 496 Grade = A\tAverage = 100")


#======================================================================#

def list_averaging(listOfTuples):
    sum_numerators = 0
    sum_denominators = 0
    i=0
    for item in listOfTuples:
        numerator = item[1]
        if numerator!=-1:
            sum_numerators += numerator
            sum_denominators += item[2]
            i+=1
    return sum_numerators/sum_denominators


def letterToGPA(letter):
    """Converts Letter Grade to Decimal (out of 4.0) helper function"""
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

def listGradePoints(letter_grades):
    """Obtains list of GPA values"""
    gradePointList = list()
    count = 0

    # Calls lettertoGPA for each letter
    for _ in letter_grades: 
        gradePointList.append(letterToGPA(letter_grades[count]))
        count += 1

    return gradePointList

def gradePoints(gradePointList):
    """Multiplies GPA by number of Gradepoints"""
    actualGradePoints = 0
    count = 0

    for _ in gradePointList:
        actualGradePoints += (gradePointList[count] * credits[count])
        count += 1

    return actualGradePoints

def GPA(letter_grades):
    """Calculates current semester gpa"""

    #Gets list of GPA Values by class
    gradePointList = listGradePoints(letter_grades)

    #Gets number of Gradepoints earned
    actualGradePoints = gradePoints(gradePointList)

    return actualGradePoints / totalSemCredits

def printGPAs():
    """Calculates and displays various GPAs"""

    #First seven semesters
    cumulativeOverallQualityPoints = 479.71
    cumulativeOverallCredits = 125

    cumulativeUBQualityPoints = 398.67
    cumulativeUBCredits = 103

    # get current semester gpa
    currentSemGPA = GPA(letter_grades)
    
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

    print("Current GPA:\t" + str(round(GPA(letter_grades),4)))
    print("UB GPA:\t\t" + str(round(overallUBGPA,4))+latin)
    print("Cumulative GPA:\t" + str(round(overallGPA,4)))

    # determine latin based on previous semesters
    overallUBGPA = 398.67/103
    if overallUBGPA >=3.75:
        latin = "\tsumma cum laude"
    elif overallUBGPA >=3.5:
        latin = "\tmagna cum laude"
    elif overallUBGPA >=3.2:
        latin = "\tcum laude"
        
    print("\nFA24 UB GPA:\t\t" + str(round(overallUBGPA,4))+latin)
    print("FA24 Cumulative GPA:\t" + str(round(479.71/125,4)))

def callClasses():
    """Main function to call the classes"""
    print(" ")
    cse453()
    cse490()
    geo102()
    mth412()
    ubc399()
    cse496()
    print(" ")

if __name__ == "__main__":
    callClasses()
    printGPAs()
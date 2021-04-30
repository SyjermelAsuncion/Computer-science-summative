
# ------------define dictionaries--------------
grading_sys = {"A+": 100, "A": 95, "A-": 90, "B+": 88, "B": 85, "B-": 80, "C+": 75, "C": 70, "C-": 65, "D": 50, "F":0}
student_info = {"Name": " ", "GPA": " ", "ID": " "}

#------------define functions--------------
def updateGPA(info):
    """
    Prompts user to input n number of grades to update GPA
    :param info: dictionary of student's information
    :return: None
    """
    grades = []

    n = 5  # you can change this depends on how many your subjects are
    x = 1
    print("Please enter", n, "grades: ")

    
    for i in range(0, n): #for every grade that's being inputted in goes into the grades list that contains dictionaries
        print(x, ":")
        x += 1
        grade = int(input())
        grades.append(grade)
        
    grade = calculateGPA(grades)

    for letter, numGrade in grading_sys.items():# this is what turns the average grade to its letter grade equivalent
        if numGrade <= grade:
            info["GPA"] = letter
            break
    return info

def calculateGPA(grades):
    grade = 0
    for i in range(0, 5):
        grade += grades.pop()
    grade = grade / 5
    
    return grade
    
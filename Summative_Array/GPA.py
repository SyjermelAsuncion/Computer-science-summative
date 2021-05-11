# ------------------------
# Syjer Asuncion
# Student GPA
# -----------------------

"""
This program allows a student to view their profile - includes Name, ID number and GPA.
It also allows the user to update their GPA by adding their n number of grades and will
be converted to a letter grade according to the school's grading system.
"""

# ------------define modules--------------
import random

# ------------define dictionaries--------------
grading_sys = {"A+": 100, "A": 95, "A-": 90, "B+": 88, "B": 85, "B-": 80, "C+": 75, "C": 70, "C-": 65, "D": 50, "F":0}
student_info = {"Name": " ", "GPA": " ", "ID": " "}

# ------------global variables--------------
endProgram = False


# ------------define functions--------------

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

def main():
    try:
        classroom = []
        num = 0
        while endProgram is False:
            inputted = int(input("""Select the number of the desired action:
            1. Add a student 2. Print all students 3. Modify Student 4. Exit: """))
            if inputted == 1:

                classroom.append(student_info.copy())
                num+=1
                while True:
                    print()
                    studentName = str(input("Enter Student's name: "))
                    if studentName.isalpha():
                        break
                    print("Invalid Name. Please enter a name without numbers.")
                    

                classroom[num-1]["Name"] = studentName
                classroom[num-1]["ID"] = random.randint(1000, 5000)

                print("Please enter the number of the desired mode")
                updateGPA(classroom[num-1])
                     

            elif inputted == 2:
                if num == 0:
                    print("Classroom is empty")
                print()
                for i in range(0,num):
                    for key, value in classroom[i].items():
                        print(str(key) + ":" + str(value))
                    print()
                
            elif inputted == 3: # if you want to change a grade of a student
                print()
                for i in range(0,num): # so that it can show all the students informations
                    for key, value in classroom[i].items():
                        print(str(key) + ":" + str(value))
                    print()
                
                studentModify = int(input("Please enter the ID of the student you want to change: "))
                
                for i in range(0,len(classroom)):
                    for criteria in classroom[i].keys():
                        if criteria == "ID":
                            if classroom[i][criteria] == studentModify: #same as {name_DIC}['ID']
                                classroom[i] = updateGPA(classroom[i])

            elif inputted == 4:
                print("Exiting...")
                break
            else:
                print("Invalid key")
                continue


    except:
        print("Error occurred. Exiting...")  # if the user did not input alphabets


# -----------main code--------------

main()



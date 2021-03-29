#------------------------
# Syjer Asuncion
# Student GPA
#-----------------------

"""
This program allows a student to view their profile - includes Name, ID number and GPA.
It also allows the user to update their GPA by adding their n number of grades and will
be converted to a letter grade according to the school's grading system.
"""

#------------define functions--------------

import random

def calculateGPA(grades, size):
    """
    This function takes the average grade of the student
    :param grades: a list containing the numerical grades of the student
    :param size: number of grades in the list
    :return: the average numerical grade of the student
    """
    try:
        sum = 0
        for i in range(0,size):
            sum+=grades.pop()
    except:
        print("Error occurred. Exiting...")
    return sum/size

def updateGPA(info):
    """
    Prompts user to input n number of grades to update GPA
    :param info: dictionary of student's information
    :return: None
    """
    try:
        grading_sys = {"A+":100,"A":95,"A-":90,"B+":88,"B":85,"B-":80,"C+":75,"C":70,"C-":65,"D":50}
        grades = []
        print("Enter how many grades you want to add: ")
        n = int(input())
        print("Enter your grades: ")
        for i in range(0, n):
            grade = int(input())
            grades.append(grade)

        grade = calculateGPA(grades,n)

        for letter,numGrade in grading_sys.items():
            if numGrade<= grade:
                info["GPA"] = letter
                break

        print("Would you like to view your profile? (Y/N):")
        mode = input()
        if mode.upper()=="Y":
            viewProfile(info)
        else:
            print("Thank you! Exiting..")
    except:
        print("Error occurred. Exiting...")

def viewProfile(info):
    """
    Prints the student's information.
    :param info: dictionary of student's information
    :return: None
    """
    try:
        if info.get("GPA") == " ":
            print("Please update your grades")
            info = updateGPA(info);
        else:
            for key,value in info.items():
                print(str(key) + ":" + str(value))
    except:
        print("Error occurred. Exiting...")
def main():
    try:
        student_info = {"Name":" ","GPA":" ","ID":" "}
        print("Enter Student's name: ")
        usr_input = input()
        if usr_input.isalpha() == True:
            student_info["name"]=usr_input
        else:
            raise
        
        student_info["ID"] = random.randint(1000,5000)

        print("Please enter the number of the desired mode")
        print("1. View my profile   2. Update GPA")
        mode = int(input())
        if mode == 1:
            viewProfile(student_info)
        elif mode == 2:
            updateGPA(student_info)
    except:
        print("Error occurred. Exiting...") # if the user did not input alphabets

#-----------main code--------------

main()
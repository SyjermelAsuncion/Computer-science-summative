#------------------------
# Syjer Asuncion
# Student GPA 
#-----------------------

"""
This program allows a student to view their profile - includes Name, ID number and GPA.
It also allows the user to update their GPA by adding their n number of grades and will
be converted to a letter grade according to the school's grading system.
"""

# ------------define modules--------------
import random
import Info_grades


#------------define functions--------------
def main():
    try:
        classroom = []
        num = 0
        while True:
            inputted = int(input("""Select the number of the desired action: 1. Add a student 2. Print all students 3. Modify Student 4. Exit: """))
            if inputted == 1:

                classroom.append(Info_grades.student_info.copy()) # A copy of the student_info dictionary which contains the informations about students
                num+=1
                while True:
                    print()
                    studentName = str(input("Enter Student's name: "))
                    if studentName.isalpha():# if the student name contains no letters then it will quit the loop
                        break
                    print("Invalid Name. Please enter a name without numbers.")
                    

                classroom[num-1]["Name"] = studentName
                classroom[num-1]["ID"] = random.randint(1000, 5000)

                print("Please enter the number of the desired mode")
                classroom[num-1] = Info_grades.updateGPA(classroom[num-1]) # go to the function updateGPA
                     

            elif inputted == 2:
                if num == 0:
                    print("Classroom is empty") # There's no students
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
                                classroom[i] = Info_grades.updateGPA(classroom[i])

            elif inputted == 4:
                print("Exiting...")
                break
            else:
                print("Invalid key")
                continue

    except:
        print("Error occurred. Exiting...")  # if the user did not input alphabets


#-----------main code--------------

main()

#---------------------------------
# Hold menu classes
#---------------------------------

# define modules
import calculator
import converter

class User(): # welcome greeting
        def __init__(self, name, year): 
            self.name = name
            self.year = year
            
        def UserMain(self):
            print()
            print("Welcome", self.name, ", this is your own student helper app that will make your grade", self.year, "in school easier. Enjoy!")
            

def main():
    print("""

    ꧁༒☬𝓢𝓽𝓾𝓭𝓮𝓷𝓽'𝓼 𝓗𝓮𝓵𝓹𝓮𝓻☬༒꧂
    1. Calculator
    2. Dna to mRNA converter
    3. Exit
    """)


    menu = input("Option:")

    if menu == "1": # go to calculator
        main_func = True
        calculator.main()
        
    elif menu == "2":
        main_func = True
        converter.main()

    elif menu == "3":
        exit()
        
    else:
        print("Invalid input. Please try again.")
#------main------------
 
if __name__ == '__main__':
    try:
        name = str(input("Enter name: "))
        year = int(input("Year level:"))
        student = User(name, year)
        student.UserMain()
        main()
        
    except:
        print("Invalid input! Please try again. ") # if they did not put integer for year level
        exit()
        

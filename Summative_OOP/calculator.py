#------ modules ------
import math
import menu
#------ classes ------
class Calculator():
    def add(self, a, b): # to add
        return a + b
    
    def subtract(self, a, b): # to subtract
        return a - b
    
    def multiply(self,a, b): # to multiply
        return a * b
    
    def divide(self, a, b): # to divide
        return a/b
    

class scientific_calc(Calculator):
    def exponents(self, a, b): # a^b
        return math.pow(a, b)
        
    def square_roots(self, a): # square roots
        return math.sqrt(a)
    
    def logarithms(self, a): # logs
        return math.log(a)
    
    def sin(self, a): # sin(a)
        return math.sin(a)
    
    def cos(self, a): # cos(a)
        return math.cos(a)
        
    def tan(self, a): # tan(a)
        return math.tan(a)

def main():
    main_calc = Calculator()
    scie_calc = scientific_calc()

    running = True

    while running is True:
        print("""
    ๐ โ๐๐๐๐ฆ๐๐๐ฅ๐ ๐ฃ ๐
    1. Regular calc.
    2. Scientific calc.
    3. Back to menu
    4. Exit
        """)
        calc_opt = input("Option:")
        
        calc_run = True
        
        while calc_run is True:
            
            if calc_opt == "1":
                print("""
            โโโโ*.ยท:ยท.โง    โฆ    โง.ยท:ยท.*โโโโ

                        Calculator
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Back
            6. Exit

            โโโโ*.ยท:ยท.โง    โฆ    โง.ยท:ยท.*โโโโ
        """)
            
                reg_opt = input("Option:")
                
                if reg_opt == "1": # add
                    first_opt = int(input("First number:"))
                    second_opt = int(input("Second number:"))
                    
                    add_reg = main_calc.add(first_opt, second_opt)
                    print("Answer:",add_reg)
                    print()
                
                elif reg_opt == "2": # subtract
                    first_opt = int(input("First number:"))
                    second_opt = int(input("Second number:"))
                    
                    sub_reg = main_calc.subtract(first_opt, second_opt)
                    print("Answer:",sub_reg)            
                    print()
                    
                elif reg_opt == "3": # multiply
                    first_opt = int(input("First number:"))
                    second_opt = int(input("Second number:"))
                    
                    mul_reg = main_calc.multiply(first_opt, second_opt)
                    print("Answer:",mul_reg)
                    print()
                    
                elif reg_opt == "4": # divide
                    first_opt = int(input("First number:"))
                    second_opt = int(input("Second number:"))
                    
                    div_reg = main_calc.divide(first_opt, second_opt)
                    print("Answer:",div_reg)
                    print()
                
                elif reg_opt == "5": # go back
                    calc_run = False
                    
                elif reg_opt == "6": # exit
                    calc_run = False
                    running = False
                    
                else:
                    print("Invalid input. Please try again.")
                
            elif calc_opt == "2":
                print("""
            โโโโ*.ยท:ยท.โง    โฆ    โง.ยท:ยท.*โโโโ

                   Scientific Calculator
            1. Exponents
            2. Square roots
            3. Logarithms
            4. Sin
            5. Cos
            6. Tan
            7. Back
            8. Exit

            โโโโ*.ยท:ยท.โง    โฆ    โง.ยท:ยท.*โโโโ
        """)
                scie_opt = input("Option:")
                
                if scie_opt == "1":
                    first_opt = int(input("Base number:"))
                    second_opt = int(input("Exponent:"))
                    
                    expo_reg = scie_calc.exponents(first_opt, second_opt)
                    print("Answer:", expo_reg)
                    print()
                
                elif scie_opt == "2":
                    first_opt = int(input("Number:"))
                    
                    expo_reg = scie_calc.square_roots(first_opt)
                    print("Answer:", expo_reg)
                    print()
                
                elif scie_opt == "3":
                    first_opt = int(input("Number:"))
                    
                    expo_reg = scie_calc.logarithms(first_opt)
                    print("Answer:", expo_reg)
                    print()

                elif scie_opt == "4":
                    first_opt = int(input("Number:"))
                    
                    expo_reg = scie_calc.sin(first_opt)
                    print("Answer:", expo_reg)
                    print()
                
                elif scie_opt == "5":
                    first_opt = int(input("Number:"))
                    
                    expo_reg = scie_calc.cos(first_opt)
                    print("Answer:", expo_reg)
                    print()
                
                elif scie_opt == "6":
                    first_opt = int(input("Number:"))
                    
                    expo_reg = scie_calc.tan(first_opt)
                    print("Answer:", expo_reg)
                    print()
                
                elif scie_opt == "7":
                    calc_run = False
                
                elif scie_opt == "8":
                    calc_run = False
                    running = False
                    
                else:
                    print("Invalid input. Please try again.")
                    
            elif calc_opt == "3":
                menu.main() # go to menu.py
            
            elif calc_opt == "4":
                exit()
            
            else:
                print("Invalid input. Please try again.")

#-----main-----
if __name__ == '__main__':
    main()
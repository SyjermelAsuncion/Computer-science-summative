#------ modules ------
import menu
#------ classes ------

class converter_seq():
    
    def DNA_seqConvert(x):
        sequence = {"G": "C", "C": "G", "A": "U", "T":"A"} # this is the given converter for DNA to mRNA
        
        print()
        print("mRNA sequence:")
        
        try:
            for char in x:
                print(sequence[char])
                
        except:
            print("Hmmmm...something seems wrong with your sequence. Please try again.")
            
                    
    def mRNA_seqConvert(x):
        sequence = {"A": "U", "G": "C", "U": "A", "A":"U", "C":"G"} # this is the given converter for mRNA to tRNA
        
        print()
        print("tRNA sequence:")
        
        try:
            for char in x:
                print(sequence[char])
                
        except:
            print("Hmmmm...something seems wrong with your sequence. Please try again.")
            

def split(seq): # to split the sequence 
    return [char for char in seq]  

def main():
    running = True

    while running is True:
        print("""
    ꧁•⊹٭𝙲𝚘𝚗𝚟𝚎𝚛𝚝𝚎𝚛٭⊹•꧂
    1. DNA to mRNA
    2. mRNA to tRNA
    3. Go back to main
    4. Exit
        """)
        convertOpt = input("Option:")
        
        if convertOpt == "1":
            try:
                DNA_sequence = str(input("What is the DNA sequence?")).upper() # to make it all capital letters
                DNA_sequence = split(DNA_sequence)
                converter_seq.DNA_seqConvert(DNA_sequence)
                    
            except:
                print("Error! please try again.")
            
        elif convertOpt == "2":
            try:
                RNA_sequence = str(input("What is the mRNA sequence?")).upper()
                RNA_sequence = split(RNA_sequence)
                converter_seq.mRNA_seqConvert(RNA_sequence)
                    
            except:
                print("Error! please try again.")
                
        elif convertOpt == "3":
            menu.main()
        
        elif convertOpt == "4":
            running = False
        
        else:
            print("Error! please try again.")
            
        
#-----main-----
if __name__ == '__main__':
    main()

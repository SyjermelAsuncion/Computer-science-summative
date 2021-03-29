"""
This program reads the items from the (input file) grocery checklist
and writes the items not bought to an output file.
"""
def main():
    try:
        #Open input File and reads its content
        groceryList = open('input.txt', mode='r')
        contents= groceryList.read()
        contents = contents.split("\n")               #items are appended into a list

        available= ["milk","chicken","apple","shampoo","mango","soap"]
        bought = []

        #Search through the available items
        for i in range(0,len(available)):
            for j in range(0,len(contents)):
                if contents[j] == available[i]:
                    bought.append(contents[j])

        #Creates an output file and write the items not bought
        missing = open('output.txt',mode = 'w')
        missing.write("Items not bought: "+"\n")
        for item in contents:
            if item not in bought:
                missing.write(item+"\n")

        #Closes the files used
        groceryList.close()
        missing.close()

    except:
        print("An error has occured. Exiting...")

main()
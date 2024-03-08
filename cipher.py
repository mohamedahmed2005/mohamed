import string
def problem_4(): # a biggest function
    def menu():
        print("choice_1: entering string")
        print("choice_2: exit")
        choice = input("enter your choice between 1 & 2: ")
        validate_choice = validate_Choice(choice) #make value of function "validate_Choice" equals to variable "validate_choice"
        if not validate_choice: # check if value of "validate_choice" equals to 1 or not
            print("invalid choice")
            menu() #recall function "menu" again
        if choice == "2": #check if user's input equals to "2" or not
            exit("Thank you for using this program")

    def validate_Choice(choice):
        while choice != "1" and choice != "2": #iterate when user's choice isn't equal to "1" and isn't equal to "2"
            return False
        return True

    print("Welcome to cipher game")

    def main():
        menu() # recall menu
        name = input("Enter your name: ")
        lngth = len(name) #take the value of length of string"name" equals to variable"lngth"
        i = 0
        encryption = ""
        print("Do you want to delete special characters?")
        print("Choice1: Yes\nChoice2: No")
        choice_1 = input("Enter your choice between 1 & 2: ")
        validate_choice = validate_Choice(choice_1)  #make value of function "validate_Choice" equals to variable "validate_choice"
        while not validate_choice: # iterate when value of "validate_choice" is false
            print("Please enter valid choice:")
            choice_1 = input("Enter your choice between 1 & 2: ")
            validate_choice = validate_Choice(choice_1) #make value of function "validate_Choice" equals to variable "validate_choice" and check condition again

        while i < lngth: #iterate when value of variable"i"is smaller than value of variable"lngth"
            if choice_1 == "1": #check if choice_1 is equals to "1" or not
                if ord(name[i]) == 32: # check if ascii number of character equals to ascii number of space or not
                    encryption += " "
                elif 97 <= ord(name[i]) < 122: #check if ascii number of character is between ascii number of character'a' and ascii number of 'y'
                    encryption += chr(ord(name[i]) + 1) # make concatenation between character and value of variable"encryption"
                elif 65 <= ord(name[i]) < 90: #check if ascii number of character is between ascii number of character'A' and ascii number of 'Y'
                    encryption += chr(ord(name[i]) + 1)
                elif (ord(name[i]) == 122): # check if ascii number of character equals to ascii number of z or not
                    encryption += ('a')  # make concatenation between 'a' and value of variable"encryption"
                elif (ord(name[i]) == 90): # check if ascii number of character equals to ascii number of Z or not
                    encryption += ('A') # make concatenation between 'A' and value of variable"encryption"
                else:
                    print(name[i], "is not a valid character in index ", i)
                i += 1
            elif choice_1 == "2": #check if choice_1 is equals to "2" or not
                if ord(name[i]) == 32: # check if ascii number of character equals to ascii number of space or not
                    encryption += " "
                elif 97 <= ord(name[i]) < 122:  #check if ascii number of character is between ascii number of character'a' and ascii number of 'y'
                    encryption += chr(ord(name[i]) + 1) # make concatenation between character and value of variable"encryption"
                elif 65 <= ord(name[i]) < 90: #check if ascii number of character is between ascii number of character'A' and ascii number of 'Y'
                    encryption += chr(ord(name[i]) + 1) # make concatenation between 'a' and value of variable"encryption"
                elif (ord(name[i]) == 122): # check if ascii number of character equals to ascii number of z or not
                    encryption += ('a')  # make concatenation between 'a' and value of variable"encryption"
                elif (ord(name[i]) == 90): # check if ascii number of character equals to ascii number of Z or not
                    encryption += ('A') # make concatenation between 'A' and value of variable"encryption"
                else:
                    encryption += name[i]
                i += 1

        print("Encrypted name is: ", encryption)
        print("Thank you for using this program")
        main()

    main()
problem_4()

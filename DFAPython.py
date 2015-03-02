#
#   Python DFA
#
def main(): 
    
    running = True;
    while(running): 
        #open file
        uInput = input("Please enter filename:" )
        try:
            file = open(uInput)
            running = False
        except:
            print("Invalid file")
    
    running = True;
    while(running):
        uInput = input("Please enter string: ")
        if (uInput.lower == "quit"):
            running = False


if __name__ == '__main__':
    main()
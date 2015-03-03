#
#   Python DFA
#
import Node

def main(): 
    #get filename to open    
    running = True;
    while(running): 
        #uInput = input("Please enter filename:" )
        #remove
        uInput = "t.txt"
        #remove
        try:
            file = open(uInput)
            running = False
        except:
            print("Invalid file")

    #parse file and store states
    counter = 0
    transitions = []
    finalStates = []
    for line in file:
        #first line contains final states
        if (counter == 0):
            #store final states
            finalStates = line.split(' ')
        #store transitions
        else:
            line = line.split(' ')
            transitions.append(Node.Node(line[0], line[1], line[2]))
        counter += 1

    #done with file so close
    file.close

    #get string to check against
    #running = True;
    #while(running):
    #    uInput = input("Please enter string: ")
    #    if (uInput.lower == "quit"):
    #        running = False

    testCase = "aaaaaabbbbbababbbbbb";

    #we always begin at 0
    pointer = 0
    error = False
    counter = 0
    for letter in testCase:
        #check if letter is in transition at pointed index
        if (letter == transitions[pointer].mLetter):
            #if letter is last letter and it is in a final state then string is accepted
            if ((pointer in finalStates) and counter == len(testCase)):
                break
            #if letter in node then advance to next node
            pointer = transitions[pointer].mFinal
        #if letter not in language set error flag and quit
        else:
            error = True
            break
        counter += 1
    if (error):
        print("Not valid!")
    else:
        print("String accepted")

if __name__ == '__main__':
    main()
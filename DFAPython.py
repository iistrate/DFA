#
#   Python DFA
#
from Node import *
from Parser import *

def main(): 
    #get filename to open    
    running = True;
    while(running): 
        uInput = input("Please enter filename:" )
        try:
            file = open(uInput)
            running = False
        except:
            print("Invalid file")

    #parse file and get alphabet, nodes, and final states
    fileParser = Parser(file)
    fileParser.parse()

    #parse file and store states
    nodes = fileParser.getNodes()
    finalStates = fileParser.getFinalStates()
    alphabet = fileParser.getAlphabet()


    #get string to check against
    running = True;
    while(running):
        uInput = input("Please enter string or quit: ")
        if (uInput == "quit"):
            running = False
        else:
            #we always begin at 0
            testCase = uInput
            testCase = testCase + testCase[-1]
            currentNode = 0
            error = False
            counter = 0
            for letter in testCase:
                #check if letter is in alphabet
                if letter in alphabet:
                    #test 
                    #print("letter is {0} and node at {1}".format(letter,currentNode));
                    #end test
                    #check if letter belongs to current node
                    for node in nodes:
                        if node.mValue == currentNode and node.mLetter == letter:
                            #if letter is last letter
                            if (counter == len(testCase) - 1):
                                #and it is in a final state then string is accepted
                                if (currentNode in finalStates):
                                    break
                                else:
                                    print("Error last letter not in final state")
                                    error = True
                                    break
                            #advance cursor
                            currentNode = node.mGoto
                            break
                #if letter not in language set error flag and quit
                else:
                    print("Error letter not in alphabet")
                    error = True
                    break
                counter += 1
            if (error):
                print("Not valid!")
            else:
                print("String accepted")   

if __name__ == '__main__':
    main()
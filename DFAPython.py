#
#   Python DFA
#
import Node

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

    #parse file and store states
    counter = 0
    nodes = []
    finalStates = []
    alphabet = []
    for line in file:
        #first line contains final states
        if (counter == 0):
            #store final states
            finalStates = line.split(' ')
            #string to ints
            finalStates = map(int, finalStates)
        #store transitions
        else:
            line = line.split(' ')
            nodes.append(Node.Node(line[0], line[1], line[2]))
            if (line[1] not in alphabet):
                alphabet.append(line[1])
        counter += 1
    #done with file so close
    file.close

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
            print(testCase)
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
                                    error = True
                                    break
                            #advance cursor
                            currentNode = node.mGoto
                            break
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
from Node import *

class Parser(object):
    """description of class"""
    def __init__(self, file):
        self.__m_file = file
        self.__m_Nodes = []
        self.__m_finalStates = []
        self.__m_alphabet = []

    def parse(self):
        counter = 0
        for line in self.__m_file:
            #first line contains final states
            if (counter == 0):
                #store final states
                self.__m_finalStates = line.split(' ')
                #string to ints
                self.__m_finalStates = [int(i) for i in self.__m_finalStates]
            #store transitions
            else:
                line = line.split(' ')
                self.__m_Nodes.append(Node(line[0], line[1], line[2]))
                if (line[1] not in self.__m_alphabet):
                    self.__m_alphabet.append(line[1])
            counter += 1

    def close(self):
        #done with file so close
        self.__m_file.close()

    def getAlphabet(self):
        return self.__m_alphabet

    def getFinalStates(self):
        return self.__m_finalStates

    def getNodes(self):
        return self.__m_Nodes
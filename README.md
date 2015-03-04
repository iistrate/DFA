# DFA
Python DFA simulator

A deterministic finite automaton(DFA) —also known as deterministic finite state machine—
is a finite state machine that accepts/rejects finite strings of symbols and only produces 
a unique computation (or run) of the automaton for each input string.

Math 362 Programming Assignment

Write a DFA simulator. 

Read your DFA from a textfile. 
First line contains a list of the final states (as integers), separated by a space. 
Rest of file contains the transitions in form: startstate, blank, symbol read, blank, tostate 

Prompt user for name of file. 

From there, program prompts the user for strings to test for acceptance on DFA. 

Show the trace of the transitions through the machine along with whether the string is accepted or not.

Continue reading strings until user enters "quit" 


Example input file... (ab)* 

0 
0 a 
1 b 
2 1 
a 2 
1 b 0 
2 a 2 
2 b 2 


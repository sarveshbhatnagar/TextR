import file
import process
import constants


#opening the file input.txt
x = file.File("input.txt")

#reading the file
content = x.read()

#creating process object for lex
notes = process.Process(content);

#state to keep track of the function being carried on.
state = 0
while notes.end():
    x = notes.lex()
    if x in constants.function:
        # print(constants.function[x])
        #change state to the function value
        state = constants.function[x]

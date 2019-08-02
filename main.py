import file
import process
import constants

x = file.File("input.txt")

content = x.read()

notes = process.Process(content);

state = 0
while notes.end():
    x = notes.lex()
    if x in constants.function:
        # print(constants.function[x])

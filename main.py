import file
import process
import constants


#opening the file input.txt
x = file.File("input.tr")

#reading the file
content = x.read()

#creating process object for lex
notes = process.Process(content);

sum = []
sub = []
mult = []
div = []

#state to keep track of the function being carried on.
state = 0
stateChange = False;
while notes.end():
    x = notes.lex()
    if x in constants.function:
        # print(constants.function[x])
        #change state to the function value
        #since state is changing here, we need to perform previous state function.
        notes.proc();
        notes.state = constants.function[x]
        notes.stateChange = True;

    if notes.state == 1 and notes.stateChange == False:
        # print("do sum");
        # print(x);
        notes.sum.append(int(x));

    elif notes.state == 2 and notes.stateChange == False:
        notes.sub.append(int(x));
    elif notes.state == 3 and notes.stateChange == False:
        notes.mult.append(int(x));
    elif notes.state == 4 and notes.stateChange == False:
        notes.div.append(int(x));
    else:
        print(x);
        notes.stateChange = False;


notes.proc()

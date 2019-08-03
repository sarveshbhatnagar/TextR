import file
import process
import constants


#opening the file input.txt
x = file.File("input.txt")

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
        if state == 1:
            pass #do something
        elif state == 2:
            pass #do something...
        elif state == 3:
            pass
        elif state == 4:
            pass
        state = constants.function[x]
        stateChange = True;

    if state == 1 and stateChange == False:
        # print("do sum");
        # print(x);
        sum.append(int(x));

    elif state == 2 and stateChange == False:
        sub.append(int(x));
    elif state == 3 and stateChange == False:
        mult.append(int(x));
    elif state == 4 and stateChange == False:
        div.append(int(x));
    else:
        print(x);
        stateChange = False;


print(sum);
print(sub);
print(mult);
print(div);

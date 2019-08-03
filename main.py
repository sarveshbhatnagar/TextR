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
            tem = 0;
            for num in sum:
                tem += num;
            print(tem);
            sum = []
        elif state == 2:
            tem = 0;
            for num in sub:
                tem -= num;
            print(tem);
            sub = []
        elif state == 3:
            tem = 1;
            for num in mult:
                tem *= num;
            print(tem);
            mult = []
        elif state == 4:
            tem = 0;
            for num in div:
                tem /= num;
            print(tem);
            div = []
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


if state == 1:
    tem = 0;
    for num in sum:
        tem += num;
    print(tem);
    sum = []
elif state == 2:
    tem = 0;
    for num in sub:
        tem -= num;
    print(tem);
    sub = []
elif state == 3:
    tem = 1;
    for num in mult:
        tem *= num;
    print(tem);
    mult = []
elif state == 4:
    tem = 0;
    for num in div:
        tem /= num;
    print(tem);
    div = []

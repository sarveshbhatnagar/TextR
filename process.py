import file

class Process(object):
    """Class process , initialize it with the content which you want to process.
    lex() returns tokens one after other,
    end() returns False if its the end of the content.
    """

    def __init__(self, content):
        self.content = content.split()
        self.index = 0
        self.state = 0
        self.stateChange = False
        self.sum = []
        self.sub = []
        self.mult = []
        self.div = []

    def lex(self):
        self.index += 1;
        return self.content[self.index-1];

    def end(self):
        if self.index == len(self.content):
            return False;
        else:
            return True;

    def proc(self):
        if self.state == 1:
            tem = 0;
            for num in self.sum:
                tem += num;
            x = file.File("input.tr")
            # print(tem);
            x.wrt(str(tem));
            self.sum = []
        elif self.state == 2:
            tem = 0;
            for num in self.sub:
                tem -= num;
            x = file.File("input.tr")
            # print(tem);
            x.wrt(str(tem));
            self.sub = []
        elif self.state == 3:
            tem = 1;
            for num in self.mult:
                tem *= num;
            x = file.File("input.tr")
            # print(tem);
            x.wrt(str(tem));
            self.mult = []
        elif self.state == 4:
            tem = 0;
            for num in self.div:
                tem /= num;
            x = file.File("input.tr")
            # print(tem);
            x.wrt(str(tem));
            self.div = []

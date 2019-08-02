
class Process(object):
    """Class process , initialize it with the content which you want to process.
    lex() returns tokens one after other,
    end() returns False if its the end of the content.
    """

    def __init__(self, content):
        self.content = content.split()
        self.index = 0

    def lex(self):
        self.index += 1;
        return self.content[self.index-1];

    def end(self):
        if self.index == len(self.content):
            return False;
        else:
            return True;


class Process(object):
    """docstring for Process."""

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

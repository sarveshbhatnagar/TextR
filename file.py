


class File(object):
    """docstring for File."""

    def __init__(self, filename):
        super(File, self).__init__()
        self.filename = filename

    def read(self):
        content = ""
        with open(self.filename,'r') as file:
            content = file.read()
        return content

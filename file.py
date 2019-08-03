


class File(object):
    """documentation for File.
    initialize with filename,
    read() returns the content of the file.
    """

    def __init__(self, filename):
        super(File, self).__init__()
        self.filename = filename

    def read(self):
        content = ""
        with open(self.filename,'r') as file:
            content = file.read()
        return content

    def wrt(self,content):
        with open("output.txt","a") as file:
            file.write(content)
            file.write("\n")

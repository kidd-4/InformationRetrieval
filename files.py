
class files:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def open_file(self,mode='r'):
        self.file = open(self.file_path,mode)
        return self.file

    def write_file(self,content):
        self.file.write(str(content))

    def close_file(self):
        self.file.close()
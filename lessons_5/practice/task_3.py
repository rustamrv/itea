
class File:
    def __init__(self, path, mode):
        self.path = path 
        self.mode = mode

    def __enter__(self):
        self.fd = open(self.path, self.mode)
        return self.fd.read()

    def __exit__(self, *args): 
        self.fd.close()



with File("lessons_5/practice/test.txt", 'r') as f:
    print(f)
 
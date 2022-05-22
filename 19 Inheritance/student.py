class Student:
    def __init__(self, fi, group_number, learn):
        self.fi = fi
        self.group_number = group_number
        self.learn = learn

    def sprint(self):
        print(self.fi, self.group_number, self.learn)

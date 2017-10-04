class Name:
    def __init__(self, first, last):
        self.first__name = first
        self.last__name = last

    def first(self):
        return self.first__name

    def last(self):
        return self.last__name

    def natural(self):
        return self.first__name + " " + self.last__name

    def formal(self):
        return self.last__name + ", " + self.first__name

    def __repr__(self):
        return self.first__name + " " + self.last__name

    def initials(self):
        return self.first__name[0] + self.last__name[0]

    def check(self, fi, li):
        return (fi == self.first__name[0]) and (li == self.last__name[0])

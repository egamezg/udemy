class File:
    def __init__(self, file):
        self.file = file

    def savefile(self, data):
        fileo = open(self.file, "wt")
        fileo.write(data)
        fileo.close()

    def addfile(self, data):
        fileo = open(self.file, "at")
        fileo.write(data)
        fileo.close()

    def readfile(self):
        fileo = open(self.file, "rt")
        datafile = fileo.read()
        return datafile


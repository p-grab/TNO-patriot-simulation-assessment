import csv


class Radar:
    """Represents a radar that sequentially processes data from an input file"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, "r")
        self.reader = csv.reader(self.file)
    
    def scan(self):
        try:
            line = next(self.reader)
            return line[0].split(";")
        except StopIteration:
            return None
        

    def close_file(self):
        self.file.close()
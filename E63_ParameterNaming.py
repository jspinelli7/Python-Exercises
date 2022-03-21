# This is a really good lecture explaining the purpose of 'self'

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year


matrix = Movie('The Matrix', 1994)
print(matrix.name)

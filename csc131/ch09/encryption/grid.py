"""
File: grid.py
"""

class Grid(object):
    """Represents a two-dimensional matrix."""

    def __init__(self, rows, columns, fillValue = None):
        """Sets up the data."""
        self.data = []
        for row in range(rows):
            dataInRow = []
            for column in range(columns):
                dataInRow.append(fillValue)
            self.data.append(dataInRow)

    def getHeight(self):
        """Returns the number of rows."""
        return len(self.data)

    def getWidth(self):
        "Returns the number of columns."""
        return len(self.data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [][]."""
        return self.data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return result

    def find(self, value):
        """Returns (row, column) if value is found,
        or None otherwise."""
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                if self[row][column] == value:
                    return (row, column)
        return None

def main():
    g = Grid(10, 10, 1)
    print(g)

if __name__ == "__main__":
    main()
    
            

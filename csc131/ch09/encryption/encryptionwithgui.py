"""
File: encryptionwithgui.py
"""

from breezypythongui import EasyFrame
from grid import Grid
from matrixcanvas import MatrixCanvas
import random

def makeMatrix():
    """Bulids and returns an encryption matrix."""
    listOfChars = []
    for ascii in range(32, 128):
        listOfChars.append(chr(ascii))
    random.shuffle(listOfChars)
    matrix = Grid(8, 12)
    i = 0
    for row in range(matrix.getHeight()):
        for column in range(matrix.getWidth()):
            matrix[row][column] = listOfChars[i]
            i += 1
    return matrix

class EncryptView(EasyFrame):
    """A window for an encryption process."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Block Cipher Encryption")
        self.setResizable(False)
        self.matrix = makeMatrix()
        self.matrixPanel = self.addPanel(row = 0, column = 0)
        self.addCanvases()
        fieldPanel = self.addPanel(row = 8, column = 0,
                                   columnspan = 12,
                                   background = "yellow")
        fieldPanel.addLabel(text = "Plaintext", row = 0, column = 0,
                            background = "yellow")
        self.plainField = fieldPanel.addTextField(text = "",
                                                  row = 0,
                                                  column = 1)
        fieldPanel.addLabel(text = "Ciphertext", row = 1, column = 0,
                            background = "yellow")
        self.cipherField = fieldPanel.addTextField("", row = 1,
                                                   column = 1,
                                                   state = "readonly")
        buttonPanel = self.addPanel(row = 9, column = 0,
                                    columnspan = 12,
                                    background = "black")
        self.encryptButton = buttonPanel.addButton(text = "Encrypt",
                                                   row = 0, column = 0,
                                                   command = self.encrypt)
        self.matrixButton = buttonPanel.addButton(text = "New matrix",
                                                  row = 0,
                                                  column = 1,
                                                  command = self.newMatrix)

    def addCanvases(self):
        """Adds canvases with the characters to the matrix panel
        and saves them in a grid for later reference."""
        self.canvasGrid = Grid(self.matrix.getHeight(),
                               self.matrix.getWidth())
        for row in range(self.matrix.getHeight()):
            for column in range(self.matrix.getWidth()):
                canvas = MatrixCanvas(self, 20, 20,
                                      self.matrix[row][column])
                self.canvasGrid[row][column] = canvas
                self.matrixPanel.addCanvas(canvas = canvas,
                                           row = row,
                                           column = column)

    def newMatrix(self):
        """Creates a new matrix and resets the matrix
        canvasses with data."""
        self.matrix = makeMatrix()
        for row in range(self.matrix.getHeight()):
            for column in range(self.matrix.getWidth()):
                self.canvasGrid[row][column].draw(self.matrix[row][column])

    def selectCanvas(self, row, column, color):
        """Paints the background of the canvas at the
        given row and column."""
        self.canvasGrid[row][column]["background"] = color

    def deselectCanvasses(self):
        """Resets the background of the canvasses in the grid."""
        for row in range(self.canvasGrid.getHeight()):
            for column in range(self.canvasGrid.getWidth()):
                self.canvasGrid[row][column]["background"] = "white"

    def encrypt(self):
        """Uses matrix to encrypt plainText. Does one pair
        of characters at a time."""
        self.cipherText = self.cipherField.getText()
        # Set up the initial state of the encryption.
        if self.cipherText == "":
            self.matrixButton["state"] = "disabled"
            self.plainText = self.plainField.getText()
            self.limit = len(self.plainText)
            if self.limit % 2 == 1:
                self.limit -= 1
            self.cursor = 0
        # Use the matrix to encrypt one pair of characters.
        if self.cursor < self.limit:
            self.cipherText += self.encryptPair()
            self.cipherField.setText(self.cipherText)
            self.cursor += 2
        # Add the last character if plaintext length was odd.
        elif self.limit < len(self.plainText):
            self.cipherText += self.plainText[self.limit]
            self.cipherField.setText(self.cipherText)
        # Clean up when done.
        if len(self.plainText) == len(self.cipherText):
            self.encryptButton["text"] = "Clear fields"
            self.encryptButton["command"] = self.clearFields

    def encryptPair(self):
        """Returns the cipherText of the pair of
        characters at cursor and cursor + 1 in plainText."""
        # Locate the characters in the matrix
        self.deselectCanvasses()
        (row1, col1) = self.matrix.find(self.plainText[self.cursor])
        (row2, col2) = self.matrix.find(self.plainText[self.cursor + 1])
        self.selectCanvas(row1, col1, "gray")
        self.selectCanvas(row2, col2, "gray")
        # Swap them if they are in the same row or column
        if row1 == row2 or col1 == col2:
            return self.plainText[self.cursor + 1] + self.plainText[self.cursor]
        # Otherwise, use the characters at the opposite
        # corners of the rectangle in the matrix
        else:
            self.selectCanvas(row2, col1, "pink")
            self.selectCanvas(row1, col2, "pink")
            ch1 = self.matrix[row2][col1]
            ch2 = self.matrix[row1][col2]
            return ch1 + ch2

    def clearFields(self):
        """Resets fields and buttons."""
        self.deselectCanvasses()
        self.plainField.setText("")
        self.cipherField.setText("")
        self.encryptButton["text"] = "Encrypt"
        self.encryptButton["command"] = self.encrypt
        self.matrixButton["state"] = "normal"

def main():
    """Instantiate and pop up the window."""
    EncryptView().mainloop()
    
if __name__ == "__main__":
    main()
    
            

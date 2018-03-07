"""
File: encryption.py
"""

from grid import Grid
import random

def makeMatrix():
    """Builds and returns an encryption matrix."""
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

def encrypt(plainText, matrix):
    """Uses matrix to encrypt plainText,
    and returns cipherText."""
    cypherText = ""
    limit = len(plainText)
    # Adjust for an odd number of characters
    if limit % 2 == 1:
        limit -= 1
    # Use the matrix to encrypt pairs of characters
    i = 0
    while i < limit:
        cypherText += encryptPair(plainText, i, matrix)
        i += 2
    # Add the last character if length was odd
    if limit < len(plainText):
        cypherText += plainText[limit]
    return cypherText

def decrypt(cipherText, matrix):
    """Uses matrix to decrypt cipherText,
    and returns plainText."""
    return encrypt(cipherText, matrix)

def encryptPair(plainText, i, matrix):
    """Returns the cipherText of the pair of
    characters at i and i + 1 in plainText."""
    # Locate the characters in the matrix
    (row1, col1) = matrix.find(plainText[i])
    (row2, col2) = matrix.find(plainText[i + 1])
    # Swap them if they are in the same row or column
    if row1 == row2 or col1 == col2:
        return plainText[i + 1] + plainText[i]
    # Otherwise, use the characters at the opposite
    # corners of the rectangle in the matrix
    else:
        ch1 = matrix[row2][col1]
        ch2 = matrix[row1][col2]
        return ch1 + ch2

def main(plainText = None):
    if not plainText:
        plainText = input("Enter the plaintext: ")
    matrix = makeMatrix()
##    print("Matrix: ")      # For debugging
##    print(matrix)
    cipherText = encrypt(plainText, matrix)
    print("Encrypting . . .\n",
          "Plain text: " + plainText,
          "\nCipher text: " + cipherText)
    oldText = decrypt(cipherText, matrix)
    print("Decrypting . . .\n",
          "Cipher text: " + cipherText,
          "\nPlain text: " + oldText)
              

if __name__ == "__main__":
    main()
    
            

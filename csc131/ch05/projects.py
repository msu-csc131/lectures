"""
CSC131 - Computational Thinking
Missouri State University, Spring 2018

This module contains solutions to the problems found at the end of Chapter 5.

File: projects.py
"""

from string import punctuation

# Table of integers in bases 2-16 with digits to use with Problem 5.6
repTable = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
            5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'A', 11: 'B', 12: 'C', 13: 'D',
            14: 'E', 15: 'F'}


def decimal_to_rep(decimal: int, base: int) -> str:
    """
    Project 5.6: Converts the integer value in decimal to a rep in the given base returns the rep as a string.
    NOTE: This solution only considers up to base 16 (hexadecimal) conversions.
    :param decimal: The integer (i.e., decimal) to convert
    :param base: The base for the converted number
    :return: A string representation of the given decimal as represented by the given base is returned.
    """
    """"""
    if decimal == 0:
        return '0'
    else:
        rep = ""
        while decimal > 0:
            remainder = decimal % base
            decimal = decimal // base
            rep = repTable[remainder] + rep
        return rep


def problem5_6() -> None:
    """Demonstrates the solution to Project 5.6"""
    print("{} in decimal is:     {}".format(10, decimal_to_rep(10, 10)))
    print("{} in octal is:       {}".format(10, decimal_to_rep(10, 8)))
    print("{} in binary is:      {}".format(10, decimal_to_rep(10, 2)))
    print("{} in hexadecimal is: {}".format(10, decimal_to_rep(10, 16)))


def problem5_7(in_name: str = 'input.txt') -> None:
    """Demonstrates the solution to Project 5.7"""
    # Take the input file name
    if in_name is None:
        in_name = input("Enter the input file name: ")

    # Open the input file and initialize list of unique words
    input_file = open(in_name, 'r')
    unique_words = []

    # Add the unique words in the file to the list
    for line in input_file:
        words = line.split()
        for word in words:
            word = word.lower().strip(punctuation)
            if word not in unique_words:
                unique_words.append(word)
    unique_words.sort()

    # Prints the unique words
    for word in unique_words:
        print(word)
    print("\nIt looks like there were {} unique words in {}.".format(len(unique_words), in_name))


def main() -> None:
    problem5_6()
    problem5_7()


# The entry point for program execution
if __name__ == "__main__":
    main()

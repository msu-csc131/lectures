"""
CSC131 - Computational Thinking
Missouri State University, Spring 2018

This module contains solutions to the problems found at the end of Chapter 5.

File: projects.py
"""
from functools import reduce


def is_sorted(my_list: list) -> bool:
    """
    Project 6.5 - Defining a predicate.
    :param my_list:
    :return: Returns True if my_list is sorted in ascending order or False otherwise.
    """
    if len(my_list) == 0 or len(my_list) == 1:
        return True
    else:
        for index in range(len(my_list) - 1):
            if my_list[index] > my_list[index + 1]:
                return False
    return True


def project6_5() -> None:
    my_list = []
    print(is_sorted(my_list))
    my_list = [1]
    print(is_sorted(my_list))
    my_list = list(range(10))
    print(is_sorted(my_list))
    my_list[9] = 3
    print(is_sorted(my_list))


def project6_9(file_name: str = "numbers.dat") -> None:
    """
    Project 6.9
    :param file_name: The file containing numbers
    :return: None
    """
    # Accept the input file name and open the file
    if file_name is None:
        file_name = input("Enter the input file name: ")
    input_file = open(file_name, 'r')

    # Read the numbers as strings into a list
    a_list = []
    for line in input_file:
        a_list.extend(line.split())

    # Convert all the strings in the list to numbers
    a_list = list(map(float, a_list))

    # Compute the sum of the numbers
    summation = reduce(lambda x, y: x + y, a_list)

    # Print the average
    if len(a_list) == 0:
        average = 0
    else:
        average = summation / len(a_list)
    print("The average is", average)


def main():
    project6_5()
    project6_9()


if __name__ == "__main__":
    main()
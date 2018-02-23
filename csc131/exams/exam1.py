"""
CSC131 - Computational Thinking
Missouri State University, Spring 2018

File: Exam1.py
"""
from functools import reduce
from string import punctuation
from turtle import Screen
from turtle import Turtle
import os


def get_data_file_name(file_name: str = "q1.dat") -> str:
    """
    Get a data file stored in the current directory with the given file name.
    :param file_name: the name of the data file
    :return The full path to the given data file is returned.
    """
    full_path = os.path.realpath(__file__)
    return os.path.dirname(full_path) + "/" + file_name


def big_unique_words(input_file_name: str) -> int:
    """
    Compute the number of unique words greater than length 5 found in the given file.
    :param input_file_name: the file to interrogate
    :return The number of unique words greater than length 5 found in the give file is returned.
    """
    unique_words = []
    with open(input_file_name, 'r') as input_file:
        contents = input_file.read()
    for word in contents.split():
        # translate any punctuation which might give a deceptively long length
        translation_table = {ord(x): None for x in punctuation}
        # consider only the lowercase versions of the word so we don't treat different 
        # cases as unique words
        word = word.translate(translation_table).lower()
        if len(word) > 5:
            if word not in unique_words:
                unique_words.append(word)
    return len(unique_words)


def question_1() -> None:
    """
    Demonstrate use of question 1 solution.
    :return None
    """
    print("big_unique_words(\"q1.dat\") = {}".format(big_unique_words(get_data_file_name("q1.dat"))))


def sum_data_in_file(input_file_name: str) -> int:
    """
    A solution to question 2 that seeks to find the sum of the contents of the given file.
    :param input_file_name: the data file
    :return The sum of the data in the given data file is returned.
    """
    with open(input_file_name, 'r') as input_file:
        contents = input_file.read()
    return reduce(lambda x, y: x + y, list(map(int, contents.split())))


def question_2() -> None:
    """
    Demonstrate use of question 2 solution.
    :return None
    """
    print("sum_data_in_file(\"q2.dat\") = {}".format(sum_data_in_file(get_data_file_name("q2.dat"))))


def get_filtered_list(data: list) -> list:
    """
    The answer to question #3 is the expression following the return statement.
    :param data the list to be filtered
    :return A list of the values in the given list that are greater than 3 is returned.
    """
    return list(filter(lambda x: x > 3, data))

def question_3() -> None:
    """
    Using the filter function and a lambda argument, write an expression that produces 
    a list of the values in some list named data that are larger than 3.
    """
    print("get_filtered_list(range(11)) = {}".format(get_filtered_list(range(11))))


def draw_robot_head(turtle: Turtle, length: int) -> None:
    """
    A possible solution to question 4.
    :param turtle: a Turtle instance with which to draw the robot head
    :param length: the length of the robot head's encapsulating rectangle
    :return None
    """
    # Provide access to screen so we can capture its click events
    win = Screen()
    # Some useful dimensions for drawing the robot head
    encapsulating_rect_length = length
    encapsulating_rect_height = length // 4
    ear_length = length // 8
    ear_height = encapsulating_rect_height // 2
    ear_gap = ear_height // 2
    face_length = encapsulating_rect_length - 2 * ear_length
    # begin our rendition
    turtle.penup()
    turtle.forward(ear_length)
    turtle.pendown()
    turtle.forward(face_length)
    turtle.left(90)
    turtle.forward(ear_gap)
    turtle.right(90)
    turtle.forward(ear_length)
    turtle.left(90)
    turtle.forward(ear_height)
    turtle.left(90)
    turtle.forward(ear_length)
    turtle.right(90)
    turtle.forward(ear_gap)
    turtle.left(90)
    turtle.forward(face_length)
    turtle.left(90)
    turtle.forward(ear_gap)
    turtle.right(90)
    turtle.forward(ear_length)
    turtle.left(90)
    turtle.forward(ear_height)
    turtle.left(90)
    turtle.forward(ear_length)
    turtle.right(90)
    turtle.forward(ear_gap)
    # hide the turtle to see the robot head
    turtle.hideturtle()
    # list for click event to close the turtle graphics system
    win.exitonclick()
    return None


def question_4() -> None:
    """
    Demonstrate an implementation of a possible question 4 solution.
    :return None
    """
    draw_robot_head(Turtle(), 100)


def question_5() -> None:
    pass


def main() -> None:
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()


if __name__ == '__main__':
    main()

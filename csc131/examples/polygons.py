from turtle import Turtle
from turtle import Screen
from time import sleep


def square(t: Turtle, length: int) -> None:
    """
    Draws a square with the given length.
    :param t: a Turtle instance
    :param length: side of square length
    :return: None
    """
    for count in range(4):
        t.forward(length)
        t.left(90)


def hexagon(t: Turtle, length: int) -> None:
    """
        Draws a hexagon with the given length.
        :param t: a Turtle instance
        :param length: side of hexagon length
        :return: None
        """
    for count in range(6):
        t.forward(length)
        t.left(60)


def radial_pattern(t: Turtle, n: int, length: int, shape) -> None:
    """
    Draws a radial pattern of n shapes with the given length.
    :param t: a Turtle instance
    :param n: number of shapes
    :param length: length of shape side
    :param shape: a function for drawing some shape
    :return: None
    """
    for count in range(n):
        shape(t, length)
        t.left(360 / n)


def test_module() -> None:
    a_turtle = Turtle()
    screen = Screen()
    radial_pattern(a_turtle, n=10, length=50, shape=square)
    sleep(2)  # pause for 5 seconds
    a_turtle.clear()
    radial_pattern(a_turtle, n=10, length=50, shape=hexagon)
    screen.exitonclick()


if __name__ == '__main__':
    test_module()

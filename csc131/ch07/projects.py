"""
CSC131 - Computational Thinking
Missouri State University, Spring 2018

This module contains solutions to the problems found at the end of Chapter 5.

File: projects.py
"""
import math
from turtle import Turtle


def draw_circle(t: Turtle, x: int, y: int, radius: int) -> None:
    """
    Draws a circle with the given center point and radius.
    :param t: A Turtle instance that renders the circle.
    :param x: x-coordinate of the center of the circle
    :param y: y-coordinate of the center of the circle
    :param radius: radius of the circle to draw
    :return: None
    """
    t.up()
    t.goto(x + radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)


def main():
    """Allows the user to enter the center point and the radius."""
    x = int(input("Enter the x coordinate of the center point: "))
    y = int(input("Enter the y coordinate of the center point: "))
    radius = int(input("Enter the radius: "))
    draw_circle(Turtle(), x, y, radius)


if __name__ == "__main__":
    main()

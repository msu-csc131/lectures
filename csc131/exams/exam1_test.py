"""
CSC131 - Computational Thinking
Missouri State University, Spring 2018

Unit test suite for exam1 module
see https://docs.python.org/3/library/unittest.html

File: exam1_test.py
"""
import unittest
from exam1 import big_unique_words
from exam1 import sum_data_in_file
from exam1 import get_filtered_list
from exam1 import get_data_file_name


class TestExam1Module(unittest.TestCase):
    """
    Unit test suite for the exam1 module.
    """
    def test_question_1(self):
        """
        A real basic test of the question 1 solution.
        :return None
        """
        actual = big_unique_words(get_data_file_name("q1.dat"))
        expected = 2
        self.assertEqual(expected, actual)

    def test_question_2(self):
        """
        A real basic test of the question 2 solution.
        :return None
        """
        actual = sum_data_in_file(get_data_file_name("q2.dat"))
        expected = 210
        self.assertEqual(expected, actual)

    def test_question_3(self):
        """
        A real basic test of the question 3 solution.
        :return None
        """
        actual = get_filtered_list(range(11))
        expected = [4, 5, 6, 7, 8, 9, 10]
        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

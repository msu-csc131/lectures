"""
File: student.py
Resources to manage a student's name and test scores.
"""


class Student(object):
    """Represents a student."""

    def __init__(self, name: str, number: float):
        """
        Initialize a Student instance with given name and the number of scores to associate with the given Student.
        :param name: The name of this Student.
        :param number: The number of scores to track for this Student; all scores are initially 0.
        """
        self._name = name
        self._scores = [0] * number

    def get_name(self) -> str:
        """
        Name accessor method.
        :return: The name of this Student is returned.
        """
        return self._name

    def set_score(self, score_index: int, score: float) -> None:
        """
        Score mutator method for the ith score associated with this Student when counting from 1.
        :param score_index: The index of the score to set or change.
        :param score: The new score to keep that is accessible via the given index.
        :return: None
        """
        self._scores[score_index - 1] = score

    def get_score(self, score_index) -> float:
        """
        Score accessor method for the ith score associated with this Student when counting from 1.
        :param score_index: The index of the score to access (when counting from 1).
        :return: The ith score associated with this Student is returned, when counting from 1.
        """
        return self._scores[score_index - 1]

    def get_average(self) -> float:
        """
        Calculate the average score associated with this Student.
        :return: The average score of all the scores for this Student is returned.
        """
        return sum(self._scores) / len(self._scores)

    def get_high_score(self) -> float:
        """
        Determine the highest score associated with this Student.
        :return: The highest score associated with this Student is returned.
        """
        return max(self._scores)

    def __str__(self):
        """
        Return a string representation of this Student.
        :return: A string representation of this Student is returned.
        """
        return "Name: " + self._name + "\nScores: " + \
               " ".join(map(str, self._scores))


def main():
    """A simple test."""
    student = Student("Ken", 5)
    print(student)
    student.set_score(1, 89)
    for i in range(2, 6):
        student.set_score(i, 100)
    print(student)
    print("{} has an average score of {}.".format(student.get_name(), student.get_average()))
    print("{}'s highest score is {}.".format(student.get_name(), student.get_high_score()))
    print("{}'s first score was {}.".format(student.get_name(), student.get_score(1)))
    help(Student)


if __name__ == "__main__":
    main()

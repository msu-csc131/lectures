"""
File: rational.py
Resources to manipulate rational numbers.
"""


class Rational(object):
    """Represents a rational number."""

    def __init__(self, numerator: int, denominator: int):
        """
        Constructor creates a number with the given numerator and denominator and reduces it to lowest terms.
        :param numerator: the numerator of this Rational number
        :param denominator: the denominator of this Rational number
        """
        self._numerator = numerator
        self._denominator = denominator
        self._reduce()

    def numerator(self) -> int:
        """
        Returns the numerator.
        :return The numerator of this Rational number is returned.
        """
        return self._numerator

    def denominator(self) -> int:
        """
        Returns the denominator.
        :return The denominator of this Rational number is returned.
        """
        return self._denominator

    def __str__(self) -> str:
        """
        Returns the string representation of the number.
        :return A string representation of this Rational number is returned.
        """
        return str(self._numerator) + "/" + str(self._denominator)

    def _reduce(self) -> None:
        """
        Helper to reduce the number to lowest terms. Note that the name with the "_" prefix *suggests* this is a private
        method.
        """
        divisor = self._gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // divisor
        self._denominator = self._denominator // divisor

    def _gcd(self, a, b) -> int:
        """
        Euclid's algorithm for greatest common divisor. Note that the name with the "_" prefix *suggests* this is a
        private method.
        :param a: an integer
        :param b: another integer
        :return The greatest common divisor of the parameters a and b is returned.
        """
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
            (a, b) = (b, a % b)
        return a

    # Methods for arithmetic and comparisons go here

    def __add__(self, other):
        """
        Returns the sum of the numbers.
        :param other: the right-hand operand of of self + other
        :return The sum of this Rational number and the other is returned.
        """
        new_numerator = self._numerator * other.denominator() + other.numerator() * self._denominator
        new_denominator = self._denominator * other.denominator()
        return Rational(new_numerator, new_denominator)

    def __lt__(self, other):
        """
        Returns self < other.
        :param other: The right-hand side of the expression self < other
        :return True is returned if self < other; False otherwise.
        """
        extremes = self._numerator * other.denominator()
        means = other.numerator() * self._denominator
        return extremes < means

    def __ge__(self, other):
        """
        Returns self >= other.
        :param other: The right-hand side of the expression self >= other
        :return True is returned if self >= other; False otherwise.
        """
        extremes = self._numerator * other.denominator()
        means = other.numerator() * self._denominator
        return extremes >= means

    def __eq__(self, other):
        """
        Tests self and other for equality.
        :param other: The right-hand side of the expression self == other
        :return True is returned if self == other; False otherwise.
        """
        if self is other:
            return True
        elif not isinstance(other, Rational):
            return False
        else:
            return self._numerator == other.numerator() and \
                   self._denominator == other.denominator()


def main():
    one_half = Rational(1, 2)
    one_sixth = Rational(1, 6)
    print("one_half =              {}".format(one_half))
    print("one_half + one_sixth =  {}".format(one_half + one_sixth))
    print("one_half == one_sixth = {}".format(one_half == one_sixth))
    print("one_half >= one_sixth = {}".format(one_half >= one_sixth))


if __name__ == "__main__":
    main()
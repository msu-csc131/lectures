def fib_tabulation(n: int) -> int:
    """
    Tabulation (Bottom up): The tabulated program for a given problem builds a
    a table in bottom up fashion and returns the last entry from the table. For
    example, for the some Fibonacci number, we first calculate fib(0), then
    fib(1) then fib(2), and so on. So literally, we are building the solutions
    of sub-problems bottom-up.
    :param n: the index into the Fibonacci sequence
    :return: The nth Fibonacci number is returned.
    """

    # array declaration
    f = [0] * (n + 1)

    # base case assignment
    f[1] = 1

    # calculating the Fibonacci and storing the values
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


def fib_memoization(n: int, lookup: dict) -> int:
    """
    Memoization (Top Down): The memoized program for a problem is similar to
    the recursive version with a small modification that it looks into a
    lookup table (dictionary) before computing solutions. We initialize a
    lookup dictionary. Whenever we need solution to a sub-problem, we first
    look into the lookup table. If the precomputed value is there then we
    return that value, otherwise we calculate the value and put the result in
    the lookup table so it can be reused later.
    :param n: the index into the Fibonacci sequence
    :param lookup: a dictionary of already computed values
    :return: The nth Fibonacci number is returned.
    """
    # Base case
    if n == 1 or n == 2:
        lookup[n] = 1

    # If the value is not calculated previously, then calculate it
    if lookup.get(n, None) is None:
        lookup[n] = fib_memoization(n - 1, lookup) + fib_memoization(n - 2, lookup)

    # Return the value corresponding to that value of n
    return lookup[n]


def main() -> int:
    # Declaration of lookup table
    lookup = {}
    n = fib_memoization(50, lookup)
    print(n)
    n = fib_tabulation(50)
    print(n)
    return 0


if __name__ == '__main__':
    main()

def factorial(n):
    """
    spec:
        title: Factorial
        domain -1:
            title: Should be incalculable for negative values
            description:
                Function raises proper exception
                when called with negative value
            throws ValueError('factorial() not defined for negative values')
        domain 0:
            title: Should return 1 on boundary
            description: Function should return 0 when called with 0
            results 1
        domain 1: results 1
        domain 3: results 6
        domain 4: results 24
        domain 5: results 120
    """
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    if n == 0:
        return 1
    return n * factorial(n - 1)

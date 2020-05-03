def square_derivative(x):
    """
    spec:
        domain 10:
            result between (19.9, 20.1)
    """
    eps = 0.01
    f = lambda x: x * x
    return (f(x + eps) - f(x)) / eps

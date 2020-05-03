def flatten_positive(x):
    """
    spec:
        domain -32: results -32
        domain 0: results 0
        domain interval (0, Infinity): results 0

        # Floats are also allowed
        domain -67.6: results -67.6
        domain interval (0.0, Infinity): results 0.0
    """
    if x > 0:
        return 0
    return x

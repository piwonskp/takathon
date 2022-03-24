class StaticMethods:
    x = 5
    y = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def sub(a, b):
        """
        spec:
            domain 10, 7: results 3
            # Check if creation of an object changes the result
            new 40, 32
            domain 10, 7: results 3
        """
        return a - b

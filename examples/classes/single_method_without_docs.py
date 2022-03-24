class SingleMethodWithoutDocs:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, c):
        """
        spec:
            # Test creation of object
            new 10, 20
            domain 2: results 32
            # Make sure object is replaced with a new one
            new -6, 2
            domain 4: results 0
        """
        return self.a + self.b + c

    def sub(self):
        """
        spec:
            new 20, 10
            domain : results 10
            new 40, 32
            domain : results 8
        """
        return self.a - self.b

    def mul(self):
        return self.a * self.b

class SingleMethodWithoutDocs:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, c):
        """
        spec:
            # TEST COMMMENT
            new 10, 20
            domain 2: results 32
            new -6, 2
            # USELESS COMMENT
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

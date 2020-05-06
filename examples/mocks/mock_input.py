def increment_input():
    """
    spec:
        title: Incrementation of input
        from unittest.mock import MagicMock
        domain:
            title: Should return 4 when input is 3
            mock .input as MagicMock(return_value='3')
            results 4
    """
    return int(input()) + 1

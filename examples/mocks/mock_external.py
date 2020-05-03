from examples.mocks.mock_input import increment_input
from examples.result_validation.factorial import factorial


def mock_external():
    """
    spec:
        mock examples.mocks.mock_input.input as Mock(return_value=1)
        domain : results 2
        mock examples.mocks.mock_input.input as Mock(return_value=5)
        domain : results 720
    """
    value = increment_input()
    return factorial(value)

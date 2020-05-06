Mocks
*****

Mocking within the same module
------------------------------

To indicate that mocked object is in the same module as procedure being tested prepend the name of it with dot.

.. literalinclude:: ../../../examples/mocks/mock_input.py

Mocking external module
-----------------------
Let's assume you want to reuse procedure defined in previous paragraph. To do that you have to specify absolute path to `input`. In this case mocked procedure is contained within `examples.mocks.mock_input` module. Note that you don't have to import `Mock` to scope since it is already builtin.

.. literalinclude:: ../../../examples/mocks/mock_external.py

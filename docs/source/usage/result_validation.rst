Result validation
*****************

Apart from standard result validation there are also other methods of validating correctness of function call.

Throws
======

If function is expected to raise an exception for particular input you can use `throws` statement.

.. literalinclude:: ../../../examples/result_validation/factorial.py

Between
=======
If your function returns inaccurate results you can use `between` to validate if result is in desired range. 

.. literalinclude:: ../../../examples/result_validation/inaccurate_result.py

Validate by function
====================
The most generic way of validating result. At first you have to define predicate in plain Python. The predicate is of type `Result -> Bool` ie. takes the result of function call and returns boolean. The boolean value indicates whether test passed or not. 

.. literalinclude:: ../../../examples/result_validation/check_by_function/test_utils.py

You can either define the predicate in the same file or import it for the sake of test/code separation as shown below. To validate result using function use `result <foo_name>` statement.

.. literalinclude:: ../../../examples/result_validation/check_by_function/check_by_function.py

OOP features
*****************

The language supports object oriented programming features such as creating objects. The features provide the way to perform basic method testing. Advanced test scenarios for classes are not supported yet.

Static methods
==============
Static methods can be tested like any other procedure.

.. literalinclude:: ../../../examples/classes/static_methods.py


Methods
=========
To create an object `new` keyword is used. `new` keyword creates the object by passing arguments to the class constructor. It provides a way to realize the test scenario:

.. code-block:: python

    new_object = ClassName(constructor_arguments)
    result = new_object.method(method_arguments)
    assert result == expected_result

This test scenario allows to test methods as separate units independently of other methods of the class.

.. literalinclude:: ../../../examples/classes/single_method_without_docs.py
